
import os, re

BASE = r"C:\Users\ashish kumar\Downloads\new web"

# ─────────────────────────────────────────
# 1. Update styles.css — brand color tokens
# ─────────────────────────────────────────
with open(os.path.join(BASE, "styles.css"), "r", encoding="utf-8") as f:
    css = f.read()

# Replace color token block at top of :root
old_colors = """:root {
  --blue-50:#eff6ff;--blue-100:#dbeafe;--blue-200:#bfdbfe;--blue-300:#93c5fd;--blue-400:#60a5fa;
  --blue-500:#3b82f6;--blue-600:#2563eb;--blue-700:#1d4ed8;--blue-800:#1e40af;--blue-900:#1e3a8a;
  --brand:#2563eb;--brand-dark:#1d4ed8;--brand-light:#eff6ff;--brand-subtle:#dbeafe;
  --white:#ffffff;--gray-50:#f8fafc;--gray-100:#f1f5f9;--gray-200:#e2e8f0;--gray-300:#cbd5e1;
  --gray-400:#94a3b8;--gray-500:#64748b;--gray-600:#475569;--gray-700:#334155;
  --gray-800:#1e293b;--gray-900:#0f172a;
  --text-primary:#0f172a;--text-secondary:#475569;--text-muted:#94a3b8;
  --border:#e2e8f0;--border-light:#f1f5f9;--bg-subtle:#f8fafc;
  --green-50:#f0fdf4;--green-500:#22c55e;--green-600:#16a34a;
  --font-sans:'Plus Jakarta Sans','Inter',-apple-system,BlinkMacSystemFont,sans-serif;
  --font-body:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;"""

new_colors = """:root {
  /* SkipIt Brand Colors — Official Palette */
  --brand:        #0044FF;
  --brand-dark:   #0036D6;
  --brand-darker: #0028A8;
  --brand-deep:   #160078;
  --brand-light:  #EBF0FF;
  --brand-subtle: #D6E0FF;

  /* Blue scale mapped to brand */
  --blue-50:  #EBF0FF;
  --blue-100: #D6E0FF;
  --blue-200: #ADCBFF;
  --blue-300: #7AABFF;
  --blue-400: #4D8CFF;
  --blue-500: #0044FF;
  --blue-600: #0036D6;
  --blue-700: #0028A8;
  --blue-800: #160078;
  --blue-900: #0D0050;

  /* Neutrals */
  --white:    #ffffff;
  --gray-50:  #f9f9fb;
  --gray-100: #f1f1f5;
  --gray-200: #E2E2E2;
  --gray-300: #c8c8d0;
  --gray-400: #9a9aaa;
  --gray-500: #6e6e82;
  --gray-600: #4e4e64;
  --gray-700: #35354a;
  --gray-800: #1e1e30;
  --gray-900: #0d0d1a;

  /* Semantic */
  --text-primary:   #0d0d1a;
  --text-secondary: #4e4e64;
  --text-muted:     #9a9aaa;
  --border:         #E2E2E2;
  --border-light:   #f1f1f5;
  --bg-subtle:      #f9f9fb;

  --green-50:  #f0fdf4;--green-500:#22c55e;--green-600:#16a34a;

  --font-sans:'Plus Jakarta Sans','Inter',-apple-system,BlinkMacSystemFont,sans-serif;
  --font-body:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;"""

css = css.replace(old_colors, new_colors)

# Replace brand shadow
css = css.replace("--shadow-brand:0 8px 32px rgba(37,99,235,.24);",
                  "--shadow-brand:0 8px 32px rgba(0,68,255,.28);")

# Update hero bg pattern colors
css = css.replace(
    "background:radial-gradient(ellipse 70% 50% at 70% 20%,rgba(37,99,235,.05) 0,transparent 70%),\n              radial-gradient(ellipse 40% 40% at 10% 80%,rgba(37,99,235,.03) 0,transparent 60%)",
    "background:radial-gradient(ellipse 70% 50% at 70% 20%,rgba(0,68,255,.05) 0,transparent 70%),\n              radial-gradient(ellipse 40% 40% at 10% 80%,rgba(22,0,120,.03) 0,transparent 60%)"
)

# Update CTA section radial
css = css.replace(
    "background:radial-gradient(circle,rgba(37,99,235,.15) 0,transparent 70%);",
    "background:radial-gradient(circle,rgba(0,68,255,.2) 0,transparent 70%);"
)

# Update btn--primary shadow
css = css.replace(
    "box-shadow:0 2px 8px rgba(37,99,235,.3),0 1px 2px rgba(37,99,235,.2)}",
    "box-shadow:0 2px 8px rgba(0,68,255,.3),0 1px 2px rgba(0,68,255,.2)}"
)

