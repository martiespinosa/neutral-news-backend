import traceback
import threading
import time
from flask import jsonify
from concurrent.futures import ThreadPoolExecutor

def fetch_news(request):
    """HTTP Cloud Function that processes a request from Cloud Scheduler."""
    print("Ejecutando fetch_news function with parallel optimization...")
    try:
        start_time = time.time()
        
        # Start ML preloading in background
        ml_thread = threading.Thread(target=preload_ml_dependencies, daemon=True)
        ml_thread.start()
        
        # Run RSS fetching in main thread
        print("🔍 Starting RSS fetching while ML dependencies load in background...")
        from src.parsers import fetch_all_rss
        from src.storage import store_news_in_firestore
        all_news = fetch_all_rss()
        stored_count = store_news_in_firestore(all_news)
        print(f"✅ RSS fetching and storage completed in {time.time() - start_time:.2f} seconds")
        
        # Start ML processing WITHOUT waiting for dependencies yet
        print("🧠 Starting ML processing tasks...")
        from src.process import process_news_groups
        # Pass the ML thread to process_news_groups
        process_news_groups(ml_thread)
        
        total_time = time.time() - start_time
        print(f"✅ Total execution completed in {total_time:.2f} seconds")
        return jsonify({
            "success": True, 
            "message": "News fetching and processing completed successfully",
            "execution_time_seconds": total_time
        })
    except Exception as e:
        error_message = f"Error en fetch_news function: {str(e)}"
        print(error_message)
        traceback.print_exc()
        return jsonify({"success": False, "error": error_message}), 500

def preload_ml_dependencies():
    """Load ML dependencies in parallel threads"""
    print("⏳ Preloading ML dependencies in background...")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Start model loading first (most I/O intensive)
        model_future = executor.submit(load_sentence_transformer)
        
        # Start loading other packages in parallel
        basic_deps_future = executor.submit(load_basic_ml_deps)
        sklearn_future = executor.submit(load_sklearn_deps)
        
        # Wait for all to complete
        basic_deps_future.result()
        sklearn_future.result()
        model = model_future.result()
    
    print(f"✅ ML dependencies loading completed in {time.time() - start_time:.2f} seconds")
    return True

def load_sentence_transformer():
    """Load the SentenceTransformer model (I/O intensive)"""
    print("  ⏳ Loading SentenceTransformer model...")
    from src.singletons.sbert_singleton import get_sbert
    model = get_sbert()
    print("  ✓ Loaded SentenceTransformer model")
    return model

def load_basic_ml_deps():
    """Load basic ML dependencies"""
    import numpy
    print("  ✓ Loaded numpy")
    import pandas
    print("  ✓ Loaded pandas")
    import scipy.sparse
    print("  ✓ Loaded scipy.sparse")
    return True

def load_sklearn_deps():
    """Load scikit-learn dependencies"""
    import sklearn.neighbors
    print("  ✓ Loaded sklearn.neighbors")
    import sklearn.cluster
    print("  ✓ Loaded sklearn.cluster")
    return True