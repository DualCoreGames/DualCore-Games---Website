import re

with open("about/index.html", "r") as f:
    content = f.read()

team_section = """
<!-- Meet the Team -->
<section class="section-padding" style="background-color: var(--color-bg); border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
<div class="container">
<h2 style="text-align: center; margin-bottom: 4rem; font-size: clamp(2rem, 4vw, 3rem);">Meet the Team</h2>
<div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
  
  <!-- Team Member 1 -->
  <div class="card" style="background-color: #1a1a1a; padding: 2rem; border-radius: 8px; text-align: center; border: 1px solid rgba(255,255,255,0.05);">
    <div style="width: 120px; height: 120px; border-radius: 50%; background-color: #333; margin: 0 auto 1.5rem auto; display: flex; align-items: center; justify-content: center; overflow: hidden; border: 2px solid var(--color-accent);">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
    </div>
    <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">[Team Member Name]</h3>
    <div class="text-accent" style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">[Role / Title]</div>
    <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">[Brief 1-2 sentence bio outlining their specific expertise in game development or production.]</p>
    <a href="#" style="display: inline-block; color: #fff; opacity: 0.6; transition: opacity 0.2s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.6'">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
    </a>
  </div>

  <!-- Team Member 2 -->
  <div class="card" style="background-color: #1a1a1a; padding: 2rem; border-radius: 8px; text-align: center; border: 1px solid rgba(255,255,255,0.05);">
    <div style="width: 120px; height: 120px; border-radius: 50%; background-color: #333; margin: 0 auto 1.5rem auto; display: flex; align-items: center; justify-content: center; overflow: hidden; border: 2px solid var(--color-accent);">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
    </div>
    <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">[Team Member Name]</h3>
    <div class="text-accent" style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">[Role / Title]</div>
    <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">[Brief 1-2 sentence bio outlining their specific expertise in game development or production.]</p>
    <a href="#" style="display: inline-block; color: #fff; opacity: 0.6; transition: opacity 0.2s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.6'">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
    </a>
  </div>

  <!-- Team Member 3 -->
  <div class="card" style="background-color: #1a1a1a; padding: 2rem; border-radius: 8px; text-align: center; border: 1px solid rgba(255,255,255,0.05);">
    <div style="width: 120px; height: 120px; border-radius: 50%; background-color: #333; margin: 0 auto 1.5rem auto; display: flex; align-items: center; justify-content: center; overflow: hidden; border: 2px solid var(--color-accent);">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
    </div>
    <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">[Team Member Name]</h3>
    <div class="text-accent" style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">[Role / Title]</div>
    <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">[Brief 1-2 sentence bio outlining their specific expertise in game development or production.]</p>
    <a href="#" style="display: inline-block; color: #fff; opacity: 0.6; transition: opacity 0.2s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.6'">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
    </a>
  </div>

</div>
</div>
</section>
"""

new_content = content.replace("<!-- Core Disciplines -->", team_section + "\n<!-- Core Disciplines -->")

with open("about/index.html", "w") as f:
    f.write(new_content)
