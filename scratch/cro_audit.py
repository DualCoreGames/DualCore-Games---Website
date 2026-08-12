import re

with open('about/index.html', 'r') as f:
    content = f.read()

# Replace the "Final CTA" and "AI Optimization" sections with a visual FAQ and unified lead capture.
new_cro_section = """<!-- Frequently Asked Questions -->
<section class="section-padding" style="background-color: var(--color-bg); border-top: 1px solid rgba(255,255,255,0.05);">
<div class="container" style="max-width: 800px;">
<div style="text-align: center; margin-bottom: 3rem;">
  <h2 style="margin-bottom: 1rem; font-size: clamp(2rem, 4vw, 2.5rem);">Frequently Asked Questions</h2>
  <p class="text-muted" style="font-size: 1.15rem;">Everything you need to know about partnering with us.</p>
</div>
<div class="faq-list">
  <div class="faq-item" style="border-bottom: 1px solid rgba(255,255,255,0.1); padding: 1.5rem 0; cursor: pointer;">
    <div class="faq-question" aria-expanded="false" style="display: flex; justify-content: space-between; align-items: center; font-weight: 700; font-size: 1.25rem;">
      What is DualCore Games?
      <span class="faq-icon" style="color: var(--color-accent); font-size: 1.5rem;">+</span>
    </div>
    <div class="faq-answer" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
      <p class="text-muted" style="margin-top: 1rem; line-height: 1.7;">DualCore Games is an independent video game development studio specializing in interactive systems, multiplayer architecture, and immersive virtual reality (VR) simulations for PC and mobile platforms.</p>
    </div>
  </div>
  <div class="faq-item" style="border-bottom: 1px solid rgba(255,255,255,0.1); padding: 1.5rem 0; cursor: pointer;">
    <div class="faq-question" aria-expanded="false" style="display: flex; justify-content: space-between; align-items: center; font-weight: 700; font-size: 1.25rem;">
      What services does DualCore Games provide?
      <span class="faq-icon" style="color: var(--color-accent); font-size: 1.5rem;">+</span>
    </div>
    <div class="faq-answer" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
      <p class="text-muted" style="margin-top: 1rem; line-height: 1.7;">DualCore Games provides full-cycle game development, high-fidelity game art (concept art, character art, environment art, animation), and VR/XR enterprise simulations.</p>
    </div>
  </div>
  <div class="faq-item" style="border-bottom: 1px solid rgba(255,255,255,0.1); padding: 1.5rem 0; cursor: pointer;">
    <div class="faq-question" aria-expanded="false" style="display: flex; justify-content: space-between; align-items: center; font-weight: 700; font-size: 1.25rem;">
      Where is DualCore Games located?
      <span class="faq-icon" style="color: var(--color-accent); font-size: 1.5rem;">+</span>
    </div>
    <div class="faq-answer" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
      <p class="text-muted" style="margin-top: 1rem; line-height: 1.7;">DualCore Games partners with global studios and enterprise clients worldwide to deliver high-performance interactive software, with remote integration capabilities.</p>
    </div>
  </div>
</div>
</div>
</section>

</main>
<!-- Unified Lead Capture Section -->
<section class="section-padding" style="background-color: var(--color-bg); border-top: 1px solid rgba(255,255,255,0.05); text-align: center;">
<div class="container" style="max-width: 600px;">
<div style="margin-bottom: 3rem;">
<h2 style="margin-bottom: 1rem; font-size: clamp(2rem, 4vw, 3rem);">Let’s Build Systems That Last.</h2>
<p class="text-muted" style="margin-bottom: 2rem; font-size: 1.15rem; line-height: 1.6;">If you are developing a scalable game, immersive simulation, or production-ready interactive system, we’re ready to architect it with you.</p>
</div>
<form action="https://script.google.com/macros/s/AKfycbzoije_tJBOEAofZS25gWx2Ge65ky5n0d8Uh-rWZN3tjtRHkTxYLnid8UUOKouhmm8/exec" method="POST" class="contact-form" id="contactForm" style="text-align: left;">
          <!-- Honeypot Field for Anti-Spam -->
          <div style="display: none;" aria-hidden="true">
            <input type="text" name="honeypot_field" tabindex="-1" autocomplete="off">
          </div>
<div class="form-group">
<label for="name">Full Name</label>
<input id="name" name="name" placeholder="John Doe" required="" type="text"/>
</div>
<div class="form-group">
<label for="email">Email Address</label>
<input id="email" name="email" placeholder="john@example.com" required="" type="email"/>
</div>
<div class="form-group">
<label for="project">Project Type</label>
<input id="project" name="project" placeholder="e.g. Mobile Game, Engine Optimization" required="" type="text"/>
</div>
<div class="form-group">
<label for="message">Message</label>
<textarea id="message" name="message" placeholder="Briefly describe your requirements..." required=""></textarea>
</div>
<button class="btn btn-primary" style="width: 100%; font-size: 1.1rem; padding: 16px; font-weight: 700;" type="submit">Discuss My Project</button>
<p style="font-size: 0.8rem; color: var(--color-text-muted); margin-top: 1.5rem; text-align: center;">
By submitting this form, you agree to our Privacy Policy. Our engineering team typically responds within 24-48 hours.
</p>
</form>
</div>
</section>
"""

start_str = "<!-- Final CTA -->"
end_str = "<!-- Unified Footer -->"

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_cro_section + content[end_idx:]
    with open('about/index.html', 'w') as f:
        f.write(new_content)
    print("Successfully injected CRO changes.")
else:
    print("Could not find start or end tags.")