# Update hero badge dot color and border
css = css.replace(
    "border:1px solid var(--blue-200);color:var(--brand);font-size:.8125rem;font-weight:600;\n  padding:7px 14px;border-radius:var(--radius-full);margin-bottom:24px}",
    "border:1px solid var(--blue-200);color:var(--brand);font-size:.8125rem;font-weight:600;\n  padding:7px 14px;border-radius:var(--radius-full);margin-bottom:24px}\n"
)

# Update gradient for owner avatar
css = css.replace(
    "background:linear-gradient(135deg,var(--brand),var(--blue-400));",
    "background:linear-gradient(135deg,var(--brand-deep),var(--brand));"
)

# Update biz-card--revenue gradient
css = css.replace(
    ".biz-card--revenue{background:linear-gradient(135deg,var(--brand),var(--blue-700));",
    ".biz-card--revenue{background:linear-gradient(135deg,var(--brand-deep),var(--brand));"
)

with open(os.path.join(BASE, "styles.css"), "w", encoding="utf-8") as f:
    f.write(css)

print(f"CSS updated: {os.path.getsize(os.path.join(BASE, 'styles.css'))} bytes")

# ─────────────────────────────────────────
# 2. Update index.html — logo + colors
# ─────────────────────────────────────────

# The SkipIt logo icon SVG (shopping cart / basket with two wheel dots)
# Based on the brand image: white shape on blue background
LOGO_ICON_SVG = """<svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Cart body: rounded rect with top-right quadrant cut -->
  <rect x="6" y="6" width="20" height="18" rx="3" fill="white"/>
  <!-- Top-right cutout to create the cart opening -->
  <rect x="18" y="6" width="8" height="9" rx="1" fill="#0044FF"/>
  <!-- Two wheels -->
  <circle cx="11" cy="30" r="4" fill="white"/>
  <circle cx="23" cy="30" r="4" fill="white"/>
  <!-- Inner white accent on cutout edge -->
  <rect x="17.5" y="14.5" width="3" height="3" rx="1" fill="white"/>
</svg>"""

# Simpler, more accurate logo icon based on brand image
LOGO_ICON_SVG = """<svg viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Main body: white left+bottom L-shape (cart basket) -->
  <path d="M5 5 H22 V14 H14 V22 H5 Z" fill="white" rx="2"/>
  <rect x="5" y="5" width="17" height="9" rx="2" ry="2" fill="white"/>
  <rect x="5" y="13" width="9" height="10" rx="0" ry="0" fill="white"/>
  <!-- Two circles (cart wheels) -->
  <circle cx="11" cy="29" r="4" fill="white"/>
  <circle cx="23" cy="29" r="4" fill="white"/>
  <!-- Right side panel (smaller upper right block) -->
  <rect x="16" y="16" width="14" height="9" rx="2" fill="white"/>
</svg>"""

# Actually let me use a cleaner version matching exactly the brand image
# The icon is: a shopping cart silhouette - looks like a bag/cart with a bite out of top-right
LOGO_ICON_SVG = """<svg viewBox="0 0 38 38" fill="white" xmlns="http://www.w3.org/2000/svg">
  <path d="M4 6C4 4.895 4.895 4 6 4H24C25.105 4 26 4.895 26 6V15H16C14.895 15 14 15.895 14 17V26H6C4.895 26 4 25.105 4 24V6Z"/>
  <rect x="17" y="17" width="17" height="9" rx="2"/>
  <circle cx="10" cy="32" r="4"/>
  <circle cx="24" cy="32" r="4"/>
</svg>"""

# Navbar logo HTML
OLD_NAV_LOGO = """      <div class="nav-logo-icon">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" fill="white"/>
        </svg>
      </div>
      <span class="nav-logo-text">Skip<span>It</span></span>"""

NEW_NAV_LOGO = """      <div class="nav-logo-icon">
        <svg viewBox="0 0 38 38" fill="white" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 6C4 4.895 4.895 4 6 4H24C25.105 4 26 4.895 26 6V15H16C14.895 15 14 15.895 14 17V26H6C4.895 26 4 25.105 4 24V6Z"/>
          <rect x="17" y="17" width="17" height="9" rx="2"/>
          <circle cx="10" cy="32" r="4"/>
          <circle cx="24" cy="32" r="4"/>
        </svg>
      </div>
      <span class="nav-logo-text">skipit</span>"""

