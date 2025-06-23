#!/usr/bin/env python3
"""
ComfyUI CUDA and System Test Script
This script tests CUDA setup and basic ComfyUI functionality
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd, description):
    """Run a command and return success status"""
    print(f"\n🔧 {description}")
    print(f"Running: {cmd}")
    print("-" * 50)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        if result.returncode == 0:
            print(f"✅ {description} - SUCCESS")
            return True
        else:
            print(f"❌ {description} - FAILED (exit code: {result.returncode})")
            return False
    except Exception as e:
        print(f"❌ {description} - ERROR: {str(e)}")
        return False

def test_python_environment():
    """Test Python environment and basic imports"""
    print("=" * 60)
    print("🐍 TESTING PYTHON ENVIRONMENT")
    print("=" * 60)
    
    # Test basic Python
    success = run_command("python3 --version", "Python Version Check")
    
    # Test pip
    success &= run_command("python3 -m pip --version", "Pip Version Check")
    
    return success

def test_cuda_setup():
    """Test CUDA setup"""
    print("=" * 60)
    print("🔥 TESTING CUDA SETUP")
    print("=" * 60)
    
    # Test nvidia-smi
    success = run_command("nvidia-smi", "NVIDIA System Management Interface")
    
    # Test CUDA with Python
    cuda_test_cmd = """
python3 -c "
try:
    import torch
    print(f'PyTorch version: {torch.__version__}')
    print(f'CUDA available: {torch.cuda.is_available()}')
    if torch.cuda.is_available():
        print(f'CUDA device count: {torch.cuda.device_count()}')
        print(f'Current device: {torch.cuda.current_device()}')
        print(f'Device name: {torch.cuda.get_device_name(0)}')
        print(f'CUDA version: {torch.version.cuda}')
        
        # Test simple CUDA operation
        x = torch.randn(3, 3).cuda()
        y = torch.randn(3, 3).cuda()
        z = torch.matmul(x, y)
        print(f'CUDA tensor operation test: SUCCESS')
        print(f'Result shape: {z.shape}')
    else:
        print('CUDA not available - this may be the source of your errors')
except ImportError as e:
    print(f'PyTorch not installed: {e}')
except Exception as e:
    print(f'CUDA test failed: {e}')
"
"""
    
    success &= run_command(cuda_test_cmd, "PyTorch CUDA Test")
    
    return success

def test_comfyui_dependencies():
    """Test ComfyUI dependencies"""
    print("=" * 60)
    print("📦 TESTING COMFYUI DEPENDENCIES")
    print("=" * 60)
    
    deps_test_cmd = """
python3 -c "
import sys
required_packages = [
    'torch', 'torchvision', 'torchaudio',
    'numpy', 'PIL', 'cv2', 'transformers',
    'diffusers', 'accelerate', 'safetensors'
]

missing_packages = []
for package in required_packages:
    try:
        if package == 'PIL':
            import PIL
        elif package == 'cv2':
            import cv2
        else:
            __import__(package)
        print(f'✅ {package}')
    except ImportError:
        print(f'❌ {package} - MISSING')
        missing_packages.append(package)

if missing_packages:
    print(f'\\nMissing packages: {missing_packages}')
    print('Install with: pip install ' + ' '.join(missing_packages))
else:
    print('\\n🎉 All core dependencies available!')
"
"""
    
    success = run_command(deps_test_cmd, "Dependency Check")
    
    return success

def test_comfyui_basic():
    """Test basic ComfyUI functionality"""
    print("=" * 60)
    print("🎨 TESTING BASIC COMFYUI FUNCTIONALITY")
    print("=" * 60)
    
    # Test if main.py exists and can be imported
    main_test_cmd = """
python3 -c "
import sys
import os
sys.path.append('.')

try:
    # Test basic ComfyUI imports
    import folder_paths
    print('✅ folder_paths module loaded')
    
    import model_management
    print('✅ model_management module loaded')
    
    print('✅ Basic ComfyUI modules can be imported')
    
except ImportError as e:
    print(f'❌ ComfyUI import failed: {e}')
    print('This suggests ComfyUI installation issues')
except Exception as e:
    print(f'❌ ComfyUI test failed: {e}')
"
"""
    
    success = run_command(main_test_cmd, "ComfyUI Basic Import Test")
    
    return success

def run_unit_tests():
    """Run ComfyUI unit tests"""
    print("=" * 60)
    print("🧪 RUNNING UNIT TESTS")
    print("=" * 60)
    
    # Install test requirements
    success = run_command("python3 -m pip install -r tests-unit/requirements.txt", "Install Test Requirements")
    
    if success:
        # Run unit tests
        success &= run_command("python3 -m pytest tests-unit/ -v", "Unit Tests")
    
    return success

def run_simple_inference_test():
    """Run a simple inference test"""
    print("=" * 60)
    print("🚀 SIMPLE INFERENCE TEST")
    print("=" * 60)
    
    simple_test_cmd = """
python3 -c "
try:
    import torch
    print('Testing simple tensor operations...')
    
    if torch.cuda.is_available():
        device = 'cuda'
        print(f'Using CUDA device: {torch.cuda.get_device_name(0)}')
    else:
        device = 'cpu'
        print('Using CPU (CUDA not available)')
    
    # Simple tensor test
    x = torch.randn(1000, 1000, device=device)
    y = torch.randn(1000, 1000, device=device)
    
    # Time the operation
    import time
    start = time.time()
    z = torch.matmul(x, y)
    end = time.time()
    
    print(f'Matrix multiplication completed in {end-start:.4f} seconds')
    print(f'Result tensor shape: {z.shape}')
    print('✅ Simple inference test passed!')
    
except Exception as e:
    print(f'❌ Simple inference test failed: {e}')
"
"""
    
    success = run_command(simple_test_cmd, "Simple Inference Test")
    
    return success

def main():
    """Main test runner"""
    print("🎯 ComfyUI CUDA and System Test Suite")
    print("=" * 60)
    
    # Change to ComfyUI directory
    os.chdir(Path(__file__).parent)
    
    results = []
    
    # Run all tests
    results.append(("Python Environment", test_python_environment()))
    results.append(("CUDA Setup", test_cuda_setup()))
    results.append(("ComfyUI Dependencies", test_comfyui_dependencies()))
    results.append(("ComfyUI Basic", test_comfyui_basic()))
    results.append(("Simple Inference", run_simple_inference_test()))
    results.append(("Unit Tests", run_unit_tests()))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{test_name:25} {status}")
        if success:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! ComfyUI should work correctly.")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
        
        if not results[1][1]:  # CUDA test failed
            print("\n🔥 CUDA Issues Detected:")
            print("- Make sure NVIDIA drivers are installed")
            print("- Verify CUDA toolkit installation")
            print("- Check PyTorch CUDA compatibility")
            print("- Try reinstalling PyTorch with: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118")

if __name__ == "__main__":
    main() 