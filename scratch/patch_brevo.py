import sys

file_path = "/Users/abhinav/.gemini/antigravity/brain/a1c62e40-a978-44fe-ba54-2d82bc59340c/google_apps_script_updated.js"
with open(file_path, "r") as f:
    content = f.read()

old_payload = """        var brevoPayload = JSON.stringify({
          "email":      email,
          "firstName":  data.name || "",
          "listIds":    [listId],
          "attributes": {
            "FORM_TYPE":   formType,
            "SOURCE_PAGE": sourcePage,
            "PLATFORM":    data.platform || ""
          },
          "updateEnabled": true
        });"""

new_payload = """        var brevoPayload = JSON.stringify({
          "email":         email,
          "listIds":       [listId],
          "updateEnabled": true
        });"""

content = content.replace(old_payload, new_payload)

with open(file_path, "w") as f:
    f.write(content)
