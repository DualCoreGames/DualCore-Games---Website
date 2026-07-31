with open("about/index.html", "r") as f:
    content = f.read()

start_marker = "<!-- Production Experience -->"
end_marker = "<!-- Team Member 1 -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_sections = """<!-- Production Experience -->
<style>
  .bento-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 3rem;
  }
  @media (min-width: 768px) {
    .bento-grid {
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: auto auto;
    }
    .bento-large {
      grid-column: span 2;
    }
  }
  .bento-card {
    background: linear-gradient(145deg, #161a22 0%, #0d1117 100%);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 2.5rem;
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .bento-card:hover {
    transform: translateY(-5px);
    border-color: rgba(0, 210, 255, 0.4);
    box-shadow: 0 15px 35px rgba(0, 210, 255, 0.1);
  }
  .bento-number {
    font-size: 3.5rem;
    font-weight: 900;
    background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    line-height: 1;
  }
  .philosophy-glass {
    background: rgba(20, 25, 35, 0.6);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 3rem;
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
  }
  .operate-card {
    background: #111;
    border-radius: 12px;
    padding: 2.5rem;
    position: relative;
    overflow: hidden;
    transition: all 0.4s ease;
    border: 1px solid rgba(255,255,255,0.05);
    z-index: 1;
  }
  .operate-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at center, rgba(255, 122, 24, 0.15) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.4s ease;
    z-index: -1;
  }
  .operate-card:hover {
    border-color: rgba(255, 122, 24, 0.4);
    transform: translateY(-5px);
  }
  .operate-card:hover::before {
    opacity: 1;
  }
  .team-grid-container {
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    gap: 2rem;
  }
  @media (min-width: 640px) {
    .team-grid-container { grid-template-columns: repeat(2, 1fr); }
  }
  @media (min-width: 1024px) {
    .team-grid-container { grid-template-columns: repeat(4, 1fr); }
  }
  .team-card {
    background-color: #1a1a1a;
    padding: 2.5rem 1.5rem;
    border-radius: 12px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.05);
    transition: transform 0.3s ease, border-color 0.3s ease;
  }
  .team-card:hover {
    transform: translateY(-8px) scale(1.02);
    border-color: var(--color-accent);
  }
</style>

<section class="section-padding" style="background-color: #05070a; border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05); position: relative; overflow: hidden;">
<div style="position: absolute; top: -20%; left: -10%; width: 50%; height: 50%; background: radial-gradient(circle, rgba(0,210,255,0.05) 0%, transparent 70%); border-radius: 50%; z-index: 0;"></div>
<div class="container" style="position: relative; z-index: 1;">
  <div style="text-align: center; max-width: 800px; margin: 0 auto;">
    <h2 style="font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 800; letter-spacing: -0.02em; margin-bottom: 1rem;">Proven <span style="background: linear-gradient(90deg, #fff 0%, #888 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Scale</span></h2>
    <p class="text-muted" style="font-size: 1.15rem; line-height: 1.8;">Our experience spans commercial games, multiplayer systems, immersive simulations, and cross-platform deployments. We prioritize stability, scalability, and measurable performance.</p>
  </div>
  
  <div class="bento-grid">
    <div class="bento-card bento-large">
      <div class="bento-number">10+</div>
      <h3 style="font-size: 1.5rem; margin-bottom: 0.75rem;">Interactive Titles Launched</h3>
      <p class="text-muted" style="font-size: 1rem; line-height: 1.6; margin: 0;">Successfully deployed across major platforms including PC, Mobile, and high-fidelity VR systems.</p>
    </div>
    <div class="bento-card">
      <div class="bento-number" style="background: linear-gradient(90deg, #ff7a18 0%, #af002d 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">&lt;50ms</div>
      <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">Multiplayer Latency</h3>
      <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6; margin: 0;">Advanced SDK integrations (Photon) ensuring seamless global sync.</p>
    </div>
    <div class="bento-card">
      <div class="bento-number" style="font-size: 2.5rem; margin-bottom: 1rem; background: linear-gradient(90deg, #11998e 0%, #38ef7d 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Cross-Platform</div>
      <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">Unified Architecture</h3>
      <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6; margin: 0;">Single codebase scaling from high-end PC down to standalone Meta Quest.</p>
    </div>
    <div class="bento-card bento-large">
      <div class="bento-number" style="font-size: 2.5rem; margin-bottom: 1rem; color: #fff; -webkit-text-fill-color: #fff;">Production Pipelines</div>
      <h3 style="font-size: 1.5rem; margin-bottom: 0.75rem;">Structured CI/CD Workflows</h3>
      <p class="text-muted" style="font-size: 1rem; line-height: 1.6; margin: 0;">Automated build systems and strict QA validation ensuring 99.9% uptime for enterprise clients.</p>
    </div>
  </div>
