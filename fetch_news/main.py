import traceback
from flask import jsonify
from src.functions.scheduled_tasks import fetch_news_task

def fetch_news(request):
    """HTTP Cloud Function that processes a request from Cloud Scheduler.
    
    Args:
        request (flask.Request): The request object.
        
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`.
    """
    print("Ejecutando fetch_news function...")
    try:
        fetch_news_task()
        print("fetch_news task completada.")
        return jsonify({"success": True, "message": "News fetching completed successfully"})
    except Exception as e:
        error_message = f"Error en fetch_news function: {str(e)}"
        print(error_message)
        traceback.print_exc()
        return jsonify({"success": False, "error": error_message}), 500