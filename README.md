# DeepFace Face Matching API

This project provides a FastAPI-based API for face verification using [DeepFace](https://github.com/serengil/deepface) and a vector database (FAISS) for fast similarity search.

## Features
- Add new faces to the database with an ID and image
- Match a query face image against the database
- Returns the highest matching face and similarity score

## Setup

### Prerequisites
- Python 3.11 (required for TensorFlow compatibility)
- Conda (recommended for environment management)

### Installation

1. **Create a conda environment with Python 3.11:**
   ```bash
   conda create -n deepface python=3.11 -y
   conda activate deepface
   ```

2. **Install dependencies:**
   ```bash
   # Use the environment's pip to ensure correct package installation
   pip install -r requirements.txt
   ```

3. **Run the API:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Access the API:**
   - Open your browser to `http://localhost:8000`
   - Interactive API documentation: `http://localhost:8000/docs`

### Troubleshooting

If you encounter dependency conflicts:
- Make sure you're using Python 3.11 (TensorFlow doesn't support Python 3.13 yet)
- Use a clean conda environment
- Install TensorFlow first if needed: `pip install tensorflow`

### Testing

Run the included test script to verify everything is working:
```bash
python test_api.py
```

This will test all endpoints and confirm the API is functioning correctly.

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