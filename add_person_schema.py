import re

with open("about/index.html", "r") as f:
    content = f.read()

# We need to find where the schemas are located and add a Person schema array
# The about page already has a breadcrumb and organization schema.
# Let's just append this before the closing </head> tag or alongside the other schemas.

person_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "DualCore Games Team",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Person",
        "name": "[Team Member 1 Name]",
        "jobTitle": "[Team Member 1 Role]",
        "worksFor": {
          "@type": "Organization",
          "name": "DualCore Games"
        },
        "description": "[Team Member 1 Bio]",
        "sameAs": "[Team Member 1 LinkedIn URL]"
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Person",
        "name": "[Team Member 2 Name]",
        "jobTitle": "[Team Member 2 Role]",
        "worksFor": {
          "@type": "Organization",
          "name": "DualCore Games"
        },
        "description": "[Team Member 2 Bio]",
        "sameAs": "[Team Member 2 LinkedIn URL]"
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@type": "Person",
        "name": "[Team Member 3 Name]",
        "jobTitle": "[Team Member 3 Role]",
        "worksFor": {
          "@type": "Organization",
          "name": "DualCore Games"
        },
        "description": "[Team Member 3 Bio]",
        "sameAs": "[Team Member 3 LinkedIn URL]"
      }
    }
  ]
}
</script>
"""

if "DualCore Games Team" not in content:
    # Insert it before the closing </head> tag
    new_content = content.replace("</head>", person_schema + "\n</head>")
    with open("about/index.html", "w") as f:
        f.write(new_content)
    print("Person schema added successfully.")
else:
    print("Person schema already exists.")
