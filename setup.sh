#!/bin/bash

# DeepFace API Setup Script
# This script sets up the DeepFace API with proper dependencies

echo "🚀 Setting up DeepFace API..."

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "❌ Conda is not installed. Please install Miniconda or Anaconda first."
    echo "Download from: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

# Create conda environment
echo "📦 Creating conda environment with Python 3.11..."
conda create -n deepface python=3.11 -y

# Activate environment
echo "🔧 Activating environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate deepface

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "To start the API:"
echo "1. Activate the environment: conda activate deepface"
echo "2. Run the server: uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
echo "3. Open http://localhost:8000 in your browser"
echo ""
echo "To test the API: python test_api.py"
