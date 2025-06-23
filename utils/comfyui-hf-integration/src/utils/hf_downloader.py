import os
from huggingface_hub import hf_hub_download

def download_model_file(repo_id, filename, target_directory, subfolder=None):
    """Download a specific file from a HuggingFace repository"""
    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)
    
    try:
        # Download the specific file
        model_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            cache_dir=None,  # Use default cache
            local_dir=target_directory,
            local_dir_use_symlinks=False,
            subfolder=subfolder
        )
        return model_path
    except Exception as e:
        print(f"Error downloading {filename} from {repo_id}: {str(e)}")
        return None

def download_model(model_name, target_directory):
    """Legacy function for backward compatibility"""
    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)

    # Download the model
    model_path = hf_hub_download(repo_id=model_name, repo_type="model", cache_dir=target_directory)
    return model_path

def download_models(models=None):
    """Download a list of models or use default FLUX.1-dev models"""
    if models is None:
        models = get_flux_models()
    
    for model in models:
        repo_id = model['repo_id']
        filename = model['filename']
        target_directory = model['target_directory']
        subfolder = model.get('subfolder', None)
        
        print(f"Downloading {filename} from {repo_id} to {target_directory}...")
        result = download_model_file(repo_id, filename, target_directory, subfolder)
        
        if result:
            print(f"✓ Downloaded {filename} successfully to {target_directory}")
        else:
            print(f"✗ Failed to download {filename}")

def get_flux_models():
    """Get the list of FLUX.1-dev models to download"""
    # Get the ComfyUI models directory (go up from current utils directory)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    models_dir = os.path.join(base_dir, "models")
    
    return [
        # Diffusion Model (FLUX.1-dev)
        {
            'repo_id': 'black-forest-labs/FLUX.1-dev',
            'filename': 'flux1-dev.safetensors',
            'target_directory': os.path.join(models_dir, 'diffusion_models'),
            'subfolder': None
        },
        # Text Encoders
        {
            'repo_id': 'comfyanonymous/flux_text_encoders',
            'filename': 'clip_l.safetensors',
            'target_directory': os.path.join(models_dir, 'text_encoders'),
            'subfolder': None
        },
        {
            'repo_id': 'comfyanonymous/flux_text_encoders',
            'filename': 't5xxl_fp16.safetensors',
            'target_directory': os.path.join(models_dir, 'text_encoders'),
            'subfolder': None
        },
        # Alternative T5 encoder (FP8 version - commented out, uncomment if you prefer this)
        # {
        #     'repo_id': 'comfyanonymous/flux_text_encoders',
        #     'filename': 't5xxl_fp8_e4m3fn_scaled.safetensors',
        #     'target_directory': os.path.join(models_dir, 'text_encoders'),
        #     'subfolder': None
        # },
        # VAE
        {
            'repo_id': 'Comfy-Org/Lumina_Image_2.0_Repackaged',
            'filename': 'ae.safetensors',
            'target_directory': os.path.join(models_dir, 'vae'),
            'subfolder': 'split_files/vae'
        }
    ]

def get_sd35_large_models():
    """Get the list of Stable Diffusion 3.5 Large models to download"""
    # Get the ComfyUI models directory (go up from current utils directory)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    models_dir = os.path.join(base_dir, "models")
    
    return [
        # Main Checkpoint (SD 3.5 Large)
        {
            'repo_id': 'stabilityai/stable-diffusion-3.5-large',
            'filename': 'sd3.5_large.safetensors',
            'target_directory': os.path.join(models_dir, 'checkpoints'),
            'subfolder': None
        },
        # Text Encoders for SD 3.5
        {
            'repo_id': 'stabilityai/stable-diffusion-3.5-large',
            'filename': 'clip_l.safetensors',
            'target_directory': os.path.join(models_dir, 'clip'),
            'subfolder': 'text_encoders'
        },
        {
            'repo_id': 'stabilityai/stable-diffusion-3.5-large',
            'filename': 'clip_g.safetensors',
            'target_directory': os.path.join(models_dir, 'clip'),
            'subfolder': 'text_encoders'
        },
        {
            'repo_id': 'stabilityai/stable-diffusion-3.5-large',
            'filename': 't5xxl_fp16.safetensors',
            'target_directory': os.path.join(models_dir, 'clip'),
            'subfolder': 'text_encoders'
        }
    ]

def get_sd35_turbo_models():
    """Get the list of Stable Diffusion 3.5 Turbo models to download"""
    # Get the ComfyUI models directory (go up from current utils directory)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    models_dir = os.path.join(base_dir, "models")
    
    return [
        # Main Checkpoint (SD 3.5 Turbo)
        {
            'repo_id': 'stabilityai/stable-diffusion-3.5-large-turbo',
            'filename': 'sd3.5_large_turbo.safetensors',
            'target_directory': os.path.join(models_dir, 'checkpoints'),
            'subfolder': None
        },
        # Text Encoders for SD 3.5 (same as large)
        {
            'repo_id': 'stabilityai/stable-diffusion-3.5-large',
            'filename': 'clip_l.safetensors',
            'target_directory': os.path.join(models_dir, 'clip'),
            'subfolder': 'text_encoders'
        },
        {
            'repo_id': 'stabilityai/stable-diffusion-3.5-large',
            'filename': 'clip_g.safetensors',
            'target_directory': os.path.join(models_dir, 'clip'),
            'subfolder': 'text_encoders'
        },
        {
            'repo_id': 'stabilityai/stable-diffusion-3.5-large',
            'filename': 't5xxl_fp16.safetensors',
            'target_directory': os.path.join(models_dir, 'clip'),
            'subfolder': 'text_encoders'
        }
    ]

def get_available_model_sets():
    """Get all available model sets"""
    return {
        'flux': {
            'name': 'FLUX.1-dev',
            'description': 'High-quality text-to-image generation with excellent prompt adherence',
            'models': get_flux_models(),
            'license_url': 'https://huggingface.co/black-forest-labs/FLUX.1-dev',
            'requirements': '12GB+ VRAM recommended'
        },
        'sd35_large': {
            'name': 'Stable Diffusion 3.5 Large',
            'description': 'Latest SD model with improved performance and image quality',
            'models': get_sd35_large_models(),
            'license_url': 'https://huggingface.co/stabilityai/stable-diffusion-3.5-large',
            'requirements': '12GB+ VRAM recommended'
        },
        'sd35_turbo': {
            'name': 'Stable Diffusion 3.5 Turbo',
            'description': 'Fast variant requiring only 4 sampling steps',
            'models': get_sd35_turbo_models(),
            'license_url': 'https://huggingface.co/stabilityai/stable-diffusion-3.5-large-turbo',
            'requirements': '8GB+ VRAM recommended'
        }
    }