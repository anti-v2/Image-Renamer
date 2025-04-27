<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Auto Rename Images by AI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2, h3 {
            color: #222;
        }
        code {
            background: #eee;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
        }
        pre {
            background: #eee;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        .container {
            max-width: 1000px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        ul {
            padding-left: 20px;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>🖼️ Auto Rename Images by AI (Image Captioning)</h1>

    <p>This small Python script automatically renames your bulk-downloaded images by <strong>looking at the image and generating a smart caption</strong> using AI! 
    No more opening each image manually. Just run the script and get meaningful names like <code>sunset_beach.jpg</code> or <code>mountain_view.png</code> instead of random codes.</p>

    <h2>✨ Features</h2>
    <ul>
        <li>AI-powered automatic caption generation</li>
        <li>Supports <code>.jpg</code>, <code>.jpeg</code>, <code>.png</code>, <code>.webp</code> images</li>
        <li>Renames files with safe names (spaces replaced by underscores)</li>
        <li>Easy and quick to use</li>
        <li>Hugging Face API based (free to use)</li>
    </ul>

    <h2>📋 Requirements</h2>
    <ul>
        <li>Python 3.10+</li>
        <li>pip (Python package manager)</li>
    </ul>

    <p>Install required Python libraries:</p>
    <pre><code>pip install pillow requests</code></pre>

    <h2>🧠 How it Works</h2>
    <ol>
        <li>Script sends your image to an AI model hosted at <a href="https://huggingface.co/" target="_blank">HuggingFace</a>.</li>
        <li>The model analyzes the image and returns a short description (caption).</li>
        <li>The script renames your file based on the generated caption.</li>
    </ol>

    <h2>🔑 Setup Hugging Face API Key</h2>
    <ol>
        <li>Create a free account at <a href="https://huggingface.co/join" target="_blank">Hugging Face Join</a>.</li>
        <li>After signup, go to <a href="https://huggingface.co/settings/tokens" target="_blank">Settings → Access Tokens</a>.</li>
        <li>Click <strong>"New Token"</strong>, name it anything (e.g., <em>image-rename</em>), and set <strong>Role: Read</strong>.</li>
        <li>Copy the generated API key (starts with <code>hf_...</code>).</li>
    </ol>

    <h2>🛠️ How to Use</h2>
    <ol>
        <li>Clone or download this repository.</li>
        <li>Open a terminal and install dependencies:
            <pre><code>pip install pillow requests</code></pre>
        </li>
        <li>Edit the script file and replace:
            <pre><code>headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY_HERE"}</code></pre>
            with your actual Hugging Face API key.
        </li>
        <li>Run the script:
            <pre><code>python rename_images.py</code></pre>
        </li>
        <li>Enter the path to the folder containing your images.</li>
        <li>Done! Your files will be automatically renamed.</li>
    </ol>

    <h2>📂 Project Structure</h2>
    <pre><code>/your-project-folder
├── README.md
└── rename_images.py
</code></pre>

    <h2>⚡ Example</h2>
    <p><strong>Before:</strong></p>
    <pre><code>08dam2zm.jpg
hs04cqcu.png
qbob4gk7.jpg
yzqg8dn9.png
</code></pre>

    <p><strong>After running the script:</strong></p>
    <pre><code>sunset_at_beach.jpg
majestic_mountains.png
forest_in_morning_light.jpg
cityscape_night_view.png
</code></pre>

    <h2>❗ Notes</h2>
    <ul>
        <li>Each image is processed one by one (may take a few seconds per image depending on your internet).</li>
        <li>API rate limits might apply if you use hundreds of images at once on free Hugging Face accounts.</li>
        <li>Always keep a backup of original files, just in case.</li>
    </ul>

    <h2>📜 License</h2>
    <p>This project is free to use under the MIT License.</p>

    <hr>
    <p style="text-align:center;">Made with ❤️ by Shirahoshi 🚀</p>
</div>
</body>
</html>
