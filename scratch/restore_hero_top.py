import re

with open('reclairos/index.html', 'r') as f:
    html = f.read()

# Pattern to find the exact block I added earlier and remove it.
# We'll remove from "/* ── KEY FIX: drop badges OUT of the image area on mobile ── */"
# up to the closing brace of ".rc-hero__inner { ... }"

pattern = r"\s*/\*\s*── KEY FIX: drop badges OUT of the image area on mobile ── \*/.*?margin-top: 0;\s*}\n"

new_html = re.sub(pattern, "\n", html, flags=re.DOTALL)

with open('reclairos/index.html', 'w') as f:
    f.write(new_html)
