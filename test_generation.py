#!/usr/bin/env python3
"""
Quick GPU Test Image Generation
This will generate a test image to verify CUDA is working
"""

import json
import urllib.request
import time
import sys
import os

# Set correct Python path
sys.path.insert(0, '/home/joel/dev/AI/ComfyUI/comfy-env/lib/python3.12/site-packages')

def queue_prompt(prompt):
    """Send a prompt to ComfyUI"""
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    req = urllib.request.Request("http://127.0.0.1:8188/prompt", data=data)
    try:
        response = urllib.request.urlopen(req)
        return json.loads(response.read())
    except Exception as e:
        print(f"Error sending prompt: {e}")
        return None

def check_server():
    """Check if ComfyUI server is running"""
    try:
        req = urllib.request.Request("http://127.0.0.1:8188/")
        urllib.request.urlopen(req, timeout=5)
        return True
    except:
        return False

# Simple test prompt (uses default SD 1.5 checkpoint if available)
test_prompt = {
    "3": {
        "class_type": "KSampler",
        "inputs": {
            "seed": 42,
            "steps": 10,
            "cfg": 7.0,
            "sampler_name": "euler",
            "scheduler": "normal",
            "denoise": 1.0,
            "model": ["4", 0],
            "positive": ["6", 0],
            "negative": ["7", 0],
            "latent_image": ["5", 0]
        }
    },
    "4": {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {
            "ckpt_name": "v1-5-pruned-emaonly.safetensors"
        }
    },
    "5": {
        "class_type": "EmptyLatentImage",
        "inputs": {
            "width": 512,
            "height": 512,
            "batch_size": 1
        }
    },
    "6": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": "a beautiful landscape with mountains and a lake, masterpiece, high quality",
            "clip": ["4", 1]
        }
    },
    "7": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": "bad quality, blurry, ugly",
            "clip": ["4", 1]
        }
    },
    "8": {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": ["3", 0],
            "vae": ["4", 2]
        }
    },
    "9": {
        "class_type": "SaveImage",
        "inputs": {
            "filename_prefix": "CUDA_TEST",
            "images": ["8", 0]
        }
    }
}

def main():
    print("🖼️ ComfyUI GPU Test Image Generation")
    print("=" * 40)
    
    # Check if server is running
    if not check_server():
        print("❌ ComfyUI server not running at http://127.0.0.1:8188")
        print("Make sure ComfyUI is started first!")
        return
    
    print("✅ ComfyUI server is running!")
    print("🎨 Generating test image with GPU acceleration...")
    print("   Prompt: 'a beautiful landscape with mountains and a lake'")
    print("   Size: 512x512")
    print("   Steps: 10 (quick test)")
    
    # Queue the prompt
    start_time = time.time()
    result = queue_prompt(test_prompt)
    
    if result:
        prompt_id = result.get('prompt_id')
        print(f"✅ Image generation started! Prompt ID: {prompt_id}")
        print("⏰ Generation in progress...")
        print("📁 Check the 'output' folder for the generated image!")
        print("🖼️ Image will be saved as 'CUDA_TEST_*.png'")
        
        # The generation happens asynchronously, so we can't wait for completion easily
        # But we can tell the user where to look
        generation_time = time.time() - start_time
        print(f"🚀 Prompt queued in {generation_time:.2f} seconds")
        print("\n💡 Tips:")
        print("   - Watch the ComfyUI logs: tail -f comfyui.log")
        print("   - Check GPU usage: nvidia-smi")
        print("   - Open web UI: http://localhost:8188")
        
    else:
        print("❌ Failed to queue image generation")
        print("Check the ComfyUI logs for errors")

if __name__ == "__main__":
    main() 