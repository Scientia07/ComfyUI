#!/bin/bash

echo "🧪 Post-Driver Update CUDA Test"
echo "==============================="

# Check new driver version
echo "📊 New Driver Information:"
nvidia-smi --query-gpu=driver_version,cuda_version --format=csv,noheader

echo ""
echo "🔥 Testing CUDA with PyTorch..."

# Set correct environment and test CUDA
export LD_LIBRARY_PATH=""
export PYTHONPATH="/home/joel/dev/AI/ComfyUI/comfy-env/lib/python3.12/site-packages"

cd /home/joel/dev/AI/ComfyUI

python3 -c "
import torch
print(f'PyTorch version: {torch.__version__}')
print(f'CUDA compiled version: {torch.version.cuda}')
print(f'CUDA available: {torch.cuda.is_available()}')

if torch.cuda.is_available():
    print(f'🎉 CUDA WORKING!')
    print(f'Device count: {torch.cuda.device_count()}')
    print(f'Device name: {torch.cuda.get_device_name(0)}')
    print(f'Device memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB')
    
    # Test CUDA operation
    print('\\n🧮 Testing CUDA operations...')
    x = torch.randn(1000, 1000, device='cuda')
    y = torch.randn(1000, 1000, device='cuda')
    
    import time
    start = time.time()
    z = torch.matmul(x, y)
    end = time.time()
    
    print(f'✅ Matrix multiplication on GPU: {end-start:.4f} seconds')
    print(f'Result shape: {z.shape}')
    print('\\n🎉 CUDA fully functional!')
    
else:
    print('❌ CUDA still not available')
    print('Driver update may not have resolved the issue')
"

echo ""
echo "🚀 If CUDA is working, you can now run ComfyUI with GPU:"
echo "cd /home/joel/dev/AI/ComfyUI"
echo "PYTHONPATH=/home/joel/dev/AI/ComfyUI/comfy-env/lib/python3.12/site-packages python3 main.py" 