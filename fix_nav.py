import re

files = [
    "work/game-art/concept-art/index.html",
    "work/game-art/character-art/index.html",
    "work/game-art/animation/index.html"
]

for file in files:
    with open(file, "r") as f:
        content = f.read()
    
    new_block = """<li class="dropdown-header">Game Art</li>
              <li><a class="dropdown-link sub-link" href="../../../work/game-art/concept-art/">Concept Art</a></li>
              <li><a class="dropdown-link sub-link" href="../../../work/game-art/character-art/">Character Art</a></li>
              <li><a class="dropdown-link sub-link" href="../../../work/game-art/environment-art/">Environment Art</a></li>
              <li><a class="dropdown-link sub-link" href="../../../work/game-art/animation/">Animation</a></li>
              <li><a class="dropdown-link sub-link" href="../../../work/game-art/technical-art-benchmarks/">Technical Art Benchmarks</a></li>"""

    content = re.sub(r"<li class=\"dropdown-header\">Game Art</li>.*?<li><a class=\"dropdown-link sub-link\" href=\"\.\.\/\.\.\/\.\.\/work\/game-art\/environment-art\/\">.*?</a></li>", new_block, content, flags=re.DOTALL)
    
    with open(file, "w") as f:
        f.write(content)
    print("Fixed " + file)
