import re

# Update styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace :root variables
new_root = """:root {
  /* SkipIt Brand Colors — Glassmorphism Premium */
  --brand:        #0055ff;
  --brand-dark:   #0044cc;
  --brand-light:  rgba(0, 85, 255, 0.15);
  
  --bg-main:      #030508; /* Very dark navy/black */
  
  /* Glass Tokens */
  --glass-bg:     rgba(15, 20, 35, 0.4);
  --glass-border: rgba(255, 255, 255, 0.06);
  --glass-highlight: rgba(255, 255, 255, 0.1);
  --glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
  --glass-blur:   blur(20px);
  
  --white:        #ffffff;
  --gray-50:      #f9f9fb;
  --gray-100:     #1a1f2e; /* Adapted for dark mode */
  --gray-200:     #252b3d;
  --gray-800:     #0f1423;
  --gray-900:     #0a0d18;

  --text-primary:   #ffffff;
  --text-secondary: #9ba1b0;
  --text-muted:     #6b7280;
  --border:         var(--glass-border);
  --border-light:   rgba(255, 255, 255, 0.04);
  --bg-subtle:      transparent;
  
  --green-50:  rgba(34, 197, 94, 0.15);
  --green-500: #22c55e;
  --green-600: #16a34a;
  
  --blue-50: rgba(0, 85, 255, 0.1);
  --blue-100: rgba(0, 85, 255, 0.15);
  --blue-200: rgba(0, 85, 255, 0.25);
  --blue-300: #7AABFF;

  --font-sans: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-2xl: 32px;
  --radius-full: 9999px;
  
  --shadow-xs: 0 1px 2px rgba(0,0,0,0.2);
  --shadow-sm: 0 2px 8px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.4);
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.5);
  --shadow-xl: 0 16px 48px rgba(0,0,0,0.6);
  --shadow-brand: 0 8px 32px rgba(0, 85, 255, 0.4);
  
  --ease-out: cubic-bezier(.16,1,.3,1);
  --duration: 280ms;
  --duration-fast: 160ms;
}"""
css = re.sub(r':root\s*\{.*?\}(?=\n\*,)', new_root, css, flags=re.DOTALL)

# Background and Glass classes
css = css.replace("body{font-family:var(--font-body);font-size:1rem;line-height:1.6;color:var(--text-primary);\n  background:#fff;", "body{font-family:var(--font-body);font-size:1rem;line-height:1.6;color:var(--text-primary);\n  background:var(--bg-main);")

glass_css = """
/* GLASSMORPHISM SYSTEM */
.glass-panel {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  box-shadow: var(--glass-shadow);
  border-radius: var(--radius-xl);
  position: relative;
  overflow: hidden;
}
.glass-panel::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, var(--glass-highlight), transparent);
}
"""

css = glass_css + css

# Replace specific component backgrounds
# product-card
css = css.replace(".product-card{background:#fff;border-radius:var(--radius-xl);border:1px solid var(--border);", ".product-card{background:var(--glass-bg);backdrop-filter:var(--glass-blur);-webkit-backdrop-filter:var(--glass-blur);border-radius:var(--radius-xl);border:1px solid var(--glass-border);box-shadow:var(--glass-shadow);")
css = css.replace(".product-card-image{aspect-ratio:4/3;overflow:hidden;background:var(--gray-100);", ".product-card-image{aspect-ratio:4/3;overflow:hidden;background:rgba(0,0,0,0.2);")

# step-card
css = css.replace(".step-card{background:#fff;border-radius:var(--radius-xl);padding:32px;\n  border:1px solid var(--border);box-shadow:var(--shadow-sm);", ".step-card{background:var(--glass-bg);backdrop-filter:var(--glass-blur);-webkit-backdrop-filter:var(--glass-blur);border-radius:var(--radius-xl);padding:32px;\n  border:1px solid var(--glass-border);box-shadow:var(--glass-shadow);")

# trust-card
css = css.replace(".trust-card{background:#fff;border-radius:var(--radius-xl);padding:24px;\n  border:1px solid var(--border);", ".trust-card{background:var(--glass-bg);backdrop-filter:var(--glass-blur);-webkit-backdrop-filter:var(--glass-blur);border-radius:var(--radius-xl);padding:24px;\n  border:1px solid var(--glass-border);box-shadow:var(--glass-shadow);")

# stat-card
css = css.replace(".stat-card{text-align:center;padding:32px 24px;border-radius:var(--radius-xl);\n  background:var(--bg-subtle);border:1px solid var(--border);", ".stat-card{text-align:center;padding:32px 24px;border-radius:var(--radius-xl);\n  background:var(--glass-bg);backdrop-filter:var(--glass-blur);-webkit-backdrop-filter:var(--glass-blur);border:1px solid var(--glass-border);box-shadow:var(--glass-shadow);")

# plan-card
css = css.replace(".plan-card{border-radius:var(--radius-2xl);padding:32px;border:1.5px solid var(--border);\n  position:relative;transition:all var(--duration);background:#fff}", ".plan-card{border-radius:var(--radius-2xl);padding:32px;border:1px solid var(--glass-border);\n  position:relative;transition:all var(--duration);background:var(--glass-bg);backdrop-filter:var(--glass-blur);-webkit-backdrop-filter:var(--glass-blur);box-shadow:var(--glass-shadow);}")

# navbar
css = css.replace("#navbar{position:fixed;top:0;left:0;right:0;z-index:1000;\n  background:rgba(255,255,255,.92);backdrop-filter:blur(16px);", "#navbar{position:fixed;top:0;left:0;right:0;z-index:1000;\n  background:rgba(10, 15, 25, 0.6);backdrop-filter:var(--glass-blur);")

# modal
css = css.replace(".listing-modal{background:#fff;border-radius:var(--radius-2xl);", ".listing-modal{background:var(--glass-bg);backdrop-filter:var(--glass-blur);-webkit-backdrop-filter:var(--glass-blur);border:1px solid var(--glass-border);border-radius:var(--radius-2xl);")
css = css.replace(".search-modal{background:#fff;border-radius:var(--radius-2xl);", ".search-modal{background:var(--glass-bg);backdrop-filter:var(--glass-blur);-webkit-backdrop-filter:var(--glass-blur);border:1px solid var(--glass-border);border-radius:var(--radius-2xl);")

# mobile nav
css = css.replace(".mobile-nav{display:none;position:fixed;inset:0;z-index:999;background:#fff;", ".mobile-nav{display:none;position:fixed;inset:0;z-index:999;background:var(--bg-main);")

# backgrounds
css = css.replace("background:#fff", "background:transparent")
css = css.replace("background:var(--gray-900)", "background:transparent")

# text adjustments
css = css.replace("color:var(--text-primary)", "color:var(--text-primary)")
css = css.replace("color:var(--text-secondary)", "color:var(--text-secondary)")
css = css.replace("color:#fff", "color:var(--text-primary)")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

# Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add a global ambient background
ambient_bg = '''<div class="ambient-bg">
  <div class="ambient-orb orb-1"></div>
  <div class="ambient-orb orb-2"></div>
</div>
'''

if "ambient-bg" not in html:
    html = html.replace("<body>", f"<body>\n{ambient_bg}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Theme applied successfully.")
