with open("reclairos/index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx_main = content.find("<main>")
idx_first_div = content.find("<div", idx_main)

first_class = ""
if idx_first_div != -1:
    idx_class = content.find("class=", idx_first_div)
    if idx_class != -1 and idx_class < content.find(">", idx_first_div):
        first_class = content[idx_class:idx_class+40]
print("First div inside main:", first_class)

idx_overview = content.find('<div id="tab-overview"')
if idx_overview != -1:
    idx_hero = content.find('<section class="rc-hero">', idx_overview)
    idx_snap = content.find('<section class="rc-snapshot">', idx_overview)
    idx_casestudy = content.find('<div id="tab-casestudy"', idx_overview)
    
    if idx_hero != -1 and idx_hero < idx_casestudy:
        print("rc-hero found inside tab-overview block!")
    else:
        print("rc-hero NOT found inside tab-overview")
        
    if idx_snap != -1 and idx_snap < idx_casestudy:
        print("rc-snapshot found inside tab-overview block!")
    else:
        print("rc-snapshot NOT found inside tab-overview")
        
btn_str = "View Game Overview"
if btn_str in content:
    print("ERROR: View Game Overview button still exists")
else:
    print("View Game Overview button successfully removed")
