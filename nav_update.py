import glob
import os

html_files = glob.glob("**/*.html", recursive=True)

for file in html_files:
    if "node_modules" in file or ".git" in file:
        continue
        
    with open(file, "r") as f:
        content = f.read()
    
    # We want to replace the Game Art dropdown section
    # Find:
    # <li class="dropdown-header">Game Art</li>
    # <li><a class="dropdown-link sub-link" href=".../technical-art-benchmarks/">Technical Art Benchmarks</a></li>
    # <li><a class="dropdown-link sub-link" href=".../environment-art/">Environment Art</a></li>
    
    # Let's use regex to find this block and replace it with all 5 links
    import re
    match = re.search(r"<li class=\"dropdown-header\">Game Art</li>\s*<li><a class=\"dropdown-link sub-link\" href=\"(.*?work/game-art/)technical-art-benchmarks/\">Technical Art Benchmarks</a></li>\s*<li><a class=\"dropdown-link sub-link\" href=\".*?environment-art/\">Environment Art</a></li>", content)
    
    if match:
        prefix = match.group(1)
        new_block = f"""<li class="dropdown-header">Game Art</li>
              <li><a class="dropdown-link sub-link" href="{prefix}concept-art/">Concept Art</a></li>
              <li><a class="dropdown-link sub-link" href="{prefix}character-art/">Character Art</a></li>
              <li><a class="dropdown-link sub-link" href="{prefix}environment-art/">Environment Art</a></li>
              <li><a class="dropdown-link sub-link" href="{prefix}animation/">Animation</a></li>
              <li><a class="dropdown-link sub-link" href="{prefix}technical-art-benchmarks/">Technical Art Benchmarks</a></li>"""
        
        new_content = content.replace(match.group(0), new_block)
        if new_content != content:
            with open(file, "w") as f:
                f.write(new_content)
            print(f"Updated navigation in {file}")
