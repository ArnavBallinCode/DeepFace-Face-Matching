# DeepFace Face Matching API

This project provides a FastAPI-based API for face verification using [DeepFace](https://github.com/serengil/deepface) and a vector database (FAISS) for fast similarity search.

## Features
- Add new faces to the database with an ID and image
- Match a query face image against the database
- Returns the highest matching face and similarity score

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the API:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### 1. Add a Face
- **POST** `/add_face`
- **Form fields:**
  - `id`: string (unique identifier for the face)
  - `file`: image file (jpg/png)
- **Example (using curl):**
  ```bash
  curl -F "id=person1" -F "file=@/path/to/image.jpg" http://localhost:8000/add_face
  ```

### 2. Match a Face
- **POST** `/match_face`
- **Form fields:**
  - `file`: image file (jpg/png)
- **Returns:**
  - `id`: best matching face ID
  - `score`: similarity score (cosine similarity, 1.0 = perfect match)
- **Example:**
  ```bash
  curl -F "file=@/path/to/query.jpg" http://localhost:8000/match_face
  ```

## Notes
- The database is in-memory and will reset when the server restarts.
- Uses DeepFace's Facenet model (128D embeddings) by default.
- For production, consider persistent storage and authentication.

## References
- [DeepFace GitHub](https://github.com/serengil/deepface)
- [FAISS](https://github.com/facebookresearch/faiss) 