import os, glob, re

files = glob.glob("**/*.html", recursive=True)
all_links = set()
broken_links = []

for f in files:
    if "node_modules" not in f and ".git" not in f:
        if f.endswith("index.html"):
            all_links.add("/" + f.replace("index.html", ""))
        all_links.add("/" + f)

for f in files:
    if "node_modules" in f or ".git" in f:
        continue
    with open(f, "r") as html:
        content = html.read()
    
    hrefs = re.findall(r'href="([^"]+)"', content)
    for href in hrefs:
        if href.startswith("http") or href.startswith("mailto") or href.startswith("#") or href.startswith("javascript"):
            continue
        
        current_dir = "/" + os.path.dirname(f)
        if current_dir == "/":
            current_dir = ""
            
        if href.startswith("/"):
            abs_href = href
        else:
            parts = current_dir.split("/")
            href_parts = href.split("/")
            for p in href_parts:
                if p == "..":
                    if len(parts) > 1:
                        parts.pop()
                elif p == "." or p == "":
                    pass
                else:
                    parts.append(p)
            
            abs_href = "/".join(parts)
            if href.endswith("/"):
                abs_href += "/"
        
        if not abs_href.endswith(".html") and not abs_href.endswith("/") and "." not in abs_href.split("/")[-1]:
             abs_href += "/"
             
        if abs_href not in all_links and abs_href.split("?")[0] not in all_links:
            is_asset = False
            for asset_ext in [".css", ".png", ".svg", ".webp", ".jpg", ".mp4", ".ico"]:
                if abs_href.endswith(asset_ext):
                    if os.path.exists(abs_href.lstrip("/")):
                        is_asset = True
                    break
            
            if not is_asset:
                broken_links.append((f, href, abs_href))

if len(broken_links) > 0:
    for bl in broken_links[:10]:
        print(f"Broken link in {bl[0]}: {bl[1]} -> resolved to {bl[2]}")
    print(f"Total potential broken local links: {len(broken_links)}")
else:
    print("No broken local HTML links found!")
