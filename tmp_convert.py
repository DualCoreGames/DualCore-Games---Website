from PIL import Image
import sys

def convert_to_webp(input_path, output_path):
    print(f"Converting {input_path} to {output_path}...")
    try:
        img = Image.open(input_path)
        img.save(output_path, "WEBP", quality=85, method=6)
        print("Success!")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    convert_to_webp("assets/images/Reclairoshomepagesection.png", "assets/images/reclairos-homepage-section.webp")
