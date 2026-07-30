import sys

with open("reclairos/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Markers
hero_start = '<!-- ═══ HERO — Full-Bleed Cinematic ═══ -->'
hero_end = '</section>\n\n    <!-- ═══ PROJECT SNAPSHOT ═══ -->'
if hero_end not in content:
    hero_end = '</section>' # fallback

snap_start = '<!-- ═══ PROJECT SNAPSHOT ═══ -->'
snap_end_str = '</section>\n\n    <!-- ═══ ELITE SQUAD ROSTER ═══ -->'

tab_container_start = '<!-- ── Mega Tab Navigation ── -->'
tab_container_end = '</div>\n  </div>\n'
overview_start = '<div id="tab-overview" class="mega-tab-content active">'

# Find hero block
idx_h_start = content.find(hero_start)
idx_h_end = content.find('</section>', idx_h_start) + len('</section>\n')

# Find snap block
idx_s_start = content.find(snap_start)
idx_s_end = content.find('</section>', idx_s_start) + len('</section>\n')

# Find tab block
idx_t_start = content.find(tab_container_start)
idx_t_end = content.find('  </div>\n  </div>\n', idx_t_start) + len('  </div>\n  </div>\n')
# Just in case, the tab container ends right before overview_start
idx_o_start = content.find(overview_start)
if idx_t_end > idx_o_start:
    idx_t_end = idx_o_start

if -1 in (idx_h_start, idx_h_end, idx_s_start, idx_s_end, idx_t_start, idx_t_end, idx_o_start):
    print("Could not find all markers.")
    sys.exit(1)

# Extract substrings
hero_str = content[idx_h_start:idx_h_end]
snap_str = content[idx_s_start:idx_s_end]
tab_str = content[idx_t_start:idx_t_end]

# Remove them from content starting from the back to preserve earlier indices
content = content[:idx_t_start] + content[idx_t_end:]
content = content[:idx_s_start] + content[idx_s_end:]
content = content[:idx_h_start] + content[idx_h_end:]

# Now re-insert
# 1. mega-tabs-container right after <main>
main_tag = '<main>'
idx_m = content.find(main_tag) + len(main_tag) + 1
content = content[:idx_m] + tab_str + '\n' + content[idx_m:]

# 2. hero_str and snap_str right after overview_start
# overview_start index has changed due to above insertions/removals
idx_o = content.find(overview_start) + len(overview_start) + 1
content = content[:idx_o] + hero_str + '\n' + snap_str + '\n' + content[idx_o:]

# 3. Remove "← View Game Overview" button from Case Study
btn_str = '<a href="javascript:void(0)" onclick="window.switchTab(\'overview\')" class="btn btn-secondary" style="padding: 0.85rem 2rem; font-weight: 600; background: transparent; border: 1px solid rgba(255,255,255,0.15);">← View Game Overview</a>'
content = content.replace(btn_str, '')

with open("reclairos/index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated HTML using precise string slicing")
