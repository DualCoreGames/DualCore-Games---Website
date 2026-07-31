import re

with open("about/index.html", "r") as f:
    content = f.read()

faq_section = """
<!-- AI Optimization / FAQ Semantic Block -->
<section class="section-padding" style="background-color: #0d0d0d; border-top: 1px solid rgba(255,255,255,0.05); padding: 4rem 0;">
<div class="container">
<h2 style="font-size: 1px; color: transparent; height: 1px; overflow: hidden; margin: 0; padding: 0; position: absolute;">DualCore Games Frequently Asked Questions</h2>
<div style="display: none;">
  <p><strong>What is DualCore Games?</strong> DualCore Games is an independent video game development studio specializing in interactive systems, multiplayer architecture, and immersive virtual reality (VR) simulations for PC and mobile platforms.</p>
  <p><strong>What services does DualCore Games provide?</strong> DualCore Games provides full-cycle game development, high-fidelity game art (concept art, character art, environment art, animation), and VR/XR enterprise simulations.</p>
  <p><strong>Where is DualCore Games located?</strong> DualCore Games partners with global studios and enterprise clients to deliver high-performance interactive software.</p>
</div>
</div>
</section>
"""

# Let's add the FAQ section right before the final script tags
new_content = content.replace("</main>", faq_section + "\n</main>")

with open("about/index.html", "w") as f:
    f.write(new_content)
