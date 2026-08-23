import re

with open('reclairos/index.html', 'r') as f:
    html = f.read()

# We want to remove the duplicated FAQ accordion trigger from the second script block.
# Actually, let's remove everything from "// FAQ Accordion Trigger" down to the end of the script block (before the `});` of DOMContentLoaded) in the second block.

# The second block starts around line 4214
# We can find the second "// FAQ Accordion Trigger" and delete from there to the end of that block.
# Wait, let's just delete the exact duplicate string for the FAQ trigger.

faq_logic_pattern = r"// FAQ Accordion Trigger.*?item\.style\.borderColor = 'rgba\(0, 209, 255, 0\.2\)';\s*}\s*}\);\s*}\);"

# Wait, it's safer to use a function
def remove_duplicate_faq(text):
    # Find all occurrences
    parts = text.split("// FAQ Accordion Trigger")
    if len(parts) == 3:
        # parts[0] is everything before the first one
        # parts[1] is the first script's remainder
        # parts[2] is the second script's remainder
        
        # Let's find where parts[2] ends (the Interactive Lore Tabs Trigger)
        lore_idx = parts[2].find("// Interactive Lore Tabs Trigger")
        if lore_idx != -1:
            # We remove from the beginning of parts[2] up to lore_idx
            parts[2] = parts[2][lore_idx:]
        else:
            print("Lore tabs not found in second block")
            return text
            
        # Rejoin
        return parts[0] + "// FAQ Accordion Trigger" + parts[1] + parts[2]
    else:
        print("Expected 2 occurrences, found", len(parts) - 1)
        return text

html = remove_duplicate_faq(html)

with open('reclairos/index.html', 'w') as f:
    f.write(html)
