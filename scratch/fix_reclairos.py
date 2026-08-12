import sys

def main():
    filepath = "reclairos/index.html"
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    # Extract the beta form lines (4157 to 4200 - 1-indexed)
    form_lines = lines[4156:4200]
    
    # Check if we got the right lines
    if "PRIVATE BETA FORM" not in form_lines[0]:
        print("Error: Line mismatch for form start.")
        sys.exit(1)
        
    # Remove the second </div><!-- /tab-casestudy --> (line 4778)
    if "<!-- /tab-casestudy -->" in lines[4777]:
        lines[4777] = "" # Delete it
    else:
        print("Warning: Line 4778 is not the closing tab-casestudy div. Found: " + lines[4777].strip())
        
    # Remove the form from its original location
    for i in range(4156, 4200):
        lines[i] = ""
        
    # Insert the form before line 4097 (index 4096)
    if "<!-- /tab-casestudy -->" in lines[4096]:
        lines = lines[:4096] + form_lines + lines[4096:]
    else:
        print("Error: Line 4097 is not the first closing tab-casestudy div. Found: " + lines[4096].strip())
        sys.exit(1)
        
    with open(filepath, 'w') as f:
        f.writelines(lines)
        
    print("Fix applied successfully.")
    
if __name__ == "__main__":
    main()
