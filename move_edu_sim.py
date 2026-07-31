import glob
import re

html_files = glob.glob("**/*.html", recursive=True)
count = 0

for file in html_files:
    if "node_modules" in file or ".git" in file:
        continue
        
    with open(file, "r") as f:
        content = f.read()
    
    # We want to replace the VR/XR dropdown section
    # Find:
    # <li class="dropdown-header">VR / XR</li>
    # <li><a class="dropdown-link sub-link" href=".../educational-simulations/">Educational Simulations</a></li>
    # <li><a class="dropdown-link sub-link" href=".../room-raider/">Room Raider</a></li>
    # <li><a class="dropdown-link sub-link" href=".../shemarooverse/">Shemarooverse</a></li>
    # <li><a class="dropdown-link sub-link" href=".../mayaaverse/">Mayaaverse</a></li>
    # <li><a class="dropdown-link category-link" href="...">View All VR/XR →</a></li>
    
    # We can match this entire block and replace it
    pattern = r'(<li class="dropdown-header">VR / XR</li>)\s*(<li><a class="dropdown-link sub-link" href=".*?/educational-simulations/">Educational Simulations</a></li>)\s*(<li><a class="dropdown-link sub-link" href=".*?/room-raider/">Room Raider</a></li>)\s*(<li><a class="dropdown-link sub-link" href=".*?/shemarooverse/">Shemarooverse</a></li>)\s*(<li><a class="dropdown-link sub-link" href=".*?/mayaaverse/">Mayaaverse</a></li>)'
    
    def replacer(match):
        header = match.group(1)
        edu = match.group(2)
        room = match.group(3)
        shem = match.group(4)
        maya = match.group(5)
        
        # New order: room, shem, maya, edu
        return f'{header}\n              {room}\n              {shem}\n              {maya}\n              {edu}'
        
    new_content, num_replacements = re.subn(pattern, replacer, content)
    
    if num_replacements > 0:
        with open(file, "w") as f:
            f.write(new_content)
        print(f"Updated navigation in {file}")
        count += 1

print(f"Total files updated: {count}")
