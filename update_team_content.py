import re
import json

with open("about/index.html", "r") as f:
    content = f.read()

# Replace the Meet the Team section
team_html = """
<!-- Meet the Team -->
<section class="section-padding" style="background-color: var(--color-bg); border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
<div class="container">
<h2 style="text-align: center; margin-bottom: 4rem; font-size: clamp(2rem, 4vw, 3rem);">Meet the Team</h2>
<div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
  
  <!-- Team Member 1 -->
  <div class="card" style="background-color: #1a1a1a; padding: 2rem; border-radius: 8px; text-align: center; border: 1px solid rgba(255,255,255,0.05);">
    <div style="width: 120px; height: 120px; border-radius: 50%; background-color: #333; margin: 0 auto 1.5rem auto; display: flex; align-items: center; justify-content: center; overflow: hidden; border: 2px solid var(--color-accent);">
      <img src="../assets/images/team/mohsin.webp" alt="Mohsin Alam - Game Designer" style="width: 100%; height: 100%; object-fit: cover;" loading="lazy">
    </div>
    <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">Mohsin Alam</h3>
    <div class="text-accent" style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">Game Designer</div>
    <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">Architects engaging gameplay loops and systems, ensuring every interaction feels intuitive and rewarding.</p>
    <a href="https://www.linkedin.com/in/mohsin-alam-unity/" target="_blank" rel="noopener noreferrer" style="display: inline-block; color: #fff; opacity: 0.6; transition: opacity 0.2s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.6'">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
    </a>
  </div>

  <!-- Team Member 2 -->
  <div class="card" style="background-color: #1a1a1a; padding: 2rem; border-radius: 8px; text-align: center; border: 1px solid rgba(255,255,255,0.05);">
    <div style="width: 120px; height: 120px; border-radius: 50%; background-color: #333; margin: 0 auto 1.5rem auto; display: flex; align-items: center; justify-content: center; overflow: hidden; border: 2px solid var(--color-accent);">
      <img src="../assets/images/team/ayush.webp" alt="Ayush Jha - Game Developer" style="width: 100%; height: 100%; object-fit: cover;" loading="lazy">
    </div>
    <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">Ayush Jha</h3>
    <div class="text-accent" style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">Game Developer</div>
    <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">Specializes in C# development, building robust mechanics and optimized architecture for seamless performance.</p>
    <a href="https://www.linkedin.com/in/ayush-jha-9bb65821a/" target="_blank" rel="noopener noreferrer" style="display: inline-block; color: #fff; opacity: 0.6; transition: opacity 0.2s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.6'">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
    </a>
  </div>

  <!-- Team Member 3 -->
  <div class="card" style="background-color: #1a1a1a; padding: 2rem; border-radius: 8px; text-align: center; border: 1px solid rgba(255,255,255,0.05);">
    <div style="width: 120px; height: 120px; border-radius: 50%; background-color: #333; margin: 0 auto 1.5rem auto; display: flex; align-items: center; justify-content: center; overflow: hidden; border: 2px solid var(--color-accent);">
      <img src="../assets/images/team/abhinav.webp" alt="Abhinav Rathore - Marketing Strategist" style="width: 100%; height: 100%; object-fit: cover;" loading="lazy">
    </div>
    <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">Abhinav Rathore</h3>
    <div class="text-accent" style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">Marketing Strategist</div>
    <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">Drives user acquisition and brand growth through data-driven campaigns and market positioning.</p>
    <a href="https://www.linkedin.com/in/rathoreabhinav0/" target="_blank" rel="noopener noreferrer" style="display: inline-block; color: #fff; opacity: 0.6; transition: opacity 0.2s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.6'">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
    </a>
  </div>

  <!-- Team Member 4 -->
  <div class="card" style="background-color: #1a1a1a; padding: 2rem; border-radius: 8px; text-align: center; border: 1px solid rgba(255,255,255,0.05);">
    <div style="width: 120px; height: 120px; border-radius: 50%; background-color: #333; margin: 0 auto 1.5rem auto; display: flex; align-items: center; justify-content: center; overflow: hidden; border: 2px solid var(--color-accent);">
      <img src="../assets/images/team/rohit.webp" alt="Rohit Rathore - SEO Specialist" style="width: 100%; height: 100%; object-fit: cover;" loading="lazy">
    </div>
    <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">Rohit Rathore</h3>
    <div class="text-accent" style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">SEO Specialist</div>
    <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">Optimizes digital visibility and search engine performance to maximize organic reach and engagement.</p>
    <a href="https://www.linkedin.com/in/rohit-kumar-singh-0aa2b2233/" target="_blank" rel="noopener noreferrer" style="display: inline-block; color: #fff; opacity: 0.6; transition: opacity 0.2s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.6'">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
    </a>
  </div>

</div>
</div>
</section>
"""

# Regex to replace the old Meet the Team block
content = re.sub(r'<!-- Meet the Team -->.*?(?=<!-- Core Disciplines -->)', team_html + "\n", content, flags=re.DOTALL)

# Update Person schema
person_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "DualCore Games Team",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Person",
        "name": "Mohsin Alam",
        "jobTitle": "Game Designer",
        "worksFor": {
          "@type": "Organization",
          "name": "DualCore Games"
        },
        "description": "Architects engaging gameplay loops and systems, ensuring every interaction feels intuitive and rewarding.",
        "sameAs": "https://www.linkedin.com/in/mohsin-alam-unity/"
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Person",
        "name": "Ayush Jha",
        "jobTitle": "Game Developer",
        "worksFor": {
          "@type": "Organization",
          "name": "DualCore Games"
        },
        "description": "Specializes in C# development, building robust mechanics and optimized architecture for seamless performance.",
        "sameAs": "https://www.linkedin.com/in/ayush-jha-9bb65821a/"
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@type": "Person",
        "name": "Abhinav Rathore",
        "jobTitle": "Marketing Strategist",
        "worksFor": {
          "@type": "Organization",
          "name": "DualCore Games"
        },
        "description": "Drives user acquisition and brand growth through data-driven campaigns and market positioning.",
        "sameAs": "https://www.linkedin.com/in/rathoreabhinav0/"
      }
    },
    {
      "@type": "ListItem",
      "position": 4,
      "item": {
        "@type": "Person",
        "name": "Rohit Rathore",
        "jobTitle": "SEO Specialist",
        "worksFor": {
          "@type": "Organization",
          "name": "DualCore Games"
        },
        "description": "Optimizes digital visibility and search engine performance to maximize organic reach and engagement.",
        "sameAs": "https://www.linkedin.com/in/rohit-kumar-singh-0aa2b2233/"
      }
    }
  ]
}
</script>
"""

content = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema\.org",\s*"@type": "ItemList",\s*"name": "DualCore Games Team".*?</script>', person_schema, content, flags=re.DOTALL)

with open("about/index.html", "w") as f:
    f.write(content)
    
print("Updated team HTML and schema.")
