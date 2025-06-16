#!/usr/bin/env python3
"""
Test script for the DeepFace ArcFace API
"""
import requests
import json

API_BASE = "http://localhost:8002"

def test_arcface_api():
    """Test the ArcFace API functionality"""
    print("🧪 Testing ArcFace API...")
    print("=" * 50)
    
    # Test root endpoint
    print("1. Testing root endpoint...")
    response = requests.get(API_BASE)
    if response.status_code == 200:
        data = response.json()
        print(f"   ✅ API running with {data['model']} model")
        print(f"   📊 Embedding dimensions: {data['embedding_dimensions']}")
        print(f"   🗃️ Faces in database: {data['faces_in_database']}")
    else:
        print(f"   ❌ Failed: {response.status_code}")
        return False
    
    # Test adding a face
    print("\n2. Testing add_face endpoint...")
    try:
        with open('img1.jpg', 'rb') as f:
            files = {'file': ('img1.jpg', f, 'image/jpeg')}
            data = {'id': 'person1_arcface'}
            
            response = requests.post(f"{API_BASE}/add_face", files=files, data=data)
            if response.status_code == 200:
                result = response.json()
                print(f"   ✅ Face added successfully")
                print(f"   ⚡ Processing time: {result['details']['processing_time']}")
                print(f"   🎯 Model: {result['details']['model']}")
                print(f"   📏 Dimensions: {result['details']['dimensions']}")
            else:
                print(f"   ❌ Failed: {response.status_code} - {response.text}")
                return False
    except FileNotFoundError:
        print("   ⚠️ img1.jpg not found, skipping add face test")
    
    # Test matching a face
    print("\n3. Testing match_face endpoint...")
    try:
        with open('img10.jpg', 'rb') as f:
            files = {'file': ('img10.jpg', f, 'image/jpeg')}
            
            response = requests.post(f"{API_BASE}/match_face", files=files)
            if response.status_code == 200:
                result = response.json()
                best_match = result['best_match']
                print(f"   ✅ Face matching completed")
                print(f"   🎯 Best match: {best_match['id']}")
                print(f"   📊 Confidence: {best_match['confidence']}%")
                print(f"   📏 Distance: {best_match['distance']}")
                print(f"   ✨ Is match: {best_match['is_match']}")
                print(f"   ⚡ Processing time: {result['query_info']['processing_time']}")
            else:
                print(f"   ❌ Failed: {response.status_code} - {response.text}")
    except FileNotFoundError:
        print("   ⚠️ img10.jpg not found, skipping match test")
    
    # Test statistics
    print("\n4. Testing stats endpoint...")
    response = requests.get(f"{API_BASE}/stats")
    if response.status_code == 200:
        stats = response.json()
        print(f"   ✅ Stats retrieved successfully")
        print(f"   🗃️ Total faces: {stats['database_stats']['total_faces']}")
        print(f"   🤖 Model: {stats['model_info']['name']}")
        print(f"   🎚️ Threshold: {stats['model_info']['similarity_threshold']}")
    else:
        print(f"   ❌ Failed: {response.status_code}")
    
    print("\n🎉 ArcFace API testing completed!")
    return True

if __name__ == "__main__":
    test_arcface_api()
