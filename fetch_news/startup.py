import os
import sys
import time
import importlib
from src.singletons.sbert_singleton import get_sbert

def preload_dependencies():
    """Preload dependencies to reduce runtime initialization overhead"""
    start = time.time()
    print("⏳ Preloading dependencies to optimize execution time...")
    
    # Preload core ML modules - only valid module paths
    modules = [
        "numpy", 
        "pandas",
        "sentence_transformers",
        "sklearn.neighbors",
        "sklearn.cluster",
        "scipy.sparse",
        "functions_framework"
    ]
    
    for module in modules:
        print(f"  ⏳ Loading {module}...")
        importlib.import_module(module)
    
    # To preload specific classes, import them differently
    print("  ⏳ Loading specific classes...")
    from sklearn.neighbors import NearestNeighbors
    from sklearn.cluster import DBSCAN
    from scipy.sparse import lil_matrix
    print("  ✅ Classes loaded successfully")
    
    # Initialize the SentenceTransformer model
    print("  ⏳ Initializing SentenceTransformer model...")
    get_sbert()  # This will load the model once
    print("  ✅ Model loaded successfully")
    

    
    print(f"✅ Dependencies preloaded in {time.time() - start:.2f} seconds")

# Run preloading, then hand over to functions-framework
if __name__ == "__main__":
    preload_dependencies()
    
    # Determine function target from environment variable or use default
    function_target = os.environ.get("FUNCTION_TARGET", "fetch_news")
    port = int(os.environ.get("PORT", "8080"))
    
    # Import and use functions_framework directly instead of os.system
    import functions_framework
    import importlib
    
    # Dynamically import the target function
    module_path, function_name = function_target.rsplit('.', 1) if '.' in function_target else ('main', function_target)
    
    try:
        module = importlib.import_module(module_path)
        target_function = getattr(module, function_name)
        
        # Register the function with functions_framework
        # Pass the string identifier, not the function object
        app = functions_framework.create_app(target=function_target)
        
        # Start the server using the Flask app directly
        print(f"Starting Flask server on port {port}")
        app.run(host='0.0.0.0', port=port, debug=False)
    except Exception as e:
        print(f"Error starting functions-framework: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)