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
    # <li><a class="dropdown-link sub-link" href=".../room-raider/">Room Raider</a></li>
    
    # regex pattern
    pattern = r'(<li class="dropdown-header">VR / XR</li>\s*<li><a class="dropdown-link sub-link" href="(.*?work/vr-xr/)room-raider/">Room Raider</a></li>)'
    
    def replacer(match):
        prefix = match.group(2)
        return f'<li class="dropdown-header">VR / XR</li>\n              <li><a class="dropdown-link sub-link" href="{prefix}educational-simulations/">Educational Simulations</a></li>\n              <li><a class="dropdown-link sub-link" href="{prefix}room-raider/">Room Raider</a></li>'
        
    new_content, num_replacements = re.subn(pattern, replacer, content)
    
    if num_replacements > 0:
        with open(file, "w") as f:
            f.write(new_content)
        print(f"Updated navigation in {file}")
        count += 1

print(f"Total files updated: {count}")
