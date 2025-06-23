#!/bin/bash

echo "🔥 ComfyUI CUDA Fix Script"
echo "=========================="

# Navigate to ComfyUI directory
cd "$(dirname "$0")"

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source comfy-env/bin/activate

# Clear CUDA environment variables
echo "🧹 Clearing CUDA environment variables..."
unset CUDA_VISIBLE_DEVICES
unset CUDA_DEVICE_ORDER

# Uninstall existing PyTorch
echo "🗑️ Uninstalling existing PyTorch..."
pip uninstall -y torch torchvision torchaudio

# Install PyTorch with CUDA 12.1 support (compatible with your CUDA 12.2)
echo "⬇️ Installing PyTorch with CUDA support..."
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Install missing dependencies
echo "📦 Installing missing dependencies..."
pip install opencv-python diffusers accelerate

# Test CUDA setup
echo "🧪 Testing CUDA setup..."
python3 -c "
import torch
print(f'PyTorch version: {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'CUDA device count: {torch.cuda.device_count()}')
    print(f'Device name: {torch.cuda.get_device_name(0)}')
    print(f'CUDA version: {torch.version.cuda}')
    
    # Test CUDA operation
    x = torch.randn(3, 3).cuda()
    y = torch.randn(3, 3).cuda()
    z = torch.matmul(x, y)
    print('✅ CUDA operation successful!')
else:
    print('❌ CUDA still not available')
"

echo "🎉 CUDA fix completed!"
echo "You can now run ComfyUI with GPU acceleration." 