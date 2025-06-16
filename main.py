from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import JSONResponse
from deepface import DeepFace
import numpy as np
import faiss
from PIL import Image
import io
import os

app = FastAPI()

# In-memory DB: list of (id, embedding)
face_db = []  # [(str, np.ndarray)]
face_ids = []

# FAISS index (cosine similarity)
embedding_dim = 128  # Default for Facenet; can be changed
index = faiss.IndexFlatIP(embedding_dim)

# Helper: extract embedding from image bytes
def get_embedding(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    # DeepFace expects a file path or numpy array
    img_np = np.array(img)
    # Get embedding (use Facenet for speed)
    embedding = DeepFace.represent(img_path = img_np, model_name = 'Facenet')[0]['embedding']
    return np.array(embedding, dtype='float32')

@app.post('/add_face')
def add_face(id: str = Form(...), file: UploadFile = File(...)):
    image_bytes = file.file.read()
    embedding = get_embedding(image_bytes)
    # Normalize for cosine similarity
    embedding = embedding / np.linalg.norm(embedding)
    face_db.append((id, embedding))
    face_ids.append(id)
    # Add to FAISS
    index.add(np.expand_dims(embedding, 0))
    return {"status": "added", "id": id}

@app.post('/match_face')
def match_face(file: UploadFile = File(...)):
    if len(face_db) == 0:
        raise HTTPException(status_code=400, detail="No faces in DB.")
    image_bytes = file.file.read()
    embedding = get_embedding(image_bytes)
    embedding = embedding / np.linalg.norm(embedding)
    # Search in FAISS
    D, I = index.search(np.expand_dims(embedding, 0), 1)  # top 1
    best_idx = I[0][0]
    best_score = float(D[0][0])
    best_id = face_ids[best_idx]
    return {"id": best_id, "score": best_score}

@app.get('/')
def root():
    return {"status": "ok"} 