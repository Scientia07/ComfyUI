#!/bin/bash

# FLUX.1-dev Model Downloader for ComfyUI
# This script sets up the environment and downloads all required models

echo "🚀 ComfyUI FLUX.1-dev Model Downloader"
echo "======================================"

# Check if we're in the right directory
if [ ! -f "src/index.py" ]; then
    echo "❌ Error: Please run this script from the comfyui-hf-integration directory"
    echo "Current directory: $(pwd)"
    echo "Expected files: src/index.py, requirements.txt"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "../../comfy-env" ]; then
    echo "❌ Error: ComfyUI virtual environment not found at ../../comfy-env"
    echo "Please make sure ComfyUI is properly installed with its virtual environment"
    exit 1
fi

echo "✅ Found ComfyUI virtual environment"

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source ../../comfy-env/bin/activate

# Install/upgrade requirements
echo "📦 Installing/updating dependencies..."
pip install -r requirements.txt

# Check if user is logged into HuggingFace
echo "🔐 Checking HuggingFace authentication..."
if ! python -c "from huggingface_hub import HfApi; HfApi().whoami()" 2>/dev/null; then
    echo "⚠️  You are not logged into HuggingFace Hub."
    echo "For FLUX.1-dev, you need to:"
    echo "1. Create an account at https://huggingface.co"
    echo "2. Accept the license at https://huggingface.co/black-forest-labs/FLUX.1-dev"
    echo "3. Run: huggingface-cli login"
    echo ""
    read -p "Do you want to login now? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        huggingface-cli login
    else
        echo "❌ Cannot proceed without HuggingFace authentication"
        exit 1
    fi
fi

echo "✅ HuggingFace authentication OK"

# Run the downloader
echo "🎯 Starting model download..."
python src/index.py

echo "🎉 Download script completed!"
echo "Check the output above for any errors." 