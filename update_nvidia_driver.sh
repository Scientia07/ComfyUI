#!/bin/bash

echo "🚀 NVIDIA Driver Update Script"
echo "=============================="
echo "Current driver: 535.230.02"
echo "Target driver:  570 (recommended)"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "❌ This script needs to be run with sudo"
    echo "Please run: sudo ./update_nvidia_driver.sh"
    exit 1
fi

echo "⚠️  WARNING: This will update your NVIDIA driver"
echo "⚠️  Your desktop may restart during this process"
echo ""
read -p "Do you want to continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Update cancelled."
    exit 1
fi

echo ""
echo "🔄 Starting driver update process..."

# Update package lists
echo "📦 Updating package lists..."
apt update

# Remove old driver cleanly
echo "🗑️ Removing old NVIDIA driver..."
apt purge -y nvidia-driver-535* nvidia-dkms-535*

# Clean any remaining NVIDIA packages
echo "🧹 Cleaning NVIDIA packages..."
apt autoremove -y
apt autoclean

# Install new driver (recommended version)
echo "⬇️ Installing NVIDIA driver 570..."
apt install -y nvidia-driver-570

# Install additional NVIDIA utilities if needed
echo "🔧 Installing NVIDIA utilities..."
apt install -y nvidia-settings nvidia-prime

echo ""
echo "✅ Driver installation completed!"
echo ""
echo "🔄 A reboot is required to activate the new driver."
echo ""
read -p "Do you want to reboot now? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🔄 Rebooting in 5 seconds..."
    echo "After reboot, test CUDA with: nvidia-smi"
    sleep 5
    reboot
else
    echo "📋 Manual reboot required later with: sudo reboot"
    echo "🧪 After reboot, test the installation with:"
    echo "   nvidia-smi"
    echo "   cd /home/joel/dev/AI/ComfyUI"
    echo "   PYTHONPATH=/home/joel/dev/AI/ComfyUI/comfy-env/lib/python3.12/site-packages python3 test_cuda_setup.py"
fi

echo ""
echo "🎉 NVIDIA driver update process completed!" 