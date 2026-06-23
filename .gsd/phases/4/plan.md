---
phase: 4
plan: 1
wave: 1
gap_closure: false
---

# Plan 4.1: Mobile Performance & Responsiveness Refinement

## Objective
Optimize mobile load times, improve visual presentation, ensure safe overflow behavior, and resolve navigation layout issues across all pages.

## Context
Load these files for context:
- .gsd/SPEC.md
- .gsd/ROADMAP.md
- .gsd/TODO.md
- index.html
- assets/css/style.css
- assets/js/main.js

## Tasks

<task type="auto">
  <name>De-duplicate / disable video on mobile and set static WebP background</name>
  <files>
    index.html
  </files>
  <action>
    Update index.html's video tag and inline script. If isMobile is detected, remove the video tag from the DOM entirely and set assets/images/hero_mobile_poster.webp as the background-image on the parent container (.hero-video-bg). This prevents mobile devices from downloading or decoding the MP4 stream, improving performance.
  </action>
  <verify>
    Check index.html source code and verify the dynamic script behavior.
  </verify>
  <done>
    On mobile viewports, the video tag is removed from the DOM and hero-video-bg displays hero_mobile_poster.webp.
  </done>
</task>

<task type="auto">
  <name>Convert heavy PNGs in assets/images/ to WebP and update references</name>
  <files>
    assets/images/about-engine-schematic.png
    assets/images/about-hero-bg.png
    assets/images/contact-hero-bg.png
    assets/images/service-gameart-schematic.png
    assets/images/service-gamedev-schematic.png
    assets/images/service-vrxr-schematic.png
    assets/images/services-hero-bg.png
    about/index.html
    blog/index.html
    contact/index.html
    services/index.html
    work/index.html
  </files>
  <action>
    1. Run a Python script using Pillow to convert the 7 high-res PNG images in assets/images/ to WebP.
    2. Replace all occurrences of these PNG references with WebP inside HTML files.
  </action>
  <verify>
    Verify that the WebP versions are generated, are significantly smaller than the PNG versions, and are referenced in the HTML pages.
  </verify>
  <done>
    No references to the 7 original PNG files remain in the HTML files and WebP images display correctly on the pages.
  </done>
</task>

<task type="auto">
  <name>Enforce layout overflow safety and mobile meta-grid 1-column stack</name>
  <files>
    assets/css/style.css
  </files>
  <action>
    1. Ensure html and body have overflow-x: hidden and width: 100% on small screens.
    2. Add global override for .cs-meta-grid under @media (max-width: 576px) to stack into a single column: grid-template-columns: 1fr !important.
  </action>
  <verify>
    Verify CSS rules in assets/css/style.css.
  </verify>
  <done>
    CSS files contain rules for overflow protection and column stacking on mobile viewports.
  </done>
</task>

<task type="auto">
  <name>Audit mobile navbar toggles and close button positioning</name>
  <files>
    assets/css/style.css
    assets/js/main.js
  </files>
  <action>
    Review close button positioning and clickable area dimensions (minimum 48x48px touch targets) on mobile viewports. Ensure that user click actions are not blocked.
  </action>
  <verify>
    Inspect CSS rule for .nav-close and check main.js for click event handlers.
  </verify>
  <done>
    Close button on mobile has clear styling, proper z-index, and at least 48x48px interactive target size.
  </done>
</task>

## Must-Haves
After all tasks complete, verify:
- [ ] Homepage hero video does not load or run on mobile viewports.
- [ ] HTML pages have clean URLs resolving to WebP images instead of PNG.
- [ ] Horizontal overflow is completely prevented on mobile.
- [ ] Mobile navigation close button functions perfectly.

## Success Criteria
- [ ] All tasks verified passing
- [ ] Must-haves confirmed
- [ ] No layout shifts or link regressions
