# Phase 1 Plan: Core Navigation & Global Stability

> **Status**: `DRAFT`

## Objective
Establish a stable mobile foundation by fixing global layout overflow, refining the mobile navigation menu, and standardizing touch-friendly components like breadcrumbs.

## Requirements
- **REQ-02**: Fix mobile menu 'X' button positioning (min 44px tap target).
- **REQ-03**: Eliminate horizontal scrolling via `overflow-x: hidden` and container audit.
- **REQ-06**: Standardize breadcrumb link sizes for touch.

## Execution Steps
1. **Global Overflow Audit**:
   - Inspect `index.css` and `body` styles.
   - Use `* { outline: 1px solid red !important; }` in a temporary debug session to find elements leaking out of the viewport.
   - Apply `overflow-x: hidden` to `html, body`.

2. **Mobile Menu Refinement**:
   - Locate mobile menu close button in CSS/JS.
   - Adjust positioning for safe areas (iOS notches, etc.) and increase tap target.
   - Ensure the menu overlay is stable and doesn't scroll the background.

3. **Breadcrumb Standardization**:
   - Audit `work/` and sub-pages for breadcrumb implementation.
   - Apply consistent padding and font-size for mobile.

4. **Verification**:
   - Test on iPhone/Android emulators.
   - Ensure zero horizontal scroll on all main pages.

## Verification Criteria
- [ ] No horizontal scrollbars visible on Home, About, Work, or Project pages.
- [ ] Mobile menu close button is accessible and has correct spacing.
- [ ] Breadcrumbs are easily tappable with no overlap.
