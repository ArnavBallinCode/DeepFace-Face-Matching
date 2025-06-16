#!/usr/bin/env python3
"""
Test script for the DeepFace API
"""
import requests
import json

API_BASE = "http://localhost:8000"

def test_add_face():
    """Test adding a face to the database"""
    print("Testing /add_face endpoint...")
    
    with open('img1.jpg', 'rb') as f:
        files = {'file': ('img1.jpg', f, 'image/jpeg')}
        data = {'id': 'person1'}
        
        response = requests.post(f"{API_BASE}/add_face", files=files, data=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200

def test_match_face():
    """Test matching a face against the database"""
    print("\nTesting /match_face endpoint...")
    
    with open('img10.jpg', 'rb') as f:
        files = {'file': ('img10.jpg', f, 'image/jpeg')}
        
        response = requests.post(f"{API_BASE}/match_face", files=files)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200

def test_root():
    """Test the root endpoint"""
    print("Testing root endpoint...")
    response = requests.get(API_BASE)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.status_code == 200

if __name__ == "__main__":
    print("Starting API tests...\n")
    
    # Test root endpoint
    if not test_root():
        print("Root endpoint failed!")
        exit(1)
    
    # Test adding a face
    if not test_add_face():
        print("Add face endpoint failed!")
        exit(1)
    
    # Test matching a face
    if not test_match_face():
        print("Match face endpoint failed!")
        exit(1)
    
    print("\nAll tests passed! 🎉")