</div>
</section>

<!-- Philosophy -->
<section class="section-padding" style="background-image: url('../assets/images/about-hero-bg.webp'); background-size: cover; background-position: center; background-attachment: fixed; position: relative;">
<div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(5, 7, 10, 0.85); z-index: 0;"></div>
<div class="container" style="position: relative; z-index: 1;">
  <div class="philosophy-split" style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
    <div class="philosophy-glass">
      <h2 style="font-size: clamp(2rem, 3.5vw, 2.75rem); font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem;">Engineering Meets<br><span class="text-accent">Creative Discipline</span></h2>
      <div style="width: 60px; height: 4px; background: var(--color-accent); margin-bottom: 2rem; border-radius: 2px;"></div>
      <p style="font-size: 1.15rem; line-height: 1.8; color: #e0e0e0; margin-bottom: 1.5rem;">At DualCore, creativity and engineering are developed in parallel.</p>
      <p style="font-size: 1.15rem; line-height: 1.8; color: #aaa; margin-bottom: 1.5rem;">We believe interactive systems succeed when technical architecture and artistic direction evolve together from day one. This reduces technical debt and improves production velocity.</p>
      <p style="font-size: 1.15rem; line-height: 1.8; color: #aaa; margin: 0;">Our work is defined by modular architecture, performance benchmarking, and transparent collaboration.</p>
    </div>
    <div style="display: flex; justify-content: center; position: relative;">
      <div style="position: absolute; inset: -20px; background: linear-gradient(45deg, rgba(0,210,255,0.2), rgba(255,122,24,0.2)); filter: blur(30px); border-radius: 50%; z-index: -1;"></div>
      <img src="../assets/images/about-engine-schematic.webp" alt="DualCore Game Engine Loop Schematic Blueprint" style="width: 100%; max-width: 550px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 25px 50px rgba(0,0,0,0.6);" loading="lazy">
    </div>
  </div>
</div>
</section>

<!-- How We Operate -->
<section class="section-padding" style="background-color: #0a0a0a; border-bottom: 1px solid rgba(255,255,255,0.05);">
<div class="container">
  <div style="text-align: center; margin-bottom: 4rem;">
    <h2 style="font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; margin-bottom: 1rem;">How We <span class="text-orange">Operate</span></h2>
    <p class="text-muted" style="font-size: 1.15rem; max-width: 600px; margin: 0 auto;">Our core pillars for delivering exceptional interactive software.</p>
  </div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2.5rem;">
    
    <div class="operate-card">
      <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--color-orange)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 1.5rem;"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
      <h3 style="font-size: 1.5rem; margin-bottom: 1rem; font-weight: 700;">Commercial Viability</h3>
      <p class="text-muted" style="line-height: 1.7; margin: 0;">We build systems that work under real-world conditions. From stable cross-platform performance to monetization-ready infrastructure.</p>
    </div>
    
    <div class="operate-card">
      <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--color-orange)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 1.5rem;"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
      <h3 style="font-size: 1.5rem; margin-bottom: 1rem; font-weight: 700;">Transparent Collaboration</h3>
      <p class="text-muted" style="line-height: 1.7; margin: 0;">We operate as a direct extension of our partners. Clear reporting, iterative deployment, and structured communication.</p>
    </div>
    
    <div class="operate-card">
      <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--color-orange)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 1.5rem;"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
      <h3 style="font-size: 1.5rem; margin-bottom: 1rem; font-weight: 700;">Production Discipline</h3>
      <p class="text-muted" style="line-height: 1.7; margin: 0;">We emphasize documentation, clean integration pipelines, and scalable backend architecture for long-term stability.</p>
    </div>
    
  </div>
</div>
</section>

<!-- Meet the Team -->
<section class="section-padding" style="background-color: var(--color-bg); border-bottom: 1px solid rgba(255,255,255,0.05);">
<div class="container">
<h2 style="text-align: center; margin-bottom: 4rem; font-size: clamp(2rem, 4vw, 3rem); font-weight: 800;">Meet the <span class="text-accent">Team</span></h2>
<div class="team-grid-container">
"""
    # Create the new content
    new_content = content[:start_idx] + new_sections + content[end_idx:]
    
    # Finally, replace class="card" with class="team-card" ONLY for the team members
    team_start = new_content.find("<!-- Team Member 1 -->")
    team_end = new_content.find("<!-- AI Optimization / FAQ Semantic Block -->")
    
    if team_start != -1 and team_end != -1:
        team_block = new_content[team_start:team_end]
        team_block = team_block.replace('class="card"', 'class="team-card"')
        new_content = new_content[:team_start] + team_block + new_content[team_end:]
    
    with open("about/index.html", "w") as f:
        f.write(new_content)
    print("About page successfully redesigned using exact string matching.")
else:
    print("Could not find start/end markers.")
