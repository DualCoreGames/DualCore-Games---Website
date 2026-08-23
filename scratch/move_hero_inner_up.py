import re

with open('reclairos/index.html', 'r') as f:
    html = f.read()

# We want to add a rule for .rc-hero__inner to the @media (max-width: 768px) block at line ~1445
# We can inject it after ".rc-hero__bg {" or similar. Let's find:
# .rc-hero {
#   min-height: 100svh;
#   height: auto;
# }
# and inject our inner rule right after it.

pattern = r"(\.rc-hero\s*\{\s*min-height:\s*100svh;\s*height:\s*auto;\s*\})"
replacement = r"\1\n      .rc-hero__inner {\n        padding-bottom: 0 !important;\n        margin-bottom: 15vh !important;\n      }"

new_html = re.sub(pattern, replacement, html)

with open('reclairos/index.html', 'w') as f:
    f.write(new_html)
