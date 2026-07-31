import cv2
import os
import urllib.request
import numpy as np

# Create directory
os.makedirs("assets/images/team", exist_ok=True)

# Image path
img_path = "/Users/abhinav/.gemini/antigravity/brain/3318ae8c-b58f-471f-af74-9d9ec34edac3/.user_uploaded/media__1785457872062.png"

# Read image
img = cv2.imread(img_path)
h, w = img.shape[:2]

# Download Haar Cascade if not present
cascade_path = "haarcascade_frontalface_default.xml"
if not os.path.exists(cascade_path):
    url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
    urllib.request.urlretrieve(url, cascade_path)

face_cascade = cv2.CascadeClassifier(cascade_path)

# Quadrants: Top-Left (Mohsin), Top-Right (Ayush), Bottom-Left (Abhinav), Bottom-Right (Rohit)
quadrants = {
    "mohsin": img[0:h//2, 0:w//2],
    "ayush": img[0:h//2, w//2:w],
    "abhinav": img[h//2:h, 0:w//2],
    "rohit": img[h//2:h, w//2:w]
}

for name, quad in quadrants.items():
    gray = cv2.cvtColor(quad, cv2.COLOR_BGR2GRAY)
    
    # Detect face
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) > 0:
        # Take the largest face
        faces = sorted(faces, key=lambda x: x[2]*x[3], reverse=True)
        x, y, fw, fh = faces[0]
        
        # Add some padding to make it a nice headshot (not too tight, but no neck)
        # We want to crop from a bit above the head, and cut off at the chin/neck.
        # Let's expand the bounding box slightly.
        pad_top = int(fh * 0.4)
        pad_bottom = int(fh * 0.2)
        pad_sides = int(fw * 0.3)
        
        y1 = max(0, y - pad_top)
        y2 = min(quad.shape[0], y + fh + pad_bottom)
        x1 = max(0, x - pad_sides)
        x2 = min(quad.shape[1], x + fw + pad_sides)
        
        # Make it perfectly square
        crop_h = y2 - y1
        crop_w = x2 - x1
        size = min(crop_h, crop_w)
        
        # Adjust to square
        if crop_h > crop_w:
            diff = crop_h - crop_w
            y1 += diff // 2
            y2 = y1 + size
        else:
            diff = crop_w - crop_h
            x1 += diff // 2
            x2 = x1 + size
            
        headshot = quad[y1:y2, x1:x2]
        
        # Resize to standard size
        headshot = cv2.resize(headshot, (400, 400))
        
        # Save as webp
        cv2.imwrite(f"assets/images/team/{name}.webp", headshot, [cv2.IMWRITE_WEBP_QUALITY, 90])
        print(f"Saved headshot for {name}")
    else:
        print(f"Face not detected for {name}")
