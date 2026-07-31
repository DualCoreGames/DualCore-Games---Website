from PIL import Image
import os

images = {
    "mohsin": "/Users/abhinav/.gemini/antigravity/brain/3318ae8c-b58f-471f-af74-9d9ec34edac3/mohsin_uniform_1785459068968.jpg",
    "ayush": "/Users/abhinav/.gemini/antigravity/brain/3318ae8c-b58f-471f-af74-9d9ec34edac3/ayush_uniform_1785459078390.jpg",
    "abhinav": "/Users/abhinav/.gemini/antigravity/brain/3318ae8c-b58f-471f-af74-9d9ec34edac3/abhinav_uniform_1785459087124.jpg",
    "rohit": "/Users/abhinav/.gemini/antigravity/brain/3318ae8c-b58f-471f-af74-9d9ec34edac3/rohit_uniform_1785459096351.jpg"
}

output_dir = "/Users/abhinav/Development/DualCoreWebsite/DualCore Games — Website/assets/images/team"

for name, path in images.items():
    try:
        if os.path.exists(path):
            img = Image.open(path)
            output_path = os.path.join(output_dir, f"{name}.webp")
            img.save(output_path, "WEBP", quality=90)
            print(f"Saved {name}.webp")
        else:
            print(f"File not found: {path}")
    except Exception as e:
        print(f"Error processing {name}: {e}")
