#!/bin/bash

echo "🔥 CUDA Environment Fix Script"
echo "=============================="
echo "Issue: LD_LIBRARY_PATH contaminated by Cursor AppImage"
echo ""

# Save original LD_LIBRARY_PATH
ORIGINAL_LD_LIBRARY_PATH="$LD_LIBRARY_PATH"

# Clean LD_LIBRARY_PATH of Cursor paths
CLEAN_LD_LIBRARY_PATH=$(echo "$LD_LIBRARY_PATH" | tr ':' '\n' | grep -v '.mount_Cursor' | tr '\n' ':' | sed 's/:*$//')

echo "🧹 Cleaning LD_LIBRARY_PATH..."
echo "Original: $ORIGINAL_LD_LIBRARY_PATH"
echo "Cleaned:  $CLEAN_LD_LIBRARY_PATH"
echo ""

# Export the clean path
export LD_LIBRARY_PATH="$CLEAN_LD_LIBRARY_PATH"

# Also clear any CUDA env vars that might be interfering
unset CUDA_VISIBLE_DEVICES
unset CUDA_DEVICE_ORDER

echo "🧪 Testing CUDA with clean environment..."
PYTHONPATH=/home/joel/dev/AI/ComfyUI/comfy-env/lib/python3.12/site-packages python3 -c "
import torch
print(f'PyTorch version: {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'Device count: {torch.cuda.device_count()}')
    print(f'Device name: {torch.cuda.get_device_name(0)}')
    # Test CUDA operation
    x = torch.randn(3, 3).cuda()
    y = torch.randn(3, 3).cuda()
    z = torch.matmul(x, y)
    print('✅ CUDA matrix operation successful!')
    print(f'Result shape: {z.shape}')
else:
    print('❌ CUDA still not available')
"

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 CUDA fix successful!"
    echo ""
    echo "📝 To make this permanent, add this to your shell profile:"
    echo 'export LD_LIBRARY_PATH=$(echo "$LD_LIBRARY_PATH" | tr '"'"':'"'"' '"'"'\n'"'"' | grep -v '"'"'.mount_Cursor'"'"' | tr '"'"'\n'"'"' '"'"':'"'"' | sed '"'"'s/:*$//'"'"')'
    echo ""
    echo "🚀 To run ComfyUI with CUDA:"
    echo "LD_LIBRARY_PATH=\"$CLEAN_LD_LIBRARY_PATH\" PYTHONPATH=/home/joel/dev/AI/ComfyUI/comfy-env/lib/python3.12/site-packages python3 main.py"
else
    echo ""
    echo "❌ CUDA fix failed. There may be additional issues."
fi 