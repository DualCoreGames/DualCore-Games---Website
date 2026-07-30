import re

with open("work/game-art/index.html", "r") as f:
    content = f.read()

new_cards = """
          <!-- Card 3: Concept Art -->
          <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; height: 100%;">
            <div style="aspect-ratio: 16/9; width: 100%; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.04); position: relative;">
              <img alt="Concept Art & Pre-Production" loading="lazy" src="../../assets/images/placeholder-asset.webp" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;" />
            </div>
            <div style="padding: 2.5rem; flex-grow: 1; display: flex; flex-direction: column;">
              <span class="text-accent" style="font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; display: block; margin-bottom: 0.5rem;">2D ILLUSTRATION</span>
              <h3 style="margin-bottom: 1rem;">Concept Art</h3>
              <p class="text-muted" style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.5; flex-grow: 1;">Pre-production character design, environment concepts, mood boards, and storyboards.</p>
              <div style="margin-top: auto;">
                <a class="btn btn-secondary" href="concept-art/" style="padding: 0.6rem 1.2rem; font-size: 0.75rem; width: auto;">Explore Concepts →</a>
              </div>
            </div>
          </div>
          
          <!-- Card 4: Character Art -->
          <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; height: 100%;">
            <div style="aspect-ratio: 16/9; width: 100%; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.04); position: relative;">
              <img alt="Character Art & Modeling" loading="lazy" src="../../assets/images/placeholder-asset.webp" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;" />
            </div>
            <div style="padding: 2.5rem; flex-grow: 1; display: flex; flex-direction: column;">
              <span class="text-accent" style="font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; display: block; margin-bottom: 0.5rem;">3D MODELING</span>
              <h3 style="margin-bottom: 1rem;">Character Art</h3>
              <p class="text-muted" style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.5; flex-grow: 1;">High-poly sculpts, low-poly game-ready models, texturing, rigging, and anatomy studies.</p>
              <div style="margin-top: auto;">
                <a class="btn btn-secondary" href="character-art/" style="padding: 0.6rem 1.2rem; font-size: 0.75rem; width: auto;">Explore Characters →</a>
              </div>
            </div>
          </div>
          
          <!-- Card 5: Animation -->
          <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; height: 100%;">
            <div style="aspect-ratio: 16/9; width: 100%; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.04); position: relative;">
              <img alt="Animation & Rigging" loading="lazy" src="../../assets/images/placeholder-asset.webp" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;" />
            </div>
            <div style="padding: 2.5rem; flex-grow: 1; display: flex; flex-direction: column;">
              <span class="text-accent" style="font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; display: block; margin-bottom: 0.5rem;">KEYFRAME & MOCAP</span>
              <h3 style="margin-bottom: 1rem;">Animation</h3>
              <p class="text-muted" style="margin-bottom: 2rem; font-size: 0.95rem; line-height: 1.5; flex-grow: 1;">Skeletal rigging, motion capture cleanup, keyframe animation, and combat loops.</p>
              <div style="margin-top: auto;">
                <a class="btn btn-secondary" href="animation/" style="padding: 0.6rem 1.2rem; font-size: 0.75rem; width: auto;">Explore Animation →</a>
              </div>
            </div>
          </div>
"""

match = re.search(r"<!-- Card 1: Technical Art Benchmarks -->", content)
if match:
    new_content = content[:match.start()] + new_cards + content[match.start():]
    with open("work/game-art/index.html", "w") as f:
        f.write(new_content)
    print("Updated work/game-art/index.html")
