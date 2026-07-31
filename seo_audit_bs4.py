import os, glob, json
from bs4 import BeautifulSoup

files = glob.glob("**/*.html", recursive=True)
issues = []
stats = {"total_pages": 0, "missing_title": 0, "missing_desc": 0, "missing_h1": 0, "multiple_h1": 0, "missing_canonical": 0, "mismatched_canonical": 0}

for f in files:
    if "node_modules" in f or ".git" in f or "404.html" in f:
        continue
    
    stats["total_pages"] += 1
    with open(f, "r") as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    
    page_issues = []
    
    # Title
    title_tag = soup.find('title')
    if not title_tag or not title_tag.string:
        page_issues.append("Missing or empty <title> tag")
        stats["missing_title"] += 1
        
    # Meta Description
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    if not desc_tag or not desc_tag.get('content') or len(desc_tag['content'].strip()) == 0:
        page_issues.append("Missing or empty meta description")
        stats["missing_desc"] += 1

    # H1
    h1s = soup.find_all('h1')
    if len(h1s) == 0:
        page_issues.append("Missing <h1> tag")
        stats["missing_h1"] += 1
    elif len(h1s) > 1:
        page_issues.append(f"Multiple <h1> tags found ({len(h1s)})")
        stats["multiple_h1"] += 1
        
    # Canonical
    canonical_tag = soup.find('link', attrs={'rel': 'canonical'})
    expected_path = f.replace("index.html", "")
    expected_canonical = f"https://dualcoregames.com/{expected_path}"
    
    if not canonical_tag or not canonical_tag.get('href'):
        page_issues.append("Missing canonical link")
        stats["missing_canonical"] += 1
    else:
        canonical = canonical_tag['href'].strip()
        if canonical != expected_canonical:
            page_issues.append(f"Mismatched canonical: expected {expected_canonical}, got {canonical}")
            stats["mismatched_canonical"] += 1
            
    if page_issues:
        issues.append({"file": f, "issues": page_issues})

with open("seo_audit_bs4.json", "w") as out:
    json.dump({"stats": stats, "issues": issues}, out, indent=2)

print("SEO Audit Complete. Found issues in", len(issues), "files.")
print("Stats:", stats)
