from PIL import Image
import os

os.makedirs("assets/images/team", exist_ok=True)

img_path = "/Users/abhinav/.gemini/antigravity/brain/3318ae8c-b58f-471f-af74-9d9ec34edac3/.user_uploaded/media__1785457872062.png"
img = Image.open(img_path)

width, height = img.size
half_w, half_h = width // 2, height // 2

quadrants = {
    "mohsin": (0, 0, half_w, half_h),
    "ayush": (half_w, 0, width, half_h),
    "abhinav": (0, half_h, half_w, height),
    "rohit": (half_w, half_h, width, height)
}

for name, box in quadrants.items():
    quad = img.crop(box)
    
    # We want to crop from the top mostly, avoid below the neck.
    # The quadrant has a border and text. Let's crop closer to the center.
    qw, qh = quad.size
    
    # Estimate the head location in these specific image cards
    # The head is roughly in the top middle of the card.
    cx, cy = qw // 2, int(qh * 0.45)
    
    # Create a square crop
    size = int(min(qw, qh) * 0.5)
    
    left = max(0, cx - size // 2)
    top = max(0, cy - int(size * 0.6))
    right = left + size
    bottom = top + size
    
    headshot = quad.crop((left, top, right, bottom))
    headshot = headshot.resize((400, 400), Image.Resampling.LANCZOS)
    headshot.save(f"assets/images/team/{name}.webp", format="WEBP", quality=90)
    print(f"Saved {name}.webp")
