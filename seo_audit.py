import os, glob, re, json

files = glob.glob("**/*.html", recursive=True)
issues = []
stats = {"total_pages": 0, "missing_title": 0, "missing_desc": 0, "missing_h1": 0, "multiple_h1": 0, "missing_canonical": 0, "mismatched_canonical": 0}

for f in files:
    if "node_modules" in f or ".git" in f or "404.html" in f:
        continue
    
    stats["total_pages"] += 1
    with open(f, "r") as html_file:
        content = html_file.read()
    
    page_issues = []
    
    # Title
    title_match = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
    if not title_match:
        page_issues.append("Missing <title> tag")
        stats["missing_title"] += 1
    else:
        title = title_match.group(1).strip()
        if len(title) == 0:
            page_issues.append("Empty <title> tag")
            stats["missing_title"] += 1
        elif len(title) > 60:
            pass # just a warning normally, we can ignore for now
            
    # Meta Description
    desc_match = re.search(r"<meta[^>]*name=[\"']description[\"'][^>]*content=[\"'](.*?)[\"'][^>]*>", content, re.IGNORECASE)
    if not desc_match:
        page_issues.append("Missing meta description")
        stats["missing_desc"] += 1
    else:
        desc = desc_match.group(1).strip()
        if len(desc) == 0:
            page_issues.append("Empty meta description")
            stats["missing_desc"] += 1

    # H1
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", content, re.IGNORECASE | re.DOTALL)
    if len(h1s) == 0:
        page_issues.append("Missing <h1> tag")
        stats["missing_h1"] += 1
    elif len(h1s) > 1:
        page_issues.append(f"Multiple <h1> tags found ({len(h1s)})")
        stats["multiple_h1"] += 1
        
    # Canonical
    canonical_match = re.search(r"<link[^>]*rel=[\"']canonical[\"'][^>]*href=[\"'](.*?)[\"'][^>]*>", content, re.IGNORECASE)
    expected_path = f.replace("index.html", "")
    expected_canonical = f"https://dualcoregames.com/{expected_path}"
    
    if not canonical_match:
        page_issues.append("Missing canonical link")
        stats["missing_canonical"] += 1
    else:
        canonical = canonical_match.group(1).strip()
        if canonical != expected_canonical:
            page_issues.append(f"Mismatched canonical: expected {expected_canonical}, got {canonical}")
            stats["mismatched_canonical"] += 1
            
    if page_issues:
        issues.append({"file": f, "issues": page_issues})

# Save results
with open("seo_audit_results.json", "w") as out:
    json.dump({"stats": stats, "issues": issues}, out, indent=2)

print("SEO Audit Complete. Found issues in", len(issues), "files.")
print("Stats:", stats)
