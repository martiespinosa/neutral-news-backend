import os
import sys
import time
import importlib

def preload_minimal_dependencies():
    """Preload only the essential dependencies needed for startup"""
    start = time.time()
    print("⏳ Preloading minimal dependencies for startup...")
    
    # Only preload functions_framework and other essential modules
    # Heavy ML modules will be loaded in parallel during execution
    modules = [
        "functions_framework",
        "flask",
        "json",
        "concurrent.futures",
        "threading"
    ]
    
    for module in modules:
        print(f"  ⏳ Loading {module}...")
        importlib.import_module(module)
    
    print(f"✅ Minimal dependencies preloaded in {time.time() - start:.2f} seconds")

# Run minimal preloading, then hand over to functions-framework
if __name__ == "__main__":
    preload_minimal_dependencies()
    
    # Determine function target from environment variable or use default
    function_target = os.environ.get("FUNCTION_TARGET", "fetch_news")
    port = int(os.environ.get("PORT", "8080"))
    
    # Import and use functions_framework directly
    import functions_framework
    
    try:
        # Dynamically import the target function
        module_path, function_name = function_target.rsplit('.', 1) if '.' in function_target else ('main', function_target)
        module = importlib.import_module(module_path)
        
        # Register the function with functions_framework
        app = functions_framework.create_app(target=function_target)
        
        # Start the server using the Flask app directly
        print(f"Starting Flask server on port {port}")
        app.run(host='0.0.0.0', port=port, debug=False)
    except Exception as e:
        print(f"Error starting functions-framework: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)