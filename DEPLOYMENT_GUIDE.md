# 🚀 ComfyUI Enhanced Setup - Deployment Guide

This repository contains a fully enhanced ComfyUI setup that's ready to deploy on any new device. Everything you need is included except the AI models (which are downloaded automatically).

## 🎯 Quick Start (3 Steps)

### 1. Clone and Setup
```bash
git clone https://github.com/Scientia07/ComfyUI.git
cd ComfyUI
```

### 2. Install Dependencies
```bash
# Create Python environment
python -m venv comfy-env
source comfy-env/bin/activate  # Linux/Mac
# OR
comfy-env\Scripts\activate     # Windows

# Install requirements
pip install -r requirements.txt
```

### 3. Download Models & Launch
```bash
# Download your first models (interactive menu)
python utils/comfyui-hf-integration/src/index.py

# Launch ComfyUI (one command!)
./launch_comfyui.sh    # Linux/Mac
# OR manually: python main.py
```

That's it! 🎉 ComfyUI will be running at `http://localhost:8188`

## 🛠️ What's Included

### ⚡ Auto-Setup Tools
- **`launch_comfyui.sh`** - One-click launcher with environment setup
- **CUDA diagnostic tools** - Auto-detect and fix CUDA issues
- **Environment isolation** - Clean Python path management

### 🤖 Enhanced Model Management
- **Interactive model downloader** - Choose from FLUX, SD3.5, etc.
- **Automatic organization** - Models placed in correct directories
- **Progress tracking** - See download progress and validation

### 📋 Ready-to-Use Workflows
- **Basic workflows** - FLUX and SD3.5 text-to-image
- **SDXL templates** - Advanced workflow collection
- **Portrait examples** - Realistic portrait generation
- **Fast generation** - Optimized quick workflows

### 🔧 Troubleshooting Tools
- **`diagnose_cuda.py`** - Check CUDA installation
- **`fix_cuda.sh`** - Auto-fix common CUDA issues
- **`update_nvidia_driver.sh`** - Update drivers if needed

## 💡 Pro Tips

### First Time Setup
1. Run the CUDA diagnostic first: `python diagnose_cuda.py`
2. If issues found, run: `./fix_cuda.sh`
3. Download a lightweight model first (SDXL Turbo recommended)

### Model Recommendations
- **For speed**: SD3.5 Large Turbo (~8GB)
- **For quality**: FLUX.1-dev (~22GB)
- **For mobile**: SDXL Turbo (~7GB)

### Common Issues
- **CUDA not found**: Run `./fix_cuda.sh`
- **Out of memory**: Use `--lowvram` or `--cpu` flags
- **Slow generation**: Check GPU memory with `nvidia-smi`

## 🎨 Getting Started with Generation

1. Open `http://localhost:8188`
2. Load a workflow from `workflows/basic/txt2img/`
3. Enter your prompt
4. Click "Queue Prompt"
5. Watch the magic happen! ✨

## 📁 Directory Structure
```
ComfyUI/
├── launch_comfyui.sh          # 🚀 One-click launcher
├── utils/comfyui-hf-integration/  # 🤖 Model downloader
├── workflows/                 # 📋 Ready-to-use workflows
├── fix_cuda.sh               # 🔧 CUDA troubleshooting
├── diagnose_cuda.py          # 🔍 System diagnostics
└── models/                   # 📦 Downloaded models go here
```

## 🤝 Need Help?

- **CUDA Issues**: Run `python diagnose_cuda.py`
- **Model Problems**: Check `utils/comfyui-hf-integration/README.md`
- **Workflow Help**: See `workflows/README.md`
- **General Issues**: Check the main [ComfyUI Documentation](https://docs.comfy.org/)

---

**Ready to create amazing AI art? Let's go! 🎨✨** 