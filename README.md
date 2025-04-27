
# 🖼️ Auto Rename Images by AI (Image Captioning)

This small Python script automatically renames your bulk-downloaded images by **looking at the image and generating a smart caption** using AI!  
No more opening each image manually. Just run the script and get meaningful names like `sunset_beach.jpg` or `mountain_view.png` instead of random codes.

---

## ✨ Features

- AI-powered automatic caption generation
- Supports `.jpg`, `.jpeg`, `.png`, `.webp` images
- Renames files with safe names (spaces replaced by underscores)
- Easy and quick to use
- Hugging Face API based (free to use)

---

### 📋 Requirements

- Python 3.10+
- pip (Python package manager)

Install required Python libraries:

``` bash 
pip install pillow requests
```

# 🔑 Setup Hugging Face API Key

  -  Create a free account at Hugging Face Join.
  -  After signup, go to Settings → Access Tokens.
   - Click "New Token", name it anything (e.g., image-rename), and set Role: Read.

    Copy the generated API key (starts with hf_...).


#🛠️ How to Use

    Clone or download this repository.

    Open a terminal and install dependencies:
```bash`
pip install pillow requests
```

Edit the script file and replace:

headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY_HERE"}

