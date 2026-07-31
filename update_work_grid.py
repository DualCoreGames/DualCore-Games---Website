import re

with open("work/index.html", "r") as f:
    work_content = f.read()

# The 5 cards we want to insert. Notice the relative paths will be different.
# In work/game-art/index.html, hrefs are "concept-art/"
# In work/index.html, hrefs should be "game-art/concept-art/"
# Images in work/game-art/index.html are "../../assets/images/placeholder-asset.webp"
# Images in work/index.html should be "../assets/images/placeholder-asset.webp"

new_cards = """
          <!-- Card 2: Environment Design -->
          <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; height: 100%;">
            <div style="aspect-ratio: 16/9; width: 100%; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.04); position: relative;">
              <img alt="Atmospheric Environment Design" loading="lazy" src="../assets/images/placeholder-asset.webp" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;" />
            </div>
            <div style="padding: 2.5rem; flex-grow: 1; display: flex; flex-direction: column;">
              <span class="text-accent" style="font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; display: block; margin-bottom: 0.5rem;">LEVEL ART</span>
              <h3 style="margin-bottom: 1rem;">Environment Art</h3>
              <p class="text-muted" style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.5; flex-grow: 1;">Custom environment assets and lighting setups designed for immersive storytelling across diverse platforms.</p>
              <div style="margin-top: auto;">
                <a class="btn btn-secondary" href="game-art/environment-art/" style="padding: 0.6rem 1.2rem; font-size: 0.75rem; width: auto;">Explore Environments →</a>
              </div>
            </div>
          </div>
          
          <!-- Card 3: Concept Art -->
          <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; height: 100%;">
            <div style="aspect-ratio: 16/9; width: 100%; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.04); position: relative;">
              <img alt="Concept Art & Pre-Production" loading="lazy" src="../assets/images/placeholder-asset.webp" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;" />
            </div>
            <div style="padding: 2.5rem; flex-grow: 1; display: flex; flex-direction: column;">
              <span class="text-accent" style="font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; display: block; margin-bottom: 0.5rem;">2D ILLUSTRATION</span>
              <h3 style="margin-bottom: 1rem;">Concept Art</h3>
              <p class="text-muted" style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.5; flex-grow: 1;">Pre-production character design, environment concepts, mood boards, and storyboards.</p>
              <div style="margin-top: auto;">
                <a class="btn btn-secondary" href="game-art/concept-art/" style="padding: 0.6rem 1.2rem; font-size: 0.75rem; width: auto;">Explore Concepts →</a>
              </div>
            </div>
          </div>
          
          <!-- Card 4: Character Art -->
          <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; height: 100%;">
            <div style="aspect-ratio: 16/9; width: 100%; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.04); position: relative;">
              <img alt="Character Art & Modeling" loading="lazy" src="../assets/images/placeholder-asset.webp" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;" />
            </div>
            <div style="padding: 2.5rem; flex-grow: 1; display: flex; flex-direction: column;">
              <span class="text-accent" style="font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; display: block; margin-bottom: 0.5rem;">3D MODELING</span>
              <h3 style="margin-bottom: 1rem;">Character Art</h3>
              <p class="text-muted" style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.5; flex-grow: 1;">High-poly sculpts, low-poly game-ready models, texturing, rigging, and anatomy studies.</p>
              <div style="margin-top: auto;">
                <a class="btn btn-secondary" href="game-art/character-art/" style="padding: 0.6rem 1.2rem; font-size: 0.75rem; width: auto;">Explore Characters →</a>
              </div>
            </div>
          </div>
          
          <!-- Card 5: Animation -->
          <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; height: 100%;">
            <div style="aspect-ratio: 16/9; width: 100%; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.04); position: relative;">
              <img alt="Animation & Rigging" loading="lazy" src="../assets/images/placeholder-asset.webp" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;" />
            </div>
            <div style="padding: 2.5rem; flex-grow: 1; display: flex; flex-direction: column;">
              <span class="text-accent" style="font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; display: block; margin-bottom: 0.5rem;">KEYFRAME & MOCAP</span>
              <h3 style="margin-bottom: 1rem;">Animation</h3>
              <p class="text-muted" style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.5; flex-grow: 1;">Skeletal rigging, motion capture cleanup, keyframe animation, and combat loops.</p>
              <div style="margin-top: auto;">
                <a class="btn btn-secondary" href="game-art/animation/" style="padding: 0.6rem 1.2rem; font-size: 0.75rem; width: auto;">Explore Animation →</a>
              </div>
            </div>
          </div>

          <!-- Card 1: Technical Art Benchmarks -->
          <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; height: 100%;">
            <div style="aspect-ratio: 16/9; width: 100%; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.04); position: relative;">
              <img alt="Technical Art & Shader Benchmarks" loading="lazy" src="../assets/images/placeholder-asset.webp" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;" />
            </div>
            <div style="padding: 2.5rem; flex-grow: 1; display: flex; flex-direction: column;">
              <span class="text-accent" style="font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; display: block; margin-bottom: 0.5rem;">SHADERS & VFX</span>
              <h3 style="margin-bottom: 1rem;">Technical Art Benchmarks</h3>
              <p class="text-muted" style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.5; flex-grow: 1;">A collection of high-performance shaders, procedural VFX, and optimization techniques for mobile and VR.</p>
              <div style="margin-top: auto;">
                <a class="btn btn-secondary" href="game-art/technical-art-benchmarks/" style="padding: 0.6rem 1.2rem; font-size: 0.75rem; width: auto;">Explore Benchmarks →</a>
              </div>
            </div>
          </div>
"""

# Find the game-art portfolio-section and replace the grid inside it
pattern = r'(<div class="portfolio-section" data-category="game-art".*?<div class="grid portfolio-grid">)(.*?)(</div>\s*</div>\s*</section>)'
new_content = re.sub(pattern, r'\1\n' + new_cards + r'\n\3', work_content, flags=re.DOTALL)

with open("work/index.html", "w") as f:
    f.write(new_content)
print("Updated work/index.html")
