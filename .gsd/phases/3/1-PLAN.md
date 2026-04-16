---
phase: 3
plan: 1
wave: 1
---

# Plan 3.1: Link and Form Verification

## Objective
Ensure all interactive elements on the newly elevated Reclairos pages are functional and correctly link to their technical/narrative counterparts.

## Context
- .gsd/SPEC.md
- work/game-development/reclairos/overview/index.html
- work/game-development/reclairos/case-study/index.html

## Tasks

<task type="auto">
  <name>Link Verification</name>
  <files>
    work/game-development/reclairos/overview/index.html
    work/game-development/reclairos/case-study/index.html
  </files>
  <action>
    Manual/Scripted check of all <a> tags to ensure they resolve to valid pages.
    - Hero button (#beta-form)
    - Case Study button (../case-study/index.html)
    - Global Contact button (../../../../contact.html)
    - Footer links
  </action>
  <verify>grep -E 'href="[^#].*"' work/game-development/reclairos/overview/index.html</verify>
  <done>All hrefs point to existent local files or valid IDs.</done>
</task>

<task type="auto">
  <name>Form Configuration Audit</name>
  <files>work/game-development/reclairos/overview/index.html</files>
  <action>
    Verify that the 'project' field in the Beta form is set specifically to "Reclairos Private Beta" to ensure correct routing in the Google Apps Script.
  </action>
  <verify>grep 'name="project" value="Reclairos Private Beta"' work/game-development/reclairos/overview/index.html</verify>
  <done>Form correctly identifies the project source for lead capture.</done>
</task>

## Success Criteria
- [ ] 100% of links on Reclairos pages are functional.
- [ ] Beta form identifies itself as "Reclairos Private Beta".
