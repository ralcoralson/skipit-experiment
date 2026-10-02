# Python script to generate the pixel-perfect Glass UI Dashboard matching the user's uploaded screenshot

dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Glass UI Financial & Rental Dashboard</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    :root {
      --bg-outer: #0a0b0d;
      --bg-canvas: #16181d;
      --card-bg: rgba(36, 39, 47, 0.88);
      --card-border: rgba(255, 255, 255, 0.08);
      --card-hover: rgba(45, 49, 58, 0.95);
      --card-black: #0c0d11;
      --card-white: #ffffff;
      --accent-red: #e52b2b;
      --accent-red-hover: #ff3b3b;
      --accent-coral: #eb4b32;
      --accent-glow: rgba(235, 75, 50, 0.42);
      --text-white: #ffffff;
      --text-muted: rgba(255, 255, 255, 0.55);
      --text-subtle: rgba(255, 255, 255, 0.35);
      --font-display: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --radius-device: 36px;
      --radius-card: 22px;
      --radius-inner: 16px;
      --radius-pill: 9999px;
      --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
    }

    body {
      background-color: var(--bg-outer);
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(255, 255, 255, 0.03) 0%, transparent 60%),
        radial-gradient(circle at 100% 100%, rgba(235, 75, 50, 0.08) 0%, transparent 50%);
      color: var(--text-white);
      font-family: var(--font-body);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px 16px;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* TOP CONTROLS BAR (MODE SWITCHER) */
    .top-toolbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      max-width: 1240px;
      margin-bottom: 16px;
      padding: 0 8px;
    }

    .brand-title-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      color: #ff5733;
      background: rgba(235, 75, 50, 0.12);
      border: 1px solid rgba(235, 75, 50, 0.3);
      padding: 4px 12px;
      border-radius: var(--radius-pill);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }

    .view-toggles {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .btn-toggle {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: rgba(255, 255, 255, 0.8);
      font-family: var(--font-display);
      font-size: 0.8125rem;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
    }

    .btn-toggle:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.2);
    }

    .btn-toggle.active {
      background: rgba(255, 255, 255, 0.2);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.35);
    }

    /* DEVICE CANVAS CONTAINER (MOCKUP FRAME) */
    .device-container {
      width: 100%;
      max-width: 1240px;
      background: var(--bg-canvas);
      border-radius: var(--radius-device);
      box-shadow: 
        0 30px 90px rgba(0, 0, 0, 0.75),
        0 0 0 12px #101216,
        0 0 0 13.5px rgba(255, 255, 255, 0.12);
      position: relative;
      overflow: hidden;
      transition: all 0.4s var(--ease-smooth);
    }

    /* Fullscreen mode expands container */
    body.fullscreen-mode .device-container {
      max-width: 100%;
      border-radius: 0;
      box-shadow: none;
      min-height: 100vh;
    }

    /* AMBIENT BACKGROUND GLOW (CRUCIAL VISUAL EFFECT FROM IMAGE) */
    .ambient-glow-wrapper {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }

    .ambient-glow-coral {
      position: absolute;
      top: 15%;
      right: -5%;
      width: 620px;
      height: 620px;
      background: radial-gradient(circle, var(--accent-glow) 0%, rgba(215, 60, 40, 0.24) 35%, transparent 70%);
      filter: blur(50px);
      transform: translate3d(0, 0, 0);
    }

    .ambient-glow-bottom {
      position: absolute;
      bottom: -10%;
      right: 15%;
      width: 450px;
      height: 450px;
      background: radial-gradient(circle, rgba(235, 90, 50, 0.18) 0%, transparent 65%);
      filter: blur(40px);
    }

    /* TOP NOTCH (MACBOOK / TABLET NOTCH PILL) */
    .device-notch {
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 130px;
      height: 22px;
      background: #000000;
      border-radius: 0 0 14px 14px;
      z-index: 50;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
    }

    .notch-camera {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #111a24;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .notch-sensor {
      width: 4px;
      height: 4px;
      border-radius: 50%;
      background: #0a0e14;
    }

    /* DASHBOARD INNER WRAPPER */
    .dashboard-inner {
      position: relative;
      z-index: 1;
      padding: 24px 28px 28px 28px;
    }

    /* TOP HEADER & NAVIGATION */
    .dash-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 24px;
      padding-top: 4px;
      flex-wrap: wrap;
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    /* Logo Icon: Red circular glyph with crescent cutout */
    .dash-logo-icon {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--accent-red);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 10px rgba(229, 43, 43, 0.4);
      flex-shrink: 0;
    }

    .dash-logo-icon svg {
      width: 22px;
      height: 22px;
      fill: #ffffff;
    }

    /* Dropdown Pills: Monthly and Filter */
    .pill-dropdown-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-pill);
      padding: 8px 18px;
      font-family: var(--font-body);
      font-size: 0.8125rem;
      font-weight: 500;
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      transition: all 0.2s ease;
      position: relative;
    }

    .pill-dropdown-btn:hover {
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(255, 255, 255, 0.15);
    }

    .pill-dropdown-btn svg {
      width: 14px;
      height: 14px;
      opacity: 0.8;
    }

    /* Center Navigation Tabs */
    .nav-tabs-pill {
      background: rgba(255, 255, 255, 0.05);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: var(--radius-pill);
      padding: 4px 6px;
      display: flex;
      align-items: center;
      gap: 2px;
    }

    .nav-tab-item {
      font-family: var(--font-body);
      font-size: 0.8125rem;
      font-weight: 500;
      color: rgba(255, 255, 255, 0.6);
      padding: 7px 15px;
      border-radius: var(--radius-pill);
      border: none;
      background: transparent;
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
    }

    .nav-tab-item:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.06);
    }

    .nav-tab-item.active {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.16);
      font-weight: 600;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }

    /* Header Right: Notification Bell & Profile Avatar */
    .header-right {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .btn-notification {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: center;
      color: rgba(255, 255, 255, 0.8);
      cursor: pointer;
      position: relative;
      transition: all 0.2s ease;
    }

    .btn-notification:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #ffffff;
    }

    .btn-notification svg {
      width: 17px;
      height: 17px;
    }

    .notif-badge-dot {
      position: absolute;
      top: 9px;
      right: 10px;
      width: 6px;
      height: 6px;
      background: var(--accent-red);
      border-radius: 50%;
      box-shadow: 0 0 6px var(--accent-red);
    }

    .user-avatar-btn {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      overflow: hidden;
      border: 1.5px solid rgba(255, 255, 255, 0.2);
      cursor: pointer;
      flex-shrink: 0;
      transition: transform 0.2s ease;
    }

    .user-avatar-btn:hover {
      transform: scale(1.05);
      border-color: #ffffff;
    }

    .user-avatar-btn img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    /* ============================================================
       BENTO GRID LAYOUT
       ============================================================ */
    .dashboard-grid {
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 20px;
    }

    .main-column {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .side-column {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* CARD BASE STYLES */
    .dash-card {
      background: var(--card-bg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-card);
      padding: 22px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
      position: relative;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .dash-card:hover {
      border-color: rgba(255, 255, 255, 0.14);
      box-shadow: 0 14px 40px rgba(0, 0, 0, 0.45);
    }

    .dash-card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
    }

    .card-title {
      font-family: var(--font-display);
      font-size: 0.9375rem;
      font-weight: 700;
      color: var(--text-white);
    }

    .card-dots-btn {
      color: var(--text-muted);
      cursor: pointer;
      font-size: 1.25rem;
      line-height: 1;
      padding: 2px 6px;
      border-radius: 4px;
      border: none;
      background: none;
      transition: color 0.2s;
    }

    .card-dots-btn:hover {
      color: #ffffff;
    }

    .card-edit-btn {
      font-size: 0.8125rem;
      font-weight: 500;
      color: var(--text-muted);
      background: none;
      border: none;
      cursor: pointer;
      transition: color 0.2s;
    }

    .card-edit-btn:hover {
      color: #ffffff;
      text-decoration: underline;
    }

    /* ============================================================
       TOP ROW: DAILY LIMIT + SCHEDULE PAYMENT
       ============================================================ */
    .top-cards-row {
      display: grid;
      grid-template-columns: 0.88fr 1.12fr;
      gap: 20px;
    }

    /* Daily Limit Card */
    .card-daily-limit .limit-stat {
      display: flex;
      align-items: baseline;
      gap: 6px;
      margin-bottom: 20px;
    }

    .limit-current {
      font-family: var(--font-display);
      font-size: 1.875rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.02em;
    }

    .limit-total {
      font-size: 0.9375rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    /* Progress bar with solid red fill + hatched pattern */
    .limit-progress-bar {
      display: flex;
      gap: 8px;
      height: 40px;
      width: 100%;
    }

    .progress-solid {
      flex: 1.2;
      background: var(--accent-red);
      border-radius: 12px;
      box-shadow: 0 4px 14px rgba(229, 43, 43, 0.4);
      transition: flex 0.4s var(--ease-smooth);
    }

    .progress-hatched {
      flex: 1;
      background-color: rgba(255, 255, 255, 0.04);
      background-image: repeating-linear-gradient(
        90deg,
        rgba(255, 255, 255, 0.35) 0px,
        rgba(255, 255, 255, 0.35) 2px,
        transparent 2px,
        transparent 6px
      );
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* Schedule Payment Card (Vibrant Red Accent) */
    .card-schedule-payment {
      background: linear-gradient(135deg, #e52b2b 0%, #cf1d1d 100%);
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 12px 36px rgba(229, 43, 43, 0.38);
      color: #ffffff;
    }

    .card-schedule-payment:hover {
      box-shadow: 0 16px 44px rgba(229, 43, 43, 0.48);
    }

    .schedule-main {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      margin-bottom: 20px;
    }

    .service-logo-circle {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: #000000;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 8px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }

    .service-logo-circle svg {
      width: 18px;
      height: 18px;
      fill: #e50914;
    }

    .schedule-amount {
      font-family: var(--font-display);
      font-size: 1.5rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.1;
      margin-bottom: 2px;
    }

    .schedule-date {
      font-size: 0.75rem;
      opacity: 0.85;
      font-weight: 500;
    }

    .schedule-subs-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      border-top: 1px solid rgba(255, 255, 255, 0.2);
      padding-top: 12px;
    }

    .sub-item {
      cursor: pointer;
      transition: transform 0.2s ease, opacity 0.2s;
    }

    .sub-item:hover {
      transform: translateY(-2px);
      opacity: 0.9;
    }

    .sub-item-amount {
      font-family: var(--font-display);
      font-size: 0.9375rem;
      font-weight: 700;
      line-height: 1.2;
    }

    .sub-item-name {
      font-size: 0.75rem;
      opacity: 0.8;
      margin-top: 1px;
    }

    /* ============================================================
       MIDDLE ROW: ACTIVITY SUMMARY (STRIATED BAR CHART)
       ============================================================ */
    .card-activity-summary {
      background: var(--card-black);
      border: 1px solid rgba(255, 255, 255, 0.06);
      padding: 24px;
    }

    .chart-container {
      position: relative;
      margin-top: 8px;
      height: 240px;
    }

    .chart-svg {
      width: 100%;
      height: 100%;
      overflow: visible;
    }

    /* Floating Tooltip */
    .chart-tooltip {
      position: absolute;
      top: 16px;
      left: 48%;
      transform: translate(-50%, -100%);
      background: rgba(36, 40, 48, 0.92);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(255, 255, 255, 0.16);
      border-radius: 12px;
      padding: 8px 14px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
      pointer-events: none;
      transition: all 0.3s var(--ease-smooth);
      z-index: 10;
    }

    .chart-tooltip-header {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.6875rem;
      color: var(--text-muted);
      margin-bottom: 2px;
    }

    .chart-tooltip-amount {
      font-family: var(--font-display);
      font-size: 0.9375rem;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.1;
    }

    .chart-tooltip-month {
      font-size: 0.6875rem;
      color: rgba(255, 255, 255, 0.6);
    }

    /* ============================================================
       BOTTOM ROW: SEND MONEY + TOTAL INCOME
       ============================================================ */
    .bottom-cards-row {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 20px;
    }

    /* Send Money Card (White Floating Card) */
    .card-send-money {
      background: var(--card-white);
      color: #111111;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.28);
    }

    .card-send-money .card-title {
      color: #111111;
    }

    .card-send-money .card-dots-btn {
      color: #888888;
    }

    .card-send-money .card-dots-btn:hover {
      color: #111111;
    }

    .send-money-content {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .btn-add-contact {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--accent-red);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      border: none;
      cursor: pointer;
      flex-shrink: 0;
      box-shadow: 0 2px 8px rgba(229, 43, 43, 0.35);
      transition: transform 0.2s ease;
    }

    .btn-add-contact:hover {
      transform: scale(1.08);
      background: var(--accent-red-hover);
    }

    .contacts-avatar-list {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .contact-avatar {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      overflow: hidden;
      border: 1.5px solid rgba(0, 0, 0, 0.08);
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s;
    }

    .contact-avatar:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    }

    .contact-avatar.selected {
      border: 2px solid var(--accent-red);
      box-shadow: 0 0 0 2px rgba(229, 43, 43, 0.2);
    }

    .contact-avatar img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    /* Send Money Amount Pill & Action Button */
    .send-pill-box {
      margin-left: auto;
      background: #0d0e12;
      color: #ffffff;
      border-radius: var(--radius-pill);
      padding: 6px 6px 6px 14px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .send-input-amount {
      background: transparent;
      border: none;
      outline: none;
      color: #ffffff;
      font-family: var(--font-display);
      font-size: 0.875rem;
      font-weight: 700;
      width: 75px;
    }

    .btn-send-action {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: var(--accent-coral);
      color: #ffffff;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: transform 0.2s ease;
    }

    .btn-send-action:hover {
      transform: scale(1.1);
      background: #ff5733;
    }

    .btn-send-action svg {
      width: 14px;
      height: 14px;
    }

    /* Total Income Card */
    .card-total-income {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .income-stat-wrap {
      display: flex;
      flex-direction: column;
    }

    .income-title {
      font-size: 0.8125rem;
      color: var(--text-muted);
      margin-bottom: 4px;
    }

    .income-amount {
      font-family: var(--font-display);
      font-size: 1.625rem;
      font-weight: 800;
      color: #ffffff;
    }

    .sparkline-svg {
      width: 120px;
      height: 48px;
      overflow: visible;
    }

    /* ============================================================
       SIDE COLUMN: AI INSIGHTS & NOTIFICATIONS
       ============================================================ */

    /* AI INSIGHTS (HERO FROSTED GLASS PANEL) */
    .card-ai-insights {
      background: rgba(255, 255, 255, 0.04);
      backdrop-filter: blur(45px);
      -webkit-backdrop-filter: blur(45px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 24px;
      padding: 22px;
      box-shadow: 0 16px 45px rgba(0, 0, 0, 0.45);
      position: relative;
      overflow: hidden;
    }

    .ai-insights-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
    }

    .ai-insights-title {
      font-family: var(--font-display);
      font-size: 0.8125rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: rgba(255, 255, 255, 0.9);
    }

    /* Inner Subcard 1: Financial Health (White) */
    .ai-health-box {
      background: #ffffff;
      border-radius: var(--radius-inner);
      padding: 18px;
      color: #111111;
      margin-bottom: 12px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
      cursor: pointer;
      transition: transform 0.2s ease;
    }

    .ai-health-box:hover {
      transform: translateY(-2px);
    }

    .ai-health-title {
      font-family: var(--font-display);
      font-size: 0.875rem;
      font-weight: 800;
      margin-bottom: 6px;
      color: #111111;
    }

    .ai-health-desc {
      font-size: 0.75rem;
      color: #444444;
      line-height: 1.5;
    }

    /* Inner Subcards: Score & Forecast */
    .ai-pill-card {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 14px;
      padding: 12px 16px;
      margin-bottom: 10px;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .ai-pill-card:hover {
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(255, 255, 255, 0.12);
      transform: translateY(-1px);
    }

    .ai-pill-card-title {
      font-family: var(--font-display);
      font-size: 0.8125rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 2px;
    }

    .ai-pill-card-sub {
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    /* Floating Ask Anything Bar */
    .ai-prompt-bar {
      margin-top: 14px;
      background: #000000;
      border: 1px solid rgba(255, 255, 255, 0.16);
      border-radius: var(--radius-pill);
      padding: 5px 6px 5px 10px;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
    }

    .ai-sparkle-icon {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: linear-gradient(135deg, #ff6b4a 0%, var(--accent-red) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 0 10px rgba(235, 75, 50, 0.5);
    }

    .ai-sparkle-icon svg {
      width: 14px;
      height: 14px;
      fill: #ffffff;
    }

    .ai-prompt-input {
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      font-family: var(--font-body);
      font-size: 0.8125rem;
      color: #ffffff;
    }

    .ai-prompt-input::placeholder {
      color: rgba(255, 255, 255, 0.45);
    }

    .btn-ai-send {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #ffffff;
      color: #000000;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: transform 0.2s ease;
      flex-shrink: 0;
    }

    .btn-ai-send:hover {
      transform: scale(1.08);
    }

    .btn-ai-send svg {
      width: 13px;
      height: 13px;
    }

    /* Notifications Card */
    .card-notifications {
      padding: 22px;
    }

    .notifications-list {
      display: flex;
      flex-direction: column;
      gap: 14px;
      margin-bottom: 16px;
    }

    .notification-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 2px 0;
      transition: transform 0.2s ease;
    }

    .notification-item:hover {
      transform: translateX(3px);
    }

    .notif-avatar {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.15);
      flex-shrink: 0;
    }

    .notif-avatar img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .notif-content {
      flex: 1;
      min-width: 0;
    }

    .notif-name {
      font-family: var(--font-display);
      font-size: 0.8125rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.2;
    }

    .notif-desc {
      font-size: 0.75rem;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .notif-time {
      font-size: 0.6875rem;
      color: var(--text-subtle);
      white-space: nowrap;
    }

    .see-all-link {
      display: block;
      text-align: right;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--accent-coral);
      text-decoration: none;
      transition: opacity 0.2s;
    }

    .see-all-link:hover {
      opacity: 0.8;
      text-decoration: underline;
    }

    /* TOAST NOTIFICATION */
    .toast-popup {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: rgba(20, 22, 28, 0.95);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #ffffff;
      padding: 14px 20px;
      border-radius: 14px;
      font-size: 0.875rem;
      font-weight: 600;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 1000;
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s var(--ease-smooth);
      pointer-events: none;
    }

    .toast-popup.show {
      transform: translateY(0);
      opacity: 1;
      pointer-events: all;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 1024px) {
      .dashboard-grid {
        grid-template-columns: 1fr;
      }
      .side-column {
        display: grid;
        grid-template-columns: 1fr 1fr;
      }
    }

    @media (max-width: 768px) {
      body {
        padding: 8px;
      }
      .device-container {
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      }
      .device-notch {
        display: none;
      }
      .dashboard-inner {
        padding: 16px;
      }
      .top-cards-row {
        grid-template-columns: 1fr;
      }
      .bottom-cards-row {
        grid-template-columns: 1fr;
      }
      .side-column {
        grid-template-columns: 1fr;
      }
      .dash-header {
        flex-direction: column;
        align-items: stretch;
      }
      .nav-tabs-pill {
        overflow-x: auto;
      }
    }
  </style>
</head>
<body>

  <!-- TOP TOOLBAR & CONTROLS -->
  <div class="top-toolbar">
    <div class="brand-title-wrap">
      <span class="brand-badge">✨ Glass UI Experience</span>
      <span style="font-size: 0.8125rem; color: rgba(255, 255, 255, 0.55)">Interactive Fintech &amp; Rental Dashboard</span>
    </div>
    <div class="view-toggles">
      <button class="btn-toggle active" id="btnDeviceView">
        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
        Device Frame
      </button>
      <button class="btn-toggle" id="btnFullscreenView">
        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>
        Fullscreen
      </button>
      <a href="marketplace.html" class="btn-toggle">
        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
        Marketplace
      </a>
    </div>
  </div>

  <!-- DEVICE CONTAINER (MOCKUP WITH CAMERA NOTCH) -->
  <div class="device-container" id="deviceContainer">
    
    <!-- Ambient Blur Background (Exact Coral Glow From Screenshot) -->
    <div class="ambient-glow-wrapper">
      <div class="ambient-glow-coral"></div>
      <div class="ambient-glow-bottom"></div>
    </div>

    <!-- Camera Notch -->
    <div class="device-notch">
      <div class="notch-camera"></div>
      <div class="notch-sensor"></div>
    </div>

    <!-- Dashboard Content -->
    <div class="dashboard-inner">

      <!-- TOP HEADER / NAV -->
      <header class="dash-header">
        <div class="header-left">
          <!-- Logo -->
          <div class="dash-logo-icon" title="Glass Dashboard">
            <svg viewBox="0 0 24 24">
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z" fill-rule="evenodd" clip-rule="evenodd"/>
              <circle cx="12" cy="12" r="9" fill="none" stroke="#fff" stroke-width="2"/>
              <path d="M12 3a9 9 0 0 1 9 9h-9V3z" fill="#fff"/>
            </svg>
          </div>

          <!-- Monthly dropdown -->
          <button class="pill-dropdown-btn" id="btnMonthly">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            <span id="labelPeriod">Monthly</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>

          <!-- Filter button -->
          <button class="pill-dropdown-btn" id="btnFilter">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
            <span>Filter</span>
          </button>
        </div>

        <!-- Center Navigation Tabs -->
        <nav class="nav-tabs-pill">
          <button class="nav-tab-item active" data-tab="dashboard">Dashboard</button>
          <button class="nav-tab-item" data-tab="wallet">My Wallet</button>
          <button class="nav-tab-item" data-tab="payment">Payment</button>
          <button class="nav-tab-item" data-tab="invoice">Invoice</button>
          <button class="nav-tab-item" data-tab="setting">Setting</button>
          <button class="nav-tab-item" data-tab="transactions">Transactions</button>
        </nav>

        <!-- Right: Notification & Profile -->
        <div class="header-right">
          <button class="btn-notification" id="btnNotification" aria-label="Notifications">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
            <span class="notif-badge-dot"></span>
          </button>
          <div class="user-avatar-btn" id="userAvatar" title="Sarah Jenkins · Verified">
            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&auto=format&fit=crop&q=80" alt="Sarah Jenkins">
          </div>
        </div>
      </header>

      <!-- MAIN BENTO GRID -->
      <div class="dashboard-grid">

        <!-- LEFT COLUMN -->
        <div class="main-column">

          <!-- TOP ROW: DAILY LIMIT + SCHEDULE PAYMENT -->
          <div class="top-cards-row">
            
            <!-- Daily Limit Card -->
            <div class="dash-card card-daily-limit">
              <div class="dash-card-header">
                <span class="card-title">Daily Limit</span>
                <button class="card-edit-btn" id="btnEditLimit">Edit</button>
              </div>
              <div class="limit-stat">
                <span class="limit-current" id="displayCurrentLimit">$1,230</span>
                <span class="limit-total" id="displayTotalLimit">/ 2,150</span>
              </div>
              <div class="limit-progress-bar">
                <div class="progress-solid" id="barSolid" title="Spent: $1,230"></div>
                <div class="progress-hatched" id="barHatched" title="Remaining: $920"></div>
              </div>
            </div>

            <!-- Schedule Payment Card (Vibrant Red) -->
            <div class="dash-card card-schedule-payment">
              <div class="dash-card-header">
                <span class="card-title" style="color:#ffffff">Schedule Payment</span>
                <button class="card-dots-btn" style="color:rgba(255,255,255,0.85)">···</button>
              </div>
              <div class="schedule-main">
                <div class="service-logo-circle" id="scheduleServiceIcon">
                  <svg viewBox="0 0 24 24">
                    <path d="M5.398 0v24L9.8 19.387V4.613L5.398 0zm8.798 0v24l4.402-4.613V4.613L14.196 0zm-4.398 5.766L14.2 24h-4.402L5.398 5.766h4.4z"/>
                  </svg>
                </div>
                <div class="schedule-amount" id="scheduleDisplayAmount">$105.99/m</div>
                <div class="schedule-date" id="scheduleDisplayDate">10 August 2026</div>
              </div>
              <div class="schedule-subs-grid">
                <div class="sub-item" onclick="switchScheduleSub('Discord', '$40.25/m', '14 August 2026')">
                  <div class="sub-item-amount">$40.25/m</div>
                  <div class="sub-item-name">Discord</div>
                </div>
                <div class="sub-item" onclick="switchScheduleSub('Netflix', '$105.99/m', '10 August 2026')">
                  <div class="sub-item-amount">$105.99/m</div>
                  <div class="sub-item-name">Netflix</div>
                </div>
                <div class="sub-item" onclick="switchScheduleSub('Notepad', '$23.25/m', '22 August 2026')">
                  <div class="sub-item-amount">$23.25/m</div>
                  <div class="sub-item-name">Notepad</div>
                </div>
              </div>
            </div>

          </div>

          <!-- MIDDLE ROW: ACTIVITY SUMMARY (STRIATED BAR CHART) -->
          <div class="dash-card card-activity-summary">
            <div class="dash-card-header">
              <span class="card-title">Activity Summary</span>
              <button class="card-dots-btn">···</button>
            </div>
            
            <div class="chart-container" id="chartContainer">
              <!-- Floating Tooltip -->
              <div class="chart-tooltip" id="chartTooltip">
                <div class="chart-tooltip-header">
                  <span id="tooltipLabel">This Month</span>
                  <svg viewBox="0 0 24 24" width="10" height="10" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
                </div>
                <div class="chart-tooltip-amount" id="tooltipAmount">$21,567</div>
                <div class="chart-tooltip-month" id="tooltipMonth">June</div>
              </div>

              <!-- High-tech Striated SVG Bar Chart -->
              <svg class="chart-svg" viewBox="0 0 740 220" preserveAspectRatio="none">
                <!-- Horizontal Dotted Gridlines -->
                <line x1="40" y1="20" x2="720" y2="20" stroke="rgba(255,255,255,0.06)" stroke-dasharray="3,3"/>
                <line x1="40" y1="60" x2="720" y2="60" stroke="rgba(255,255,255,0.06)" stroke-dasharray="3,3"/>
                <line x1="40" y1="100" x2="720" y2="100" stroke="rgba(255,255,255,0.06)" stroke-dasharray="3,3"/>
                <line x1="40" y1="140" x2="720" y2="140" stroke="rgba(255,255,255,0.06)" stroke-dasharray="3,3"/>
                <line x1="40" y1="180" x2="720" y2="180" stroke="rgba(255,255,255,0.06)" stroke-dasharray="3,3"/>

                <!-- Y-Axis Labels -->
                <text x="10" y="24" fill="rgba(255,255,255,0.35)" font-size="10" font-family="Inter">25K</text>
                <text x="10" y="64" fill="rgba(255,255,255,0.35)" font-size="10" font-family="Inter">20K</text>
                <text x="10" y="104" fill="rgba(255,255,255,0.35)" font-size="10" font-family="Inter">15K</text>
                <text x="10" y="144" fill="rgba(255,255,255,0.35)" font-size="10" font-family="Inter">10K</text>
                <text x="10" y="184" fill="rgba(255,255,255,0.35)" font-size="10" font-family="Inter">5K</text>

                <!-- Month Striated Bars Group (Generated with SVG paths) -->
                <!-- Jan -->
                <g class="bar-group" data-month="Jan" data-val="$10,240" data-x="68" onmouseenter="hoverChartBar(this)">
                  <line x1="50" y1="140" x2="86" y2="140" stroke="#e52b2b" stroke-width="2"/>
                  <path d="M52,140 V180 M56,140 V180 M60,140 V180 M64,140 V180 M68,140 V180 M72,140 V180 M76,140 V180 M80,140 V180 M84,140 V180" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
                  <text x="68" y="202" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter">Jan</text>
                </g>

                <!-- Feb -->
                <g class="bar-group" data-month="Feb" data-val="$13,150" data-x="124" onmouseenter="hoverChartBar(this)">
                  <line x1="106" y1="120" x2="142" y2="120" stroke="#e52b2b" stroke-width="2"/>
                  <path d="M108,120 V180 M112,120 V180 M116,120 V180 M120,120 V180 M124,120 V180 M128,120 V180 M132,120 V180 M136,120 V180 M140,120 V180" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
                  <text x="124" y="202" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter">Feb</text>
                </g>

                <!-- Mar -->
                <g class="bar-group" data-month="Mar" data-val="$8,400" data-x="180" onmouseenter="hoverChartBar(this)">
                  <line x1="162" y1="150" x2="198" y2="150" stroke="#e52b2b" stroke-width="2"/>
                  <path d="M164,150 V180 M168,150 V180 M172,150 V180 M176,150 V180 M180,150 V180 M184,150 V180 M188,150 V180 M192,150 V180 M196,150 V180" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
                  <text x="180" y="202" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter">Mar</text>
                </g>

                <!-- Apr -->
                <g class="bar-group" data-month="Apr" data-val="$16,800" data-x="236" onmouseenter="hoverChartBar(this)">
                  <line x1="218" y1="95" x2="254" y2="95" stroke="#e52b2b" stroke-width="2"/>
                  <path d="M220,95 V180 M224,95 V180 M228,95 V180 M232,95 V180 M236,95 V180 M240,95 V180 M244,95 V180 M248,95 V180 M252,95 V180" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
                  <text x="236" y="202" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter">Apr</text>
                </g>

                <!-- May -->
                <g class="bar-group" data-month="May" data-val="$11,300" data-x="292" onmouseenter="hoverChartBar(this)">
                  <line x1="274" y1="135" x2="310" y2="135" stroke="#e52b2b" stroke-width="2"/>
                  <path d="M276,135 V180 M280,135 V180 M284,135 V180 M288,135 V180 M292,135 V180 M296,135 V180 M300,135 V180 M304,135 V180 M308,135 V180" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
                  <text x="292" y="202" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter">May</text>
                </g>

                <!-- Jun -->
                <g class="bar-group" data-month="Jun" data-val="$15,200" data-x="348" onmouseenter="hoverChartBar(this)">
                  <line x1="330" y1="105" x2="366" y2="105" stroke="#e52b2b" stroke-width="2"/>
                  <path d="M332,105 V180 M336,105 V180 M340,105 V180 M344,105 V180 M348,105 V180 M352,105 V180 M356,105 V180 M360,105 V180 M364,105 V180" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
                  <text x="348" y="202" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter">Jun</text>
                </g>

                <!-- Jul (ACTIVE HIGHLIGHT BAR IN SCREENSHOT) -->
                <g class="bar-group active" data-month="July" data-val="$21,567" data-x="404" onmouseenter="hoverChartBar(this)">
                  <line x1="386" y1="50" x2="422" y2="50" stroke="#ff5733" stroke-width="2.5"/>
                  <path d="M388,50 V180 M392,50 V180 M396,50 V180 M400,50 V180 M404,50 V180 M408,50 V180 M412,50 V180 M416,50 V180 M420,50 V180" stroke="#ff7a59" stroke-width="1.4" opacity="0.9"/>
                  <text x="404" y="202" fill="#ffffff" font-weight="700" font-size="11" text-anchor="middle" font-family="Inter">Jul</text>
                </g>

                <!-- Aug -->
                <g class="bar-group" data-month="Aug" data-val="$12,900" data-x="460" onmouseenter="hoverChartBar(this)">
                  <line x1="442" y1="125" x2="478" y2="125" stroke="#e52b2b" stroke-width="2"/>
                  <path d="M444,125 V180 M448,125 V180 M452,125 V180 M456,125 V180 M460,125 V180 M464,125 V180 M468,125 V180 M472,125 V180 M476,125 V180" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
                  <text x="460" y="202" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter">Aug</text>
                </g>

                <!-- Sep -->
                <g class="bar-group" data-month="Sep" data-val="$9,700" data-x="516" onmouseenter="hoverChartBar(this)">
                  <line x1="498" y1="145" x2="534" y2="145" stroke="#e52b2b" stroke-width="2"/>
                  <path d="M500,145 V180 M504,145 V180 M508,145 V180 M512,145 V180 M516,145 V180 M520,145 V180 M524,145 V180 M528,145 V180 M532,145 V180" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
                  <text x="516" y="202" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter">Sep</text>
                </g>

                <!-- Oct -->
                <g class="bar-group" data-month="Oct" data-val="$7,100" data-x="572" onmouseenter="hoverChartBar(this)">
                  <line x1="554" y1="160" x2="590" y2="160" stroke="#e52b2b" stroke-width="2"/>
                  <path d="M556,160 V180 M560,160 V180 M564,160 V180 M568,160 V180 M572,160 V180 M576,160 V180 M580,160 V180 M584,160 V180 M588,160 V180" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
                  <text x="572" y="202" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter">Oct</text>
                </g>

                <!-- Nov -->
                <g class="bar-group" data-month="Nov" data-val="$11,800" data-x="628" onmouseenter="hoverChartBar(this)">
                  <line x1="610" y1="130" x2="646" y2="130" stroke="#e52b2b" stroke-width="2"/>
                  <path d="M612,130 V180 M616,130 V180 M620,130 V180 M624,130 V180 M628,130 V180 M632,130 V180 M636,130 V180 M640,130 V180 M644,130 V180" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
                  <text x="628" y="202" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter">Nov</text>
                </g>

                <!-- Dec -->
                <g class="bar-group" data-month="Dec" data-val="$14,600" data-x="684" onmouseenter="hoverChartBar(this)">
                  <line x1="666" y1="110" x2="702" y2="110" stroke="#e52b2b" stroke-width="2"/>
                  <path d="M668,110 V180 M672,110 V180 M676,110 V180 M680,110 V180 M684,110 V180 M688,110 V180 M692,110 V180 M696,110 V180 M700,110 V180" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>
                  <text x="684" y="202" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter">Dec</text>
                </g>
              </svg>
            </div>
          </div>

          <!-- BOTTOM ROW: SEND MONEY + TOTAL INCOME -->
          <div class="bottom-cards-row">
            
            <!-- Send Money Card (White) -->
            <div class="dash-card card-send-money">
              <div class="dash-card-header" style="margin-bottom:12px">
                <span class="card-title">Send Money</span>
                <button class="card-dots-btn">···</button>
              </div>
              <div class="send-money-content">
                <!-- Add contact button -->
                <button class="btn-add-contact" id="btnAddContact" title="Add recipient">
                  <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
                </button>

                <!-- Avatars list -->
                <div class="contacts-avatar-list">
                  <div class="contact-avatar selected" onclick="selectContact(this, 'Esther Howard')">
                    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&auto=format&fit=crop&q=80" alt="Esther">
                  </div>
                  <div class="contact-avatar" onclick="selectContact(this, 'Leslie Alexander')">
                    <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&auto=format&fit=crop&q=80" alt="Leslie">
                  </div>
                  <div class="contact-avatar" onclick="selectContact(this, 'Bessie Cooper')">
                    <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?w=120&auto=format&fit=crop&q=80" alt="Bessie">
                  </div>
                  <div class="contact-avatar" onclick="selectContact(this, 'Guy Hawkins')">
                    <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=120&auto=format&fit=crop&q=80" alt="Guy">
                  </div>
                </div>

                <!-- Amount Input & Send Pill -->
                <div class="send-pill-box">
                  <input type="text" class="send-input-amount" id="inputSendAmount" value="$450 USD">
                  <button class="btn-send-action" id="btnSendMoney" title="Send now">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                  </button>
                </div>
              </div>
            </div>

            <!-- Total Income Card -->
            <div class="dash-card card-total-income">
              <div class="income-stat-wrap">
                <span class="income-title">Total Income</span>
                <span class="income-amount" id="displayTotalIncome">$7,890</span>
              </div>
              <!-- Sparkline Chart -->
              <svg class="sparkline-svg" viewBox="0 0 120 48">
                <defs>
                  <linearGradient id="sparklineGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="#eb4b32" stop-opacity="0.4"/>
                    <stop offset="100%" stop-color="#eb4b32" stop-opacity="0"/>
                  </linearGradient>
                </defs>
                <path d="M 0,38 Q 15,20 28,32 T 56,12 T 78,42 T 98,28 T 116,10" fill="none" stroke="#eb4b32" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="116" cy="10" r="3.5" fill="#eb4b32" stroke="#ffffff" stroke-width="1.5"/>
              </svg>
            </div>

          </div>

        </div>

        <!-- RIGHT COLUMN: AI INSIGHTS & NOTIFICATIONS -->
        <div class="side-column">

          <!-- AI INSIGHTS (FROSTED AMBIENT GLASS PANEL) -->
          <div class="card-ai-insights">
            <div class="ai-insights-header">
              <span class="ai-insights-title">AI INSIGHTS</span>
              <button class="card-dots-btn">···</button>
            </div>

            <!-- Card 1: Financial Health (Floating White) -->
            <div class="ai-health-box" onclick="expandInsight('health')">
              <div class="ai-health-title">Financial Health</div>
              <div class="ai-health-desc">
                Your financial health remains strong this week. Income continues to exceed expenses, helping you maintain positive cash flow and steady savings growth.
              </div>
            </div>

            <!-- Card 2: Financial Score -->
            <div class="ai-pill-card" onclick="expandInsight('score')">
              <div class="ai-pill-card-title">Financial Score: 86/100</div>
              <div class="ai-pill-card-sub">Your money habits are improving.</div>
            </div>

            <!-- Card 3: Monthly Forecast -->
            <div class="ai-pill-card" onclick="expandInsight('forecast')">
              <div class="ai-pill-card-title">Monthly Forecast</div>
              <div class="ai-pill-card-sub">You're on track for higher savings.</div>
            </div>

            <!-- Floating Prompt Bar (Ask Anything...) -->
            <form class="ai-prompt-bar" id="aiPromptForm" onsubmit="handleAiPrompt(event)">
              <div class="ai-sparkle-icon">
                <svg viewBox="0 0 24 24"><path d="M12 2L14.4 9.6L22 12L14.4 14.4L12 22L9.6 14.4L2 12L9.6 9.6L12 2Z"/></svg>
              </div>
              <input type="text" class="ai-prompt-input" id="aiInput" placeholder="Ask Anything..." autocomplete="off">
              <button type="submit" class="btn-ai-send" title="Send query">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
              </button>
            </form>
          </div>

          <!-- NOTIFICATIONS -->
          <div class="dash-card card-notifications">
            <div class="dash-card-header">
              <span class="card-title">Notifications</span>
              <button class="card-dots-btn">···</button>
            </div>

            <div class="notifications-list" id="notifList">
              <!-- Item 1 -->
              <div class="notification-item">
                <div class="notif-avatar">
                  <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&auto=format&fit=crop&q=80" alt="Esther">
                </div>
                <div class="notif-content">
                  <div class="notif-name">Esther Howard</div>
                  <div class="notif-desc">Request for you $120</div>
                </div>
                <div class="notif-time">1 Hour</div>
              </div>

              <!-- Item 2 -->
              <div class="notification-item">
                <div class="notif-avatar">
                  <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&auto=format&fit=crop&q=80" alt="Leslie">
                </div>
                <div class="notif-content">
                  <div class="notif-name">Leslie Alexander</div>
                  <div class="notif-desc">Request for you $120</div>
                </div>
                <div class="notif-time">1 Hour</div>
              </div>

              <!-- Item 3 -->
              <div class="notification-item">
                <div class="notif-avatar">
                  <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?w=120&auto=format&fit=crop&q=80" alt="Bessie">
                </div>
                <div class="notif-content">
                  <div class="notif-name">Bessie Cooper</div>
                  <div class="notif-desc">Request for you $120</div>
                </div>
                <div class="notif-time">1 Hour</div>
              </div>
            </div>

            <a href="javascript:void(0)" class="see-all-link" id="btnSeeAllNotifs">See All</a>
          </div>

        </div>

      </div>

    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div class="toast-popup" id="toastPopup">
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#22c55e" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
    <span id="toastMessage">Action completed successfully</span>
  </div>

  <script>
    // ============================================================
    // VIEW SWITCHER (DEVICE FRAME ⟷ FULLSCREEN)
    // ============================================================
    const btnDeviceView = document.getElementById('btnDeviceView');
    const btnFullscreenView = document.getElementById('btnFullscreenView');

    btnDeviceView.addEventListener('click', () => {
      document.body.classList.remove('fullscreen-mode');
      btnDeviceView.classList.add('active');
      btnFullscreenView.classList.remove('active');
    });

    btnFullscreenView.addEventListener('click', () => {
      document.body.classList.add('fullscreen-mode');
      btnFullscreenView.classList.add('active');
      btnDeviceView.classList.remove('active');
    });

    // ============================================================
    // TOAST SYSTEM
    // ============================================================
    function showToast(msg) {
      const toast = document.getElementById('toastPopup');
      const toastMsg = document.getElementById('toastMessage');
      if (toast && toastMsg) {
        toastMsg.textContent = msg;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 3000);
      }
    }

    // ============================================================
    // INTERACTIVE CHART HOVER
    // ============================================================
    const tooltip = document.getElementById('chartTooltip');
    const tooltipAmount = document.getElementById('tooltipAmount');
    const tooltipMonth = document.getElementById('tooltipMonth');

    function hoverChartBar(group) {
      document.querySelectorAll('.bar-group').forEach(g => {
        g.classList.remove('active');
        const line = g.querySelector('line');
        if (line) line.setAttribute('stroke', '#e52b2b');
      });

      group.classList.add('active');
      const activeLine = group.querySelector('line');
      if (activeLine) activeLine.setAttribute('stroke', '#ff5733');

      const val = group.dataset.val;
      const month = group.dataset.month;
      const xPercent = (parseFloat(group.dataset.x) / 740) * 100;

      if (tooltip) {
        tooltip.style.left = `${xPercent}%`;
        if (tooltipAmount) tooltipAmount.textContent = val;
        if (tooltipMonth) tooltipMonth.textContent = month;
      }
    }

    // ============================================================
    // SWITCH SCHEDULED SUBSCRIPTION
    // ============================================================
    function switchScheduleSub(name, amount, date) {
      const amountEl = document.getElementById('scheduleDisplayAmount');
      const dateEl = document.getElementById('scheduleDisplayDate');
      const iconWrap = document.getElementById('scheduleServiceIcon');

      if (amountEl) amountEl.textContent = amount;
      if (dateEl) dateEl.textContent = date;

      if (iconWrap) {
        if (name === 'Discord') {
          iconWrap.innerHTML = '<svg viewBox="0 0 24 24" width="20" height="20" fill="#5865f2"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.894.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028z"/></svg>';
        } else if (name === 'Netflix') {
          iconWrap.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="#e50914"><path d="M5.398 0v24L9.8 19.387V4.613L5.398 0zm8.798 0v24l4.402-4.613V4.613L14.196 0zm-4.398 5.766L14.2 24h-4.402L5.398 5.766h4.4z"/></svg>';
        } else {
          iconWrap.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="#ffffff"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>';
        }
      }
      showToast(`Showing subscription: ${name}`);
    }

    // ============================================================
    // SEND MONEY SELECTION & DISPATCH
    // ============================================================
    let activeRecipient = 'Esther Howard';

    function selectContact(el, name) {
      document.querySelectorAll('.contact-avatar').forEach(a => a.classList.remove('selected'));
      el.classList.add('selected');
      activeRecipient = name;
      showToast(`Recipient selected: ${name}`);
    }

    document.getElementById('btnSendMoney')?.addEventListener('click', () => {
      const amount = document.getElementById('inputSendAmount')?.value || '$450 USD';
      showToast(`🚀 Successfully sent ${amount} to ${activeRecipient}!`);
    });

    document.getElementById('btnAddContact')?.addEventListener('click', () => {
      showToast('Add new contact modal opened');
    });

    // ============================================================
    // EDIT DAILY LIMIT
    // ============================================================
    document.getElementById('btnEditLimit')?.addEventListener('click', () => {
      const newLimit = prompt('Enter new daily limit (e.g. $1,500):', '$1,500');
      if (newLimit) {
        document.getElementById('displayCurrentLimit').textContent = newLimit;
        showToast(`Daily limit updated to ${newLimit}`);
      }
    });

    // ============================================================
    // AI PROMPT ASSISTANT
    // ============================================================
    function handleAiPrompt(e) {
      e.preventDefault();
      const input = document.getElementById('aiInput');
      const q = input?.value?.trim();
      if (!q) return;

      input.value = '';
      showToast(`Analyzing: "${q}"...`);

      // Generate dynamic intelligent response in AI Health Box
      const healthDesc = document.querySelector('.ai-health-desc');
      const healthTitle = document.querySelector('.ai-health-title');

      setTimeout(() => {
        if (healthTitle) healthTitle.textContent = `AI Insight: "${q.slice(0, 24)}..."`;
        if (healthDesc) {
          healthDesc.textContent = `Based on your recent transactions, your cash flow is 14% higher than last month. Discretionary spending on subscriptions has reduced by $38. You are currently saving $620 per week.`;
        }
        showToast('AI analysis updated');
      }, 700);
    }

    function expandInsight(type) {
      if (type === 'health') {
        showToast('Detailed Financial Health breakdown opened');
      } else if (type === 'score') {
        showToast('Credit & spending score: 86/100 (Top 12% among peers)');
      } else if (type === 'forecast') {
        showToast('Next month projected surplus: +$1,840');
      }
    }

    // ============================================================
    // PERIOD & FILTER DROPDOWNS
    // ============================================================
    const periods = ['Weekly', 'Monthly', 'Quarterly', 'Yearly'];
    let pIdx = 1;

    document.getElementById('btnMonthly')?.addEventListener('click', () => {
      pIdx = (pIdx + 1) % periods.length;
      document.getElementById('labelPeriod').textContent = periods[pIdx];
      showToast(`Timeframe changed to ${periods[pIdx]}`);
    });

    document.getElementById('btnFilter')?.addEventListener('click', () => {
      showToast('Filters: All channels, Active cards, Invoices');
    });

    // Nav tabs switcher
    document.querySelectorAll('.nav-tab-item').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.nav-tab-item').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        showToast(`Switched view to: ${btn.textContent.trim()}`);
      });
    });

    document.getElementById('btnSeeAllNotifs')?.addEventListener('click', () => {
      showToast('All 18 recent notifications loaded');
    });

    document.getElementById('btnNotification')?.addEventListener('click', () => {
      showToast('3 unread alerts: Requests pending approval');
    });
  </script>
</body>
</html>
"""

# Write to dashboard.html, glass-ui.html, and index.html
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(dashboard_html)

with open("glass-ui.html", "w", encoding="utf-8") as f:
    f.write(dashboard_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(dashboard_html)

print("Dashboard files generated successfully.")