with open(os.path.join(BASE, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# Update navbar logo
html = html.replace(OLD_NAV_LOGO, NEW_NAV_LOGO)

# Remove the <span> color from logo text (now it's just "skipit")
# Also update footer logo
OLD_FOOTER_LOGO = """<span style="font-family:var(--font-sans);font-size:1.25rem;font-weight:800;color:white;letter-spacing:-.03em">Skip<span style="color:var(--blue-400)">It</span></span>"""
NEW_FOOTER_LOGO = """<span style="font-family:var(--font-sans);font-size:1.25rem;font-weight:800;color:white;letter-spacing:-.05em;text-transform:lowercase">skipit</span>"""
html = html.replace(OLD_FOOTER_LOGO, NEW_FOOTER_LOGO)

# Update footer icon to match
OLD_FOOTER_ICON = """            <div class="nav-logo-icon" style="background:rgba(255,255,255,.12);width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" style="width:18px;height:18px;fill:white">
              <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
            </svg>
          </div>"""

NEW_FOOTER_ICON = """            <div class="nav-logo-icon" style="background:var(--brand);width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center">
            <svg viewBox="0 0 38 38" fill="white" xmlns="http://www.w3.org/2000/svg" style="width:20px;height:20px">
              <path d="M4 6C4 4.895 4.895 4 6 4H24C25.105 4 26 4.895 26 6V15H16C14.895 15 14 15.895 14 17V26H6C4.895 26 4 25.105 4 24V6Z"/>
              <rect x="17" y="17" width="17" height="9" rx="2"/>
              <circle cx="10" cy="32" r="4"/>
              <circle cx="24" cy="32" r="4"/>
            </svg>
          </div>"""

html = html.replace(OLD_FOOTER_ICON, NEW_FOOTER_ICON)

# Update nav-logo-text CSS inline references — remove "Skip<span>It</span>" in title
# The title tag
html = html.replace("<title>SkipIt — Skip buying. Rent smarter.</title>",
                    "<title>skipit — Skip buying. Rent smarter.</title>")

# OG title
html = html.replace('<meta property="og:title" content="SkipIt — Skip buying. Rent smarter.">',
                    '<meta property="og:title" content="skipit — Skip buying. Rent smarter.">')

# Update CTA section button colors to use correct brand
# Already using var(--brand) so those will auto-update

# Update hero badge background color inline styles
html = html.replace(
    'style="background:var(--brand-light)',
    'style="background:var(--brand-light)'  # no change needed, css vars handle it
)

# Update the hero floating card brand colors
html = html.replace(
    'style="background:var(--brand-light)">\n          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:16px;height:16px;color:var(--brand)"',
    'style="background:var(--brand-light)">\n          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:16px;height:16px;color:var(--brand)"'
)

# Update the example listing card color references
html = html.replace(
    'style="background:var(--green-50);color:var(--green-600);font-size:.75rem;font-weight:700;padding:4px 10px;border-radius:var(--radius-full)"',
    'style="background:var(--green-50);color:var(--green-600);font-size:.75rem;font-weight:700;padding:4px 10px;border-radius:var(--radius-full)"'
)

# Update the hero tagline inline color
html = html.replace(
    '<strong style="color:var(--blue-300)">The insight:</strong>',
    '<strong style="color:var(--blue-300)">The insight:</strong>'
)

with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print(f"HTML updated: {os.path.getsize(os.path.join(BASE, 'index.html'))} bytes")

# ─────────────────────────────────────────
# 3. Add logo text styling to CSS
# ─────────────────────────────────────────
with open(os.path.join(BASE, "styles.css"), "r", encoding="utf-8") as f:
    css = f.read()

# Update nav-logo-text to remove the span color and use lowercase
css = css.replace(
    ".nav-logo-text{font-family:var(--font-sans);font-size:1.375rem;font-weight:800;\n  color:var(--text-primary);letter-spacing:-.03em}\n.nav-logo-text span{color:var(--brand)}",
    ".nav-logo-text{font-family:var(--font-sans);font-size:1.375rem;font-weight:800;\n  color:var(--text-primary);letter-spacing:-.055em;text-transform:lowercase}"
)

# Increase logo icon size slightly and update border radius
css = css.replace(
    ".nav-logo-icon{width:34px;height:34px;background:var(--brand);border-radius:10px;\n  display:flex;align-items:center;justify-content:center}",
    ".nav-logo-icon{width:36px;height:36px;background:var(--brand);border-radius:10px;\n  display:flex;align-items:center;justify-content:center}"
)

# Update the logo SVG size in nav
css = css.replace(
    ".nav-logo-icon svg{width:18px;height:18px;fill:white}",
    ".nav-logo-icon svg{width:21px;height:21px;fill:white}"
)

with open(os.path.join(BASE, "styles.css"), "w", encoding="utf-8") as f:
    f.write(css)

print(f"CSS final: {os.path.getsize(os.path.join(BASE, 'styles.css'))} bytes")
print("All brand updates applied!")
