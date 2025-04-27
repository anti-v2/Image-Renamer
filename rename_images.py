import os
import requests

# Hugging Face settings
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": "Bearer YOUR API HUGGINS KEY"}  # <--- paste your API key here

def get_image_caption(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    if response.status_code == 200:
        try:
            return response.json()[0]['generated_text']
        except (KeyError, IndexError):
            print("Failed to get caption for", image_path)
            return None
    else:
        print(f"Error {response.status_code} for {image_path}")
        return None

def rename_images(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            file_path = os.path.join(folder_path, filename)
            caption = get_image_caption(file_path)
            if caption:
                safe_caption = caption.replace(" ", "_").replace("/", "_")
                new_filename = safe_caption[:50] + os.path.splitext(filename)[1]
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed {filename} -> {new_filename}")

if __name__ == "__main__":
    folder = input("Enter the path to your images folder: ")
    rename_images(folder)

