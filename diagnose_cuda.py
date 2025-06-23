#!/usr/bin/env python3
"""
Comprehensive CUDA Diagnostic Script
This script will help identify the exact CUDA driver compatibility issue
"""

import subprocess
import sys
import os

def run_cmd(cmd):
    """Run a command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def main():
    print("🔍 COMPREHENSIVE CUDA DIAGNOSTIC")
    print("=" * 50)
    
    # System info
    print("\n📊 SYSTEM INFORMATION:")
    print("-" * 30)
    
    # Kernel version
    ret, out, err = run_cmd("uname -r")
    if ret == 0:
        print(f"Kernel: {out.strip()}")
    
    # Driver version from nvidia-smi
    ret, out, err = run_cmd("nvidia-smi --query-gpu=driver_version --format=csv,noheader")
    if ret == 0:
        print(f"NVIDIA Driver: {out.strip()}")
    
    # CUDA version from nvidia-smi
    ret, out, err = run_cmd("nvidia-smi --query-gpu=cuda_version --format=csv,noheader")
    if ret == 0:
        print(f"CUDA Version (from driver): {out.strip()}")
    
    # Check libcuda
    print(f"\n🔗 CUDA LIBRARIES:")
    print("-" * 30)
    
    ret, out, err = run_cmd("ldconfig -p | grep libcuda")
    if ret == 0:
        print("libcuda.so locations:")
        print(out)
    else:
        print("❌ libcuda.so not found in ldconfig")
    
    # Check if CUDA library is accessible
    ret, out, err = run_cmd("ls -la /usr/lib/x86_64-linux-gnu/libcuda.so*")
    if ret == 0:
        print("CUDA library files:")
        print(out)
    
    # Set the correct PYTHONPATH and test
    venv_path = "/home/joel/dev/AI/ComfyUI/comfy-env/lib/python3.12/site-packages"
    os.environ['PYTHONPATH'] = venv_path
    
    print(f"\n🐍 PYTORCH DIAGNOSIS:")
    print("-" * 30)
    
    try:
        import torch
        print(f"PyTorch version: {torch.__version__}")
        print(f"PyTorch compiled with CUDA: {torch.version.cuda}")
        print(f"PyTorch built with cuDNN: {torch.backends.cudnn.version()}")
        
        # Check CUDA compilation flags
        print(f"CUDA available (before init): {torch.cuda.is_available()}")
        
        # Try to get more detailed error
        try:
            torch.cuda.init()
            print("✅ torch.cuda.init() successful")
        except Exception as e:
            print(f"❌ torch.cuda.init() failed: {e}")
        
        # Check device count with error handling
        try:
            device_count = torch.cuda.device_count()
            print(f"CUDA device count: {device_count}")
        except Exception as e:
            print(f"❌ Getting device count failed: {e}")
        
        # Check if we can import CUDA functions
        try:
            from torch.utils.cpp_extension import CUDA_HOME
            print(f"CUDA_HOME: {CUDA_HOME}")
        except:
            print("CUDA_HOME not accessible")
            
    except ImportError as e:
        print(f"❌ Cannot import PyTorch: {e}")
    
    print(f"\n🔧 POTENTIAL FIXES:")
    print("-" * 30)
    print("1. Driver compatibility issue:")
    print("   Your driver (535.230.02) supports CUDA 12.2")
    print("   PyTorch was compiled with CUDA 12.1")
    print("   This should be compatible, but may have issues")
    
    print("\n2. Try installing PyTorch with exact CUDA version:")
    print("   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118")
    
    print("\n3. Try clearing all CUDA cache:")
    print("   rm -rf ~/.cache/torch/")
    print("   rm -rf ~/.cache/huggingface/")
    
    print("\n4. Check for conflicting CUDA installations:")
    print("   sudo find / -name '*cuda*' -type f 2>/dev/null | grep -E '(libcuda|libnvidia)' | head -10")
    
    print("\n5. Try CPU-only mode temporarily:")
    print("   export CUDA_VISIBLE_DEVICES=''")
    
    # Environment variables
    print(f"\n🌍 ENVIRONMENT VARIABLES:")
    print("-" * 30)
    
    cuda_vars = ['CUDA_VISIBLE_DEVICES', 'CUDA_DEVICE_ORDER', 'CUDA_HOME', 'CUDA_PATH', 'LD_LIBRARY_PATH']
    for var in cuda_vars:
        value = os.environ.get(var, 'Not set')
        print(f"{var}: {value}")

if __name__ == "__main__":
    main() 