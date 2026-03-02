import sys
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw

def enhance_reclairos(input_path, output_path):
    print(f"Loading image from {input_path}...")
    try:
        img = Image.open(input_path).convert("RGB")
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # 1. Scale to 1920x1080 minimum while maintaining aspect ratio
    # Keep pixel sharpness (Nearest Neighbor)
    target_w, target_h = 1920, 1080
    img_w, img_h = img.size
    
    # Calculate scale factor to cover the target
    scale = max(target_w / img_w, target_h / img_h)
    new_w = int(img_w * scale)
    new_h = int(img_h * scale)
    
    print(f"Upscaling from {img_w}x{img_h} to {new_w}x{new_h} using NEAREST...")
    img = img.resize((new_w, new_h), Image.Resampling.NEAREST)
    
    # 2. Deepen shadow blacks and increase dynamic contrast
    print("Applying contrast and shadow enhancements...")
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.15) # Slight contrast increase
    
    # Convert to array for specific shadow deepening
    data = np.array(img, dtype=np.float32)
    # Deepen blacks: anything below a certain darkness gets darker, but don't clip completely
    shadow_mask = data < 60
    data[shadow_mask] = data[shadow_mask] * 0.85
    
    # 3. Slight warm tone grading for cinematic mood
    # Boost Red and Green channels slightly in midtones
    print("Applying warm tone grading...")
    data[:,:,0] = np.clip(data[:,:,0] * 1.05, 0, 255) # Red
    data[:,:,1] = np.clip(data[:,:,1] * 1.02, 0, 255) # Green
    
    img_graded = Image.fromarray(data.astype(np.uint8))
    
    # 4. Intensify fire glow softly (Controlled Bloom)
    print("Adding fire glow (bloom)...")
    # Tresholding to find intense fire (bright warm colors)
    threshold = 180
    bloom_mask_data = np.copy(data)
    # Zero out non-bright parts
    mask = (data[:,:,0] > threshold) & (data[:,:,1] > 100)
    bloom_mask_data[~mask] = 0
    bloom_layer = Image.fromarray(bloom_mask_data.astype(np.uint8))
    
    # Blur the bloom layer
    bloom_layer = bloom_layer.filter(ImageFilter.GaussianBlur(radius=40))
    
    # Composite bloom: Additive blend using screen mode approximation
    # Screen = 1 - (1 - a)*(1 - b)
    data_graded = np.array(img_graded, dtype=np.float32) / 255.0
    data_bloom = np.array(bloom_layer, dtype=np.float32) / 255.0
    screened = 1.0 - (1.0 - data_graded) * (1.0 - data_bloom * 0.6) # 0.6 opacity for controlled bloom
    img_bloomed = Image.fromarray((screened * 255).astype(np.uint8))
    
    # 5. Micro depth-of-field blur in far background ONLY
    # We create a gradient mask where the vertical center (throne/character) is sharp, and edges (especially top background) are blurred
    print("Applying micro depth-of-field blur...")
    blurred_img = img_bloomed.filter(ImageFilter.GaussianBlur(radius=6))
    
    # Create mask for DoF
    dof_mask = Image.new("L", (new_w, new_h), 0)
    draw = ImageDraw.Draw(dof_mask)
    # Top 20% of the image gets blurred (far background cave walls)
    blur_start_y = int(new_h * 0.3)
    for y in range(blur_start_y):
        intensity = int(255 * (1.0 - (y / blur_start_y)))
        draw.line([(0, y), (new_w, y)], fill=intensity)
        
    # Bottom 10% also slight blur for foreground depth
    blur_end_y = int(new_h * 0.85)
    for y in range(blur_end_y, new_h):
        intensity = int(255 * ((y - blur_end_y) / (new_h - blur_end_y)) * 0.5)
        draw.line([(0, y), (new_w, y)], fill=intensity)
        
    img_dof = Image.composite(blurred_img, img_bloomed, dof_mask)
    
    # 6. Add very subtle vignette around edges
    print("Adding vignette...")
    vignette = Image.new("L", (new_w, new_h), 255)
    draw_v = ImageDraw.Draw(vignette)
    
    # Center of vignette slightly offset to the top where the face is
    cx = new_w // 2
    cy = int(new_h * 0.45)
    max_dist = np.sqrt(cx**2 + cy**2) * 1.2
    
    vig_data = np.zeros((new_h, new_w), dtype=np.float32)
    Y, X = np.ogrid[:new_h, :new_w]
    dist_from_center = np.sqrt((X - cx)**2 + (Y - cy)**2)
    # Falloff factor
    vig_mask = 1.0 - (dist_from_center / max_dist)**2.5
    vig_mask = np.clip(vig_mask, 0.4, 1.0) # Never completely black
    
    final_data = np.array(img_dof, dtype=np.float32)
    for c in range(3):
        final_data[:,:,c] = final_data[:,:,c] * vig_mask
        
    final_image = Image.fromarray(final_data.astype(np.uint8))
    
    # 7. Crop to exactly 1920x1080 center to optimize for web aspect ratio
    left = (new_w - 1920) // 2
    top = (new_h - 1080) // 2
    right = left + 1920
    bottom = top + 1080
    final_image = final_image.crop((left, top, right, bottom))
    
    print(f"Saving final cinematic frame to {output_path}...")
    final_image.save(output_path, "WEBP", quality=90) # WEBP is optimized for web
    print("Done! Image is dark mode friendly and cinematic.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 enhance_key_art.py <input_image_path> <output_image_path>")
        sys.exit(1)
        
    enhance_reclairos(sys.argv[1], sys.argv[2])
