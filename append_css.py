css_append = """
/* AMBIENT BACKGROUND */
.ambient-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1;
  background: var(--bg-main);
  overflow: hidden;
  pointer-events: none;
}
.ambient-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.5;
  animation: float-orb 20s infinite alternate ease-in-out;
}
.orb-1 {
  width: 600px;
  height: 600px;
  background: rgba(0, 68, 255, 0.15);
  top: -10%;
  right: -10%;
}
.orb-2 {
  width: 800px;
  height: 800px;
  background: rgba(22, 0, 120, 0.15);
  bottom: -20%;
  left: -20%;
  animation-delay: -5s;
}
@keyframes float-orb {
  0% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(-30px, 50px) scale(1.1); }
  100% { transform: translate(50px, -30px) scale(0.9); }
}

/* Fix glass panel text colors for readability */
.product-card-title,
.lm-owner-name,
.product-price-main,
.stat-value,
.benefit-text h4,
.smart-card h4,
.trust-card h3,
.plan-tier,
.biz-card h3,
.comparison-label,
.flow-box {
  color: var(--text-primary) !important;
}

.product-price-per,
.product-card-location,
.product-card-rating,
.lm-owner-sub,
.benefit-text p,
.smart-card p,
.trust-card p,
.plan-description,
.plan-feature,
.biz-card p {
  color: var(--text-secondary) !important;
}

.lm-price-main,
.lm-title {
  color: var(--text-primary);
}

.lm-deposit-val {
  color: var(--text-primary) !important;
}

/* Update inputs and textareas to dark mode */
input, textarea {
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-primary);
  border: 1px solid var(--border);
}
input::placeholder, textarea::placeholder {
  color: var(--text-muted);
}
.search-input-wrap input {
  color: var(--text-primary);
}

/* Modals glass */
.listing-modal, .search-modal {
  box-shadow: 0 24px 64px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.1);
}
.listing-modal-body, .search-modal {
  background: transparent !important;
}
.listing-modal-image, .product-card-image {
  background: transparent !important;
}
"""

with open("styles.css", "a", encoding="utf-8") as f:
    f.write(css_append)

print("CSS appended successfully.")
