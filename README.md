
# 🖼️ Auto Rename Images by AI 

This small Python script automatically renames your bulk-downloaded images by **looking at the image and generating a smart caption** using AI!  
No more opening each image manually. Just run the script and get meaningful names like `sunset_beach.jpg` or `mountain_view.png` instead of random codes.
Its more like an API that opens the wallpaper and see the image (The AI) and then sends and rename wallpaper.

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

 ```
pip install pillow requests
```
---

### 🔑 Setup Hugging Face API Key

  -  Create a free account at Hugging Face Join.
  -  After signup, go to Settings → Access Tokens.
   - Click "New Token", name it anything (e.g., image-rename), and set Role: Read.
  - Copy the generated API key (starts with hf_...).

---

### 🛠️ How to Use
  - Clone the repository
  ```
git clone https://github.com/anti-v2/Image-Renamer.git
cd Image-Renamer
```
- Create virtual env Linux:
```
python -m venv wallRename
pip install pillow requests
```
---

#### Edit the script file (rename_images.py) and replace:
```
headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY_HERE"}
```
-with your actual Hugging Face API key. eg hf_
#### Run the script:
```
python rename_images.py
```
---
### Images
![image](https://github.com/user-attachments/assets/bb40dfac-230c-4638-88bd-74e38dc088b7)
![image](https://github.com/user-attachments/assets/bb40dfac-230c-4638-88bd-74e38dc088b7)
![image](https://github.com/user-attachments/assets/bb40dfac-230c-4638-88bd-74e38dc088b7)

---





