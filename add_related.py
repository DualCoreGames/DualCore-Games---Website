import os
import re

projects = [
    {
        "file": "work/vr-xr/room-raider/index.html",
        "related": [
            {"name": "Mayaaverse", "url": "../mayaaverse/", "desc": "Virtual Temple Sanctuary", "img": "../../assets/mayaaverse-hero-bg.webp"},
            {"name": "Educational Simulations", "url": "../educational-simulations/", "desc": "Enterprise XR Training", "img": "../../assets/room-raider-hero.webp"} # Placeholder img
        ]
    },
    {
        "file": "work/vr-xr/mayaaverse/index.html",
        "related": [
            {"name": "Shemarooverse", "url": "../shemarooverse/", "desc": "Bollywood VR Experience", "img": "../../assets/shemarooverse-hero.webp"},
            {"name": "Room Raider", "url": "../room-raider/", "desc": "Mixed Reality Action", "img": "../../assets/room-raider-hero.webp"}
        ]
    },
    {
        "file": "work/vr-xr/shemarooverse/index.html",
        "related": [
            {"name": "Mayaaverse", "url": "../mayaaverse/", "desc": "Virtual Temple Sanctuary", "img": "../../assets/mayaaverse-hero-bg.webp"},
            {"name": "Educational Simulations", "url": "../educational-simulations/", "desc": "Enterprise XR Training", "img": "../../assets/room-raider-hero.webp"}
        ]
    },
    {
        "file": "work/vr-xr/educational-simulations/index.html",
        "related": [
            {"name": "Room Raider", "url": "../room-raider/", "desc": "Mixed Reality Action", "img": "../../assets/room-raider-hero.webp"},
            {"name": "Shemarooverse", "url": "../shemarooverse/", "desc": "Bollywood VR Experience", "img": "../../assets/shemarooverse-hero.webp"}
        ]
    }
]

for proj in projects:
    if not os.path.exists(proj["file"]):
        print(f"Not found: {proj['file']}")
        continue
        
    with open(proj["file"], "r") as f:
        content = f.read()
        
    if 'class="related-projects"' in content:
        continue # Already added
        
    related_html = f"""
<!-- Related Projects -->
<section class="section-padding related-projects" style="background-color: var(--color-bg); border-top: 1px solid rgba(255,255,255,0.05);">
<div class="container">
<h3 style="margin-bottom: 2rem; font-size: 2rem;">Explore More VR/XR</h3>
<div class="grid" style="grid-template-columns: 1fr 1fr; gap: 2rem;">
  <a href="{proj['related'][0]['url']}" class="card" style="text-decoration: none; background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.05); transition: transform 0.2s; display: block;">
    <h4 style="color: #fff; margin-bottom: 0.5rem; font-size: 1.25rem;">{proj['related'][0]['name']}</h4>
    <p class="text-muted" style="margin: 0;">{proj['related'][0]['desc']} →</p>
  </a>
  <a href="{proj['related'][1]['url']}" class="card" style="text-decoration: none; background-color: #1a1a1a; padding: 1.5rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.05); transition: transform 0.2s; display: block;">
    <h4 style="color: #fff; margin-bottom: 0.5rem; font-size: 1.25rem;">{proj['related'][1]['name']}</h4>
    <p class="text-muted" style="margin: 0;">{proj['related'][1]['desc']} →</p>
  </a>
</div>
</div>
</section>
"""
    
    # Insert right before </main>
    new_content = content.replace("</main>", related_html + "\n</main>")
    
    with open(proj["file"], "w") as f:
        f.write(new_content)
        
    print(f"Added related projects to {proj['file']}")
