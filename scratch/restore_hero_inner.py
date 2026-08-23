import re

with open('reclairos/index.html', 'r') as f:
    html = f.read()

# Pattern to find the .rc-hero__inner override in the first media query
pattern = r"\s*\.rc-hero__inner\s*{\s*padding-bottom:\s*0\s*!important;\s*margin-bottom:\s*15vh\s*!important;\s*/\*\s*Move text and CTA up\s*\*/\s*}\n"

new_html = re.sub(pattern, "\n", html)

with open('reclairos/index.html', 'w') as f:
    f.write(new_html)
