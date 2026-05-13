# Phase 2 Plan: Homepage Hero & Media Optimization

> **Status**: `DRAFT`

## Objective
Ensure the homepage hero video displays correctly on mobile devices, providing a premium "Systems-First" introduction without layout breaks or loading issues.

## Requirements
- **REQ-01**: Homepage Hero Video must autoplay (muted) and scale to cover the mobile viewport without distortion.

## Execution Steps
1. **Hero Video Audit**:
   - Inspect `index.html` hero section.
   - Check if the video tag has `playsinline`, `autoplay`, `muted`, and `loop`.
   - Verify the `poster` image is set for fallback.

2. **CSS Refinement**:
   - Locate `.hero-video` and `.hero-video-bg` in `style.css`.
   - Use `object-fit: cover` and ensure `width: 100%`, `height: 100%`.
   - Adjust the `transform: translate(-50%, -50%)` if it's causing framing issues on narrow viewports.

3. **Fallback & Performance**:
   - Ensure a high-quality static image displays if the video fails to load or is on a low-power mobile mode.

4. **Verification**:
   - Test on iOS (Safari) and Android (Chrome) emulators.
   - Confirm video fills the screen and text remains readable.

## Verification Criteria
- [ ] Hero video autoplays on mobile devices.
- [ ] Video correctly fills the container (`object-fit: cover`).
- [ ] No blank space or broken icons in the hero background.
