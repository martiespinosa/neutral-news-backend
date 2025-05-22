import traceback
import firebase_admin
from firebase_admin import credentials, firestore

_firebase_client = None

def get_firebase_db():
    """Get or initialize the Firebase client."""
    global _firebase_client
    if _firebase_client is not None:
        return _firebase_client
    
    try:
        try:
            app = firebase_admin.get_app()
        except ValueError:
            cred = credentials.ApplicationDefault()
            app = firebase_admin.initialize_app(cred)
        
        _firebase_client = firestore.client()
        return _firebase_client
    except Exception as e:
        print(f"Error initializing Firebase: {str(e)}")
        traceback.print_exc()
        raise