
import os

BASE = r"C:\Users\ashish kumar\Downloads\new web"

# 1. Update styles.css
with open(os.path.join(BASE, "styles.css"), "r", encoding="utf-8") as f:
    css = f.read()

DARK_CSS = """

/* ============================================================
   DARK THEME
   ============================================================ */
body.dark-theme {
  --white:    #0d0d1a;
  --gray-50:  #141421;
  --gray-100: #1e1e30;
  --gray-200: #35354a;
  --gray-300: #4e4e64;
  --gray-400: #6e6e82;
  --gray-500: #9a9aaa;
  --gray-600: #c8c8d0;
  --gray-700: #E2E2E2;
  --gray-800: #f1f1f5;
  --gray-900: #f9f9fb;

  --text-primary:   #ffffff;
  --text-secondary: #c8c8d0;
  --text-muted:     #9a9aaa;
  
  --border:         #35354a;
  --border-light:   #1e1e30;
  --bg-subtle:      #141421;
}

body {
  transition: background-color var(--duration) var(--ease-out), color var(--duration) var(--ease-out);
}

.product-card, .search-modal, .listing-modal, .step-card, .comparison-card, .plan-card, .smart-card, .trust-card, .biz-card, .split-visual, #navbar, .mobile-nav, .mobile-cta-bar, .hero-floating-card, .owner-banner {
  transition: background-color var(--duration) var(--ease-out), border-color var(--duration) var(--ease-out), box-shadow var(--duration) var(--ease-out), transform var(--duration) var(--ease-out);
}

body.dark-theme .hero-bg-pattern {
  opacity: 0.15;
}

body.dark-theme #the-problem {
  background: #080811;
}

body.dark-theme #cta-section, body.dark-theme #footer {
  background: #080811;
}

body.dark-theme .nav-logo-text {
  color: #fff;
}

body.dark-theme .btn--white {
  background: var(--brand);
  color: #fff;
}

body.dark-theme .btn--outline-white {
  border-color: rgba(255,255,255,0.3);
}

body.dark-theme .search-modal {
  background: var(--gray-50);
}
"""

if "body.dark-theme" not in css:
    with open(os.path.join(BASE, "styles.css"), "a", encoding="utf-8") as f:
        f.write(DARK_CSS)

# 2. Update index.html
with open(os.path.join(BASE, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

NAV_ACTIONS_OLD = """<div class="nav-actions">
      <button class="nav-search-btn js-open-search" aria-label="Search" id="navSearchBtn">"""

NAV_ACTIONS_NEW = """<div class="nav-actions">
      <button class="nav-search-btn" id="themeToggle" aria-label="Toggle dark mode">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" id="themeIcon">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
      </button>
      <button class="nav-search-btn js-open-search" aria-label="Search" id="navSearchBtn">"""

if 'id="themeToggle"' not in html:
    html = html.replace(NAV_ACTIONS_OLD, NAV_ACTIONS_NEW)
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

# 3. Update main.js
with open(os.path.join(BASE, "main.js"), "r", encoding="utf-8") as f:
    js = f.read()

DARK_JS = """
// ============================================================
// DARK MODE TOGGLE
// ============================================================
const themeToggle = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');

function setTheme(isDark) {
  if (isDark) {
    document.body.classList.add('dark-theme');
    themeIcon.innerHTML = '<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>';
    localStorage.setItem('skipit_theme', 'dark');
  } else {
    document.body.classList.remove('dark-theme');
    themeIcon.innerHTML = '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>';
    localStorage.setItem('skipit_theme', 'light');
  }
}

// Initialize theme
const savedTheme = localStorage.getItem('skipit_theme');
const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
  setTheme(true);
}

themeToggle?.addEventListener('click', () => {
  const isDark = document.body.classList.contains('dark-theme');
  setTheme(!isDark);
});
"""

if "DARK MODE TOGGLE" not in js:
    with open(os.path.join(BASE, "main.js"), "a", encoding="utf-8") as f:
        f.write(DARK_JS)

print("Dark mode implemented.")
