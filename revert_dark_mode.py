
import os

BASE = r"C:\Users\ashish kumar\Downloads\new web"

# 1. Write Favicon
FAVICON_SVG = """<svg viewBox="0 0 38 38" fill="#0044FF" xmlns="http://www.w3.org/2000/svg">
  <path d="M4 6C4 4.895 4.895 4 6 4H24C25.105 4 26 4.895 26 6V15H16C14.895 15 14 15.895 14 17V26H6C4.895 26 4 25.105 4 24V6Z"/>
  <rect x="17" y="17" width="17" height="9" rx="2"/>
  <circle cx="10" cy="32" r="4"/>
  <circle cx="24" cy="32" r="4"/>
</svg>"""
with open(os.path.join(BASE, "images", "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(FAVICON_SVG)

# 2. Update index.html
with open(os.path.join(BASE, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# Remove Dark Mode button
DARK_BTN = """<button class="nav-search-btn" id="themeToggle" aria-label="Toggle dark mode">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" id="themeIcon">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
      </button>\n      """
html = html.replace(DARK_BTN, "")

# Add favicon if not exists
if "favicon.svg" not in html:
    html = html.replace(
        '<link rel="stylesheet" href="styles.css">',
        '<link rel="icon" type="image/svg+xml" href="images/favicon.svg">\n  <link rel="stylesheet" href="styles.css">'
    )

with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

# 3. Update styles.css
with open(os.path.join(BASE, "styles.css"), "r", encoding="utf-8") as f:
    css = f.read()

dark_start = css.find("/* ============================================================\n   DARK THEME")
if dark_start != -1:
    css = css[:dark_start]
    with open(os.path.join(BASE, "styles.css"), "w", encoding="utf-8") as f:
        f.write(css)

# 4. Update main.js
with open(os.path.join(BASE, "main.js"), "r", encoding="utf-8") as f:
    js = f.read()

dark_js_start = js.find("// ============================================================\n// DARK MODE TOGGLE")
if dark_js_start != -1:
    js = js[:dark_js_start]
    with open(os.path.join(BASE, "main.js"), "w", encoding="utf-8") as f:
        f.write(js)

print("Dark mode removed and favicon added successfully.")
