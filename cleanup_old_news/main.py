# main.py for cleanup_old_news
import traceback
from src.functions.scheduled_tasks import cleanup_old_news_task

def cleanup_old_news() -> None:
    """Triggers the cleanup_old_news_task."""
    try:
        print("Executing cleanup_old_news task...")
        cleanup_old_news_task()
        print("cleanup_old_news task completed.")
    except Exception as e:
        print(f"Error in cleanup_old_news function: {str(e)}")
        traceback.print_exc()

# Ensure the function is registered if running locally with functions-framework
# functions-framework --target cleanup_old_news --source .