from sentence_transformers import SentenceTransformer
import os

_model = None

def get_sbert():
    global _model
    if _model is not None:
        return _model
        
    bundled_model_path = "/app/model"
    if os.path.exists(bundled_model_path):
        print(f"Loading model from {bundled_model_path}...")
        _model = SentenceTransformer(bundled_model_path)
        print(f"Model loaded successfully")
    else:
        print(f"Model path not found: {bundled_model_path}")
        # Fall back to downloading from HuggingFace
        _model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        
    return _model