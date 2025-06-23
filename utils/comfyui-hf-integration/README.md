# To activate the venv

source comfy-env/bin/activate 

# ComfyUI Hugging Face Integration

This project integrates ComfyUI with the Hugging Face Hub, allowing users to easily download and manage models from the Hugging Face repository.

## Project Structure

```
comfyui-hf-integration
├── src
│   ├── index.py
│   └── utils
│       └── hf_downloader.py
├── requirements.txt
└── README.md
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd comfyui-hf-integration
pip install -r requirements.txt
```

## Usage

To download models from the Hugging Face Hub, run the following command:

```bash
python src/index.py
```

This will execute the model download process defined in `index.py`, which utilizes the downloader utility in `hf_downloader.py`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

