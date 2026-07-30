import os
import re

def fix_active_nav(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Determine which section we are in
    # The active keyword will be based on the top-level directory (or root)
    if '/about/' in filepath:
        active_target = '>About<'
    elif '/blog/' in filepath:
        active_target = '>Blog<'
    elif '/contact/' in filepath:
        active_target = '>Contact<'
    elif '/services/' in filepath:
        active_target = '>Services'
    elif '/work/' in filepath:
        active_target = '>Portfolio'
    elif '/reclairos/' in filepath:
        active_target = '>Reclairos<'
    elif filepath == './index.html':
        active_target = '>Home<'
    else:
        # Other pages like privacy-policy, terms might not have an active tab
        active_target = None

    # First, strip ' active' from ALL nav-links in the menu.
    content = re.sub(r'class="nav-link\s+active"', 'class="nav-link"', content)
    content = re.sub(r'class="nav-link\s+dropdown-toggle\s+active"', 'class="nav-link dropdown-toggle"', content)
    
    if active_target:
        # Now add ' active' to the target
        if active_target == '>Services' or active_target == '>Portfolio':
            pattern = re.compile(r'(<a[^>]*class="nav-link\s+dropdown-toggle"[^>]*>)\s*' + active_target[1:], re.IGNORECASE | re.DOTALL)
            def add_active_class(match):
                anchor_start = match.group(1)
                new_anchor = anchor_start.replace('class="nav-link dropdown-toggle"', 'class="nav-link dropdown-toggle active"')
                return new_anchor + match.group(0)[len(anchor_start):]
            content = pattern.sub(add_active_class, content)
        else:
            pattern = re.compile(r'(<a[^>]*class="nav-link"[^>]*>)\s*' + active_target[1:], re.IGNORECASE | re.DOTALL)
            def add_active_class_reg(match):
                anchor_start = match.group(1)
                new_anchor = anchor_start.replace('class="nav-link"', 'class="nav-link active"')
                return new_anchor + match.group(0)[len(anchor_start):]
            content = pattern.sub(add_active_class_reg, content)

    with open(filepath, 'w') as f:
        f.write(content)

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.gsd' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            fix_active_nav(path)

print("Done fixing active nav states.")
