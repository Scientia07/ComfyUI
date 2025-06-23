import os
from utils.hf_downloader import download_models, get_available_model_sets

def show_banner():
    """Display the application banner"""
    print("=" * 70)
    print("🎨 ComfyUI Model Downloader 🎨")
    print("=" * 70)
    print("Download popular AI models for ComfyUI with ease!")
    print()

def show_model_details(model_set_key, model_set):
    """Display detailed information about a model set"""
    print(f"\n📋 {model_set['name']} Details:")
    print("─" * 50)
    print(f"Description: {model_set['description']}")
    print(f"Requirements: {model_set['requirements']}")
    print(f"License: {model_set['license_url']}")
    print()
    
    print("📁 Files to be downloaded:")
    for i, model in enumerate(model_set['models'], 1):
        print(f"  {i}. {model['filename']}")
        print(f"     └─ {model['repo_id']}")
        print(f"     └─ Target: {os.path.basename(model['target_directory'])}/")
        if model.get('subfolder'):
            print(f"     └─ Subfolder: {model['subfolder']}")
        print()

def show_menu():
    """Display the main menu and handle user selection"""
    model_sets = get_available_model_sets()
    
    while True:
        show_banner()
        
        print("🚀 Available Model Sets:")
        print()
        
        menu_items = list(model_sets.items())
        for i, (key, model_set) in enumerate(menu_items, 1):
            print(f"  {i}. {model_set['name']}")
            print(f"     {model_set['description']}")
            print(f"     {model_set['requirements']}")
            print()
        
        print("  0. Exit")
        print()
        
        try:
            choice = input("Select a model set to download (0-{}): ".format(len(menu_items))).strip()
            
            if choice == '0':
                print("👋 Goodbye!")
                break
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(menu_items):
                selected_key, selected_set = menu_items[choice_num - 1]
                handle_model_selection(selected_key, selected_set)
            else:
                print("❌ Invalid choice. Please try again.")
                input("Press Enter to continue...")
                
        except ValueError:
            print("❌ Please enter a valid number.")
            input("Press Enter to continue...")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break

def handle_model_selection(model_key, model_set):
    """Handle the selected model set download process"""
    while True:
        print("\n" + "=" * 70)
        show_model_details(model_key, model_set)
        
        print("⚠️  IMPORTANT:")
        print("Before downloading, you MUST accept the license agreement at:")
        print(f"👉 {model_set['license_url']}")
        print()
        print("For Stable Diffusion models, you need to:")
        print("1. Visit the model page on HuggingFace")
        print("2. Sign in to your HuggingFace account") 
        print("3. Accept the license agreement")
        print("4. Make sure you're logged in locally with: huggingface-cli login")
        print()
        
        print("What would you like to do?")
        print("1. Download these models")
        print("2. View file details again")
        print("3. Back to main menu")
        
        sub_choice = input("Enter your choice (1-3): ").strip()
        
        if sub_choice == '1':
            confirm_and_download(model_set)
            break
        elif sub_choice == '2':
            continue
        elif sub_choice == '3':
            break
        else:
            print("❌ Invalid choice.")
            input("Press Enter to continue...")

def confirm_and_download(model_set):
    """Confirm license acceptance and start download"""
    print("\n🔐 License Confirmation")
    print("─" * 30)
    
    response = input("Have you accepted the license agreement? (y/N): ").strip().lower()
    
    if response not in ['y', 'yes']:
        print("❌ You must accept the license agreement before downloading.")
        print("Please visit the model page and accept the agreement first.")
        input("Press Enter to continue...")
        return
    
    print("\n🚀 Starting download process...")
    print("This may take a while depending on your internet connection.")
    print("The models are large files (several GB each).")
    print()
    
    try:
        download_models(model_set['models'])
        
        print("\n" + "=" * 50)
        print("✅ All models downloaded successfully!")
        print("=" * 50)
        
        # Show the expected directory structure
        show_directory_structure(model_set['models'])
        
        print("🎉 You can now use these models in ComfyUI!")
        print("Restart ComfyUI if it's currently running to see the new models.")
        
    except Exception as e:
        print(f"\n❌ Error during download: {str(e)}")
        print()
        print("Common solutions:")
        print("1. Check your internet connection")
        print("2. Login to HuggingFace: huggingface-cli login")
        print("3. Make sure you accepted the license agreement")
        print("4. Try running the script again")
    
    input("\nPress Enter to return to main menu...")

def show_directory_structure(models):
    """Show the expected directory structure after download"""
    print("\n📁 Your ComfyUI models directory structure:")
    
    # Group models by target directory
    dir_groups = {}
    for model in models:
        target_dir = os.path.basename(model['target_directory'])
        if target_dir not in dir_groups:
            dir_groups[target_dir] = []
        dir_groups[target_dir].append(model['filename'])
    
    print("ComfyUI/models/")
    for dir_name, files in dir_groups.items():
        print(f"├── {dir_name}/")
        for i, filename in enumerate(files):
            prefix = "└──" if i == len(files) - 1 else "├──"
            print(f"│   {prefix} {filename}")

def main():
    """Main entry point"""
    try:
        show_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Download cancelled by user.")

if __name__ == "__main__":
    main()