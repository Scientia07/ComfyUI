#!/bin/bash

# ComfyUI Launch Script
# Handles environment setup for CUDA compatibility

echo "🚀 Launching ComfyUI with optimized environment..."

# Change to ComfyUI directory
cd /home/joel/dev/AI/ComfyUI

# Activate virtual environment
echo "📦 Activating ComfyUI virtual environment..."
source comfy-env/bin/activate

# Clean environment variables to resolve CUDA conflicts
echo "🧹 Setting clean environment paths..."
export LD_LIBRARY_PATH=''
export PYTHONPATH='/home/joel/dev/AI/ComfyUI/comfy-env/lib/python3.12/site-packages'

# Verify CUDA availability
echo "🔍 Checking CUDA availability..."
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}'); print(f'CUDA device count: {torch.cuda.device_count()}'); print(f'Current device: {torch.cuda.current_device() if torch.cuda.is_available() else \"None\"}')"

echo "🎨 Starting ComfyUI..."
echo "Access ComfyUI at: http://localhost:8188"
echo "Press Ctrl+C to stop"
echo ""

# Launch ComfyUI
python main.py 