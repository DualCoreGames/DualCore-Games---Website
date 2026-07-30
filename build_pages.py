import os, re

with open("work/game-art/environment-art/index.html", "r") as f:
    template = f.read()

pages = [
    {
        "path": "work/game-art/concept-art/index.html",
        "title": "Concept Art",
        "desc": "Pre-production character design, environment concepts, mood boards, and storyboards.",
        "meta": "2D Illustrations &amp; Pre-Production",
        "label": "Concept Studies",
        "p1_title": "Sci-Fi Environment Concepts",
        "p1_desc": "Mood boards and architectural sketches for future orbital stations.",
        "p2_title": "Character Iterations",
        "p2_desc": "Iterative design process from rough sketch to finalized character sheet."
    },
    {
        "path": "work/game-art/character-art/index.html",
        "title": "Character Art",
        "desc": "High-poly sculpts, low-poly game-ready models, texturing, rigging, and anatomy studies.",
        "meta": "3D Modeling &amp; Texturing",
        "label": "Character Studies",
        "p1_title": "High-Poly ZBrush Sculpts",
        "p1_desc": "Detailed organic and hard-surface modeling for main protagonists.",
        "p2_title": "Game-Ready Topology",
        "p2_desc": "Optimized wireframes and PBR texture breakdowns."
    },
    {
        "path": "work/game-art/animation/index.html",
        "title": "Animation",
        "desc": "Skeletal rigging, motion capture cleanup, keyframe animation, and combat loops.",
        "meta": "Keyframe &amp; MoCap",
        "label": "Motion Studies",
        "p1_title": "Combat Attack Sequences",
        "p1_desc": "Fluid keyframe animations focusing on weight, anticipation, and follow-through.",
        "p2_title": "Idle &amp; Traversal Loops",
        "p2_desc": "Seamless looping animations for standard gameplay states."
    }
]

placeholder_section = """
    <section class="cs-section">
      <div class="container">
        <!-- Project 1 -->
        <div class="project-showcase-item">
          <span class="cs-section-num">01 &nbsp;/&nbsp; Showcase</span>
          <h3>{p1_title}</h3>
          <div style="margin-bottom: 2rem;">
            <p style="color: var(--color-text-muted); font-size: 1rem; line-height: 1.8;">{p1_desc}</p>
          </div>
          <div style="aspect-ratio: 16/9; width: 100%; background: #111; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
            <img src="../../../assets/images/placeholder-asset.webp" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.5;" alt="Placeholder">
            <div style="position: absolute; text-align: center;">
              <span style="font-size: 0.75rem; font-weight: 800; letter-spacing: 0.2em; color: var(--color-accent); text-transform: uppercase;">Awaiting Asset</span>
              <p style="margin: 0; color: #fff; font-size: 1.1rem; font-weight: 600;">Upload High-Res Media Here</p>
            </div>
          </div>
        </div>
        <!-- Project 2 -->
        <div class="project-showcase-item" style="margin-top: 6rem;">
          <span class="cs-section-num">02 &nbsp;/&nbsp; Showcase</span>
          <h3>{p2_title}</h3>
          <div style="margin-bottom: 2rem;">
            <p style="color: var(--color-text-muted); font-size: 1rem; line-height: 1.8;">{p2_desc}</p>
          </div>
          <div style="aspect-ratio: 16/9; width: 100%; background: #111; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
            <img src="../../../assets/images/placeholder-asset.webp" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.5;" alt="Placeholder">
            <div style="position: absolute; text-align: center;">
              <span style="font-size: 0.75rem; font-weight: 800; letter-spacing: 0.2em; color: var(--color-accent); text-transform: uppercase;">Awaiting Asset</span>
              <p style="margin: 0; color: #fff; font-size: 1.1rem; font-weight: 600;">Upload High-Res Media Here</p>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

for page in pages:
    content = template
    content = content.replace("Environment &amp; Level Design", page["title"])
    content = content.replace("Environment & Level Design", page["title"])
    content = content.replace("Environment Art", page["title"])
    
    url_base = page['path'].replace('index.html', '')
    content = re.sub(r"https://dualcoregames.com/work/game-art/environment-art/", "https://dualcoregames.com/" + url_base, content)
    
    content = re.sub(r"<p class=\"cs-hero__meta\">.*?</p>", "<p class=\"cs-hero__meta\">" + page['meta'] + "</p>", content)
    content = re.sub(r"<span class=\"cs-label\">.*?</span>", "<span class=\"cs-label\">" + page['label'] + "</span>", content)
    
    formatted_section = placeholder_section.replace("{p1_title}", page["p1_title"])
    formatted_section = formatted_section.replace("{p1_desc}", page["p1_desc"])
    formatted_section = formatted_section.replace("{p2_title}", page["p2_title"])
    formatted_section = formatted_section.replace("{p2_desc}", page["p2_desc"])
    
    content = re.sub(r"<section class=\"cs-section\">.*?</section>", formatted_section, content, flags=re.DOTALL)
    
    content = re.sub(r"<div class=\"cs-meta-grid\">.*?</div>\s*</div>\s*</section>", "</div></section>", content, flags=re.DOTALL)
    
    with open(page["path"], "w") as f:
        f.write(content)
    print("Created " + page['path'])

# Now let's fix environment-art and technical-art-benchmarks
for p in ["work/game-art/environment-art/index.html", "work/game-art/technical-art-benchmarks/index.html"]:
    with open(p, "r") as f:
        c = f.read()
    c = re.sub(r"<section class=\"cs-section\">.*?</section>", formatted_section, c, flags=re.DOTALL)
    with open(p, "w") as f:
        f.write(c)
    print("Updated " + p)
