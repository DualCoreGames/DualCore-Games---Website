import glob
import re
import os

html_files = glob.glob("**/*.html", recursive=True)

print("--- Performance & SEO Check ---")

missing_lazy = []
heavy_images = []

for file in html_files:
    if "node_modules" in file or ".git" in file:
        continue
        
    with open(file, "r") as f:
        content = f.read()
        
    # Check for images without loading="lazy" (skip the first image or hero images if possible, but let's just find them)
    images = re.findall(r'<img[^>]+>', content)
    
    for idx, img in enumerate(images):
        if 'loading="lazy"' not in img:
            # Hero images shouldn't be lazy loaded usually. Let's flag them anyway to see.
            missing_lazy.append((file, img))
            
# Check actual image sizes on disk
img_files = glob.glob("**/*.webp", recursive=True) + glob.glob("**/*.png", recursive=True) + glob.glob("**/*.jpg", recursive=True)
for img_path in img_files:
    if "node_modules" in img_path or ".git" in img_path:
        continue
    size_kb = os.path.getsize(img_path) / 1024
    if size_kb > 500: # flag over 500kb
        heavy_images.append((img_path, size_kb))
        
print(f"Images missing loading=\"lazy\": {len(missing_lazy)}")
for f, img in missing_lazy[:10]:
    print(f"  {f}: {img}")
if len(missing_lazy) > 10: print("  ...")

print(f"\nHeavy Images (> 500KB): {len(heavy_images)}")
for p, s in heavy_images:
    print(f"  {p}: {s:.2f} KB")

# Check viewport meta tag for mobile responsiveness
viewport_missing = []
for file in html_files:
    if "node_modules" in file or ".git" in file:
        continue
    with open(file, "r") as f:
        content = f.read()
    if '<meta name="viewport" content="width=device-width, initial-scale=1.0">' not in content:
        if '<meta name="viewport"' not in content:
            viewport_missing.append(file)
            
print(f"\nFiles missing viewport meta: {len(viewport_missing)}")
for f in viewport_missing:
    print(f"  {f}")
