# ComfyUI Workflows Collection

This directory contains a curated collection of ComfyUI workflows organized by complexity and use case.

## 📁 **Folder Structure**

```
workflows/
├── README.md                    # This guide
├── basic/                       # Simple, beginner-friendly workflows
│   ├── txt2img/                # Basic text-to-image generation
│   ├── img2img/                # Image-to-image transformation
│   └── inpainting/             # Basic inpainting workflows
├── advanced/                    # Complex, multi-step workflows
│   ├── controlnet/             # ControlNet-based workflows
│   ├── lora_combinations/      # Multiple LoRA workflows
│   ├── upscaling/              # High-resolution workflows
│   └── animation/              # Video/animation workflows
├── examples/                    # Ready-to-use example workflows
│   ├── portraits/              # Portrait generation examples
│   ├── landscapes/             # Landscape generation examples
│   ├── artistic_styles/        # Various artistic style examples
│   └── product_shots/          # Product photography examples
└── templates/                   # Workflow templates for customization
    ├── base_templates/         # Foundation templates
    ├── model_specific/         # Templates for specific models
    └── custom_nodes/           # Templates using custom nodes
```

## 🎯 **How to Use**

### **For Beginners:**
Start with `basic/` workflows - these are simple, well-documented, and use standard models.

### **For Advanced Users:**
Explore `advanced/` workflows for complex multi-step processes and specialized techniques.

### **For Quick Testing:**
Use `examples/` for ready-made workflows that demonstrate specific styles or subjects.

### **For Customization:**
Copy from `templates/` and modify for your specific needs.

## 🔧 **Import Instructions**

1. **Drag & Drop**: Drag any `.json` file into ComfyUI interface
2. **Load Button**: Use ComfyUI's "Load" button to browse and select workflows
3. **API Usage**: Use workflow files with ComfyUI API for automation

## 📝 **Workflow Naming Convention**

```
[model]_[type]_[resolution]_[special].json

Examples:
- sd35_txt2img_1024_basic.json
- flux_portrait_1024_detailed.json
- sdxl_landscape_2048_upscaled.json
```

## 🎨 **Model Compatibility**

Each workflow is tagged with compatible models:
- **SD 3.5**: `sd35_*.json`
- **Flux**: `flux_*.json` 
- **SDXL**: `sdxl_*.json`
- **Universal**: `universal_*.json` (works with multiple models)

## 🏷️ **Workflow Tags**

Workflows are tagged for easy filtering:
- `#beginner` - Simple, well-documented
- `#advanced` - Complex, multi-step
- `#portrait` - Portrait generation
- `#landscape` - Landscape/nature scenes
- `#artistic` - Artistic styles
- `#controlnet` - Uses ControlNet
- `#lora` - Uses LoRA models
- `#upscale` - High-resolution output
- `#fast` - Quick generation (<30 steps)
- `#quality` - High-quality output (>30 steps)

## 📊 **Workflow Statistics**

Each workflow includes metadata:
```json
{
  "metadata": {
    "name": "Basic Text-to-Image",
    "description": "Simple text-to-image generation",
    "author": "ComfyUI Collection",
    "tags": ["beginner", "txt2img", "basic"],
    "models_required": ["checkpoint", "vae"],
    "estimated_time": "30-60 seconds",
    "memory_usage": "8GB VRAM",
    "difficulty": "beginner"
  }
}
```

## 🚀 **Quick Start Workflows**

### Most Popular:
- `basic/txt2img/sd35_basic_1024.json` - SD 3.5 basic generation
- `basic/txt2img/flux_basic_1024.json` - Flux basic generation
- `examples/portraits/realistic_portrait.json` - Realistic portraits
- `examples/landscapes/nature_scenes.json` - Nature landscapes

### Performance Optimized:
- `templates/base_templates/fast_generation.json` - Speed optimized
- `templates/base_templates/quality_generation.json` - Quality optimized
- `templates/base_templates/balanced_generation.json` - Balanced speed/quality

## 🔄 **Workflow Updates**

Workflows are versioned and updated regularly:
- **v1.0**: Initial release
- **v1.1**: Bug fixes and optimizations
- **v2.0**: Major feature additions

Check the `version` field in each workflow file for the current version.

## 💡 **Contributing**

To add your own workflows:
1. Follow the naming convention
2. Include proper metadata
3. Test with the target models
4. Document any special requirements
5. Add appropriate tags

## ⚠️ **Requirements**

### Minimum:
- ComfyUI installed
- At least one checkpoint model
- 8GB VRAM (for basic workflows)

### Recommended:
- 12GB+ VRAM
- Text encoders (CLIP, T5)
- VAE model
- Various LoRAs and ControlNets

## 🆘 **Troubleshooting**

### Common Issues:
- **Missing models**: Check model requirements in workflow metadata
- **Memory errors**: Try workflows tagged with `#low_memory`
- **Slow generation**: Use workflows tagged with `#fast`
- **Poor quality**: Ensure proper model compatibility

### Getting Help:
- Check workflow documentation
- Review model requirements
- Test with simpler workflows first
- Check ComfyUI console for errors

---

*This workflow collection is designed to help users of all skill levels create amazing AI-generated content with ComfyUI.* 