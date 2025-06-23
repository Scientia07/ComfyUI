# 🚀 Quick Start Guide

## Your First ComfyUI Workflow

### ⚡ **Fastest Start (30 seconds)**

1. **Import Workflow**: Drag `basic/txt2img/sd35_basic_1024.json` into ComfyUI
2. **Click Queue Prompt**: The workflow is pre-configured with your models
3. **Generate**: Watch your first AI image being created!

### 🎯 **Recommended First Workflows**

#### **1. SD 3.5 Basic** (`basic/txt2img/sd35_basic_1024.json`)
- ✅ **Ready to use** with your current models
- ✅ **Beginner friendly** - just change the prompt
- ✅ **Fast generation** - 30-60 seconds
- 🎯 **Perfect for**: Learning ComfyUI basics

#### **2. Flux Advanced** (`basic/txt2img/flux_basic_1024.json`)  
- ✅ **Superior quality** with Flux.1 Dev
- ✅ **Advanced prompting** with dual CLIP encoders
- ✅ **Your existing models** - fully compatible
- 🎯 **Perfect for**: High-quality generation

#### **3. Fast Template** (`templates/base_templates/fast_generation.json`)
- ✅ **15-30 second** generation
- ✅ **Low memory** usage (6-8GB)
- ✅ **Customizable** template
- 🎯 **Perfect for**: Quick testing and iteration

## 📋 **Step-by-Step First Generation**

### Step 1: Choose Your Workflow
```
✨ Recommended: basic/txt2img/sd35_basic_1024.json
```

### Step 2: Import to ComfyUI
```
Method 1: Drag & drop the .json file into ComfyUI interface
Method 2: Click "Load" button → Browse → Select workflow
```

### Step 3: Customize (Optional)
```
• Change prompt: "a beautiful landscape..." → "your custom prompt"
• Adjust settings: Steps (20), CFG (7.0), Resolution (1024x1024)
• Modify seed: For reproducible results
```

### Step 4: Generate
```
Click "Queue Prompt" button → Wait → Enjoy your image!
```

## 🎨 **Your Current Setup**

Based on your models, you can immediately use:

| Workflow | Model Used | Generation Time | Quality |
|----------|------------|----------------|---------|
| **SD 3.5 Basic** | sd3.5_large.safetensors | 30-60s | Excellent |
| **Flux Basic** | flux1-dev-fp8.safetensors | 45-90s | Superior |
| **Fast Template** | Any checkpoint | 15-30s | Good |
| **Realistic Portrait** | sd3.5_large.safetensors | 60-120s | Professional |

## 🔧 **Customization Tips**

### **Prompts:**
```
Good: "a beautiful landscape, detailed, 4k"
Better: "a majestic mountain landscape at sunset, highly detailed, photorealistic, 4k"
```

### **Quality vs Speed:**
```
Fast: 12 steps, CFG 5, DPM++ 2M
Balanced: 20 steps, CFG 7, Euler  
Quality: 30 steps, CFG 8.5, DPM++ 2M Karras
```

### **Resolution:**
```
Fast: 512x512
Standard: 1024x1024  
High-res: 1536x1536 (requires more VRAM)
```

## 🆘 **Troubleshooting**

### **Common Issues:**

❌ **"Model not found"**  
✅ Check that model filename in workflow matches your actual file

❌ **"Out of memory"**  
✅ Try `templates/base_templates/fast_generation.json` (lower memory)

❌ **"Slow generation"**  
✅ Reduce steps to 12-15 or use smaller resolution

❌ **"Poor quality"**  
✅ Increase steps to 25-30 and CFG to 8-9

## 📁 **Folder Overview**

```
workflows/
├── 📂 basic/           ← Start here!
├── 📂 advanced/        ← Later exploration
├── 📂 examples/        ← Ready-made styles  
└── 📂 templates/       ← Customizable bases
```

## 🎯 **Next Steps**

1. **Master the basics** with SD 3.5 workflow
2. **Experiment with prompts** to see different results
3. **Try Flux workflow** for advanced generation
4. **Explore examples/** for specific styles
5. **Customize templates/** for your needs

## 💡 **Pro Tips**

- **Save successful prompts** for future use
- **Use consistent seeds** for comparing different settings
- **Start with lower steps** for faster iteration
- **Monitor VRAM usage** to optimize performance
- **Keep notes** of what settings work best for you

---

**🎉 Ready to create amazing AI art? Start with `basic/txt2img/sd35_basic_1024.json` and let your creativity flow!** 