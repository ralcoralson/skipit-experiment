# Python script to generate the complete, pristine index.html matching SkipIt's official palette and Dribbble layout inspiration

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>skipit — Skip buying. Rent smarter.</title>
  <meta name="description" content="SkipIt is a peer-to-peer rental marketplace where you can rent products from real people nearby. Skip the cost of ownership. Rent what you need, earn from what you own.">
  <meta name="theme-color" content="#0044FF">
  <meta property="og:title" content="skipit — Skip buying. Rent smarter.">
  <meta property="og:description" content="Peer-to-peer rental marketplace. Rent what you need, earn from what you own.">
  <meta property="og:type" content="website">
  <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
  <link rel="stylesheet" href="styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
</head>
<body>

<!-- ============================================================
     SEARCH MODAL
     ============================================================ -->
<div class="search-overlay" id="searchOverlay" role="dialog" aria-label="Search">
  <div class="search-modal">
    <form id="searchForm">
      <div class="search-input-wrap">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
        </svg>
        <input id="searchInput" type="text" placeholder="Search cameras, laptops, tools, consoles..." autocomplete="off">
      </div>
    </form>
    <div class="search-hints">
      <p>Popular searches</p>
      <div class="search-quick-cats">
        <button class="search-quick-cat">Camera</button>
        <button class="search-quick-cat">PlayStation 5</button>
        <button class="search-quick-cat">Projector</button>
        <button class="search-quick-cat">Power Drill</button>
        <button class="search-quick-cat">Mountain Bike</button>
        <button class="search-quick-cat">DJ Speaker</button>
        <button class="search-quick-cat">Camping Tent</button>
      </div>
    </div>
  </div>
</div>

<!-- ============================================================
     LISTING DETAIL MODAL (PREMIUM E-COMMERCE COMPOSITION)
     ============================================================ -->
<div class="listing-overlay" id="listingOverlay" role="dialog" aria-label="Listing detail">
  <div class="listing-modal">
    <button class="listing-modal-close" id="lmClose" aria-label="Close">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg>
    </button>
    <div class="listing-modal-image">
      <img id="lmImage" src="" alt="Product" loading="eager">
    </div>
    <div class="listing-modal-body">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:12px;flex-wrap:wrap">
        <span class="badge badge--green">
          <svg viewBox="0 0 8 8" fill="currentColor" style="width:8px;height:8px"><circle cx="4" cy="4" r="3"/></svg>
          Available Now
        </span>
        <span class="badge badge--blue" id="lmCategoryBadge">Photography</span>
      </div>
      <h2 id="lmTitle" style="font-family:var(--font-sans);font-size:1.375rem;font-weight:800;letter-spacing:-.025em;line-height:1.2;margin-bottom:6px"></h2>
      
      <div style="display:flex;align-items:center;gap:14px;font-size:.875rem;color:var(--text-muted);margin-bottom:12px">
        <div style="display:flex;align-items:center;gap:4px">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:14px;height:14px;color:var(--text-muted)"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <span id="lmLocation"></span>
        </div>
        <div style="display:flex;align-items:center;gap:4px;font-weight:700;color:var(--text-secondary)">
          <svg viewBox="0 0 24 24" style="width:13px;height:13px;color:#f59e0b;fill:#f59e0b"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <span id="lmRating">4.9 (34 reviews)</span>
        </div>
      </div>

      <div class="lm-price-row">
        <span class="lm-price-main" id="lmPrice"></span>
        <span class="lm-price-per">/ day</span>
      </div>
      
      <p id="lmDesc" style="font-size:.9375rem;color:var(--text-secondary);line-height:1.6;margin-bottom:16px"></p>

      <!-- Verified Owner Snippet -->
      <div class="lm-owner-row">
        <div class="lm-owner-avatar" id="lmOwnerInitial">R</div>
        <div>
          <div class="lm-owner-name" id="lmOwnerName"></div>
          <div class="lm-owner-sub">Verified Owner · SkipIt Member · ID Checked</div>
        </div>
        <div style="margin-left:auto;display:flex;align-items:center;gap:4px;font-size:.8125rem;font-weight:700;color:var(--green-600)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:14px;height:14px"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          Verified
        </div>
      </div>

      <!-- Rental Duration Selector -->
      <div style="margin:16px 0 12px">
        <label style="display:block;font-size:0.8125rem;font-weight:700;color:var(--text-primary);margin-bottom:8px">Select Rental Duration</label>
        <div class="lm-duration-selector" id="lmDurationSelector">
          <button type="button" class="duration-pill active" data-days="1">1 Day</button>
          <button type="button" class="duration-pill" data-days="3">3 Days</button>
          <button type="button" class="duration-pill" data-days="7">7 Days (10% off)</button>
          <button type="button" class="duration-pill" data-days="14">14 Days (15% off)</button>
        </div>
      </div>

      <!-- Protection Plan Add-on -->
      <div style="margin:14px 0">
        <label style="display:block;font-size:0.8125rem;font-weight:700;color:var(--text-primary);margin-bottom:8px">Damage Protection Plan (Optional)</label>
        <div class="lm-protection-selector" id="lmProtectionSelector">
          <label class="protection-pill active">
            <input type="radio" name="lmProtection" value="0" checked>
            <span>None (₹0)</span>
          </label>
          <label class="protection-pill">
            <input type="radio" name="lmProtection" value="49">
            <span>Basic (+₹49/d)</span>
          </label>
          <label class="protection-pill">
            <input type="radio" name="lmProtection" value="99">
            <span>Premium (+₹99/d)</span>
          </label>
        </div>
      </div>

      <!-- Price Breakdown Panel -->
      <div class="lm-breakdown-box">
        <div class="lm-breakdown-row">
          <span>Rental fee (<span id="lmDaysLabel">1 day</span>)</span>
          <span id="lmRentalSubtotal">₹799</span>
        </div>
        <div class="lm-breakdown-row" id="lmProtectionRow" style="display:none">
          <span>Protection plan</span>
          <span id="lmProtectionFee">₹0</span>
        </div>
        <div class="lm-breakdown-row">
          <span style="display:flex;align-items:center;gap:6px">
            Security Deposit
            <span style="font-size:0.6875rem;background:var(--blue-100);color:var(--brand);padding:2px 6px;border-radius:4px;font-weight:700">100% Refundable</span>
          </span>
          <span id="lmDeposit">₹5,000</span>
        </div>
        <div class="lm-divider" style="margin:10px 0"></div>
        <div class="lm-breakdown-total">
          <span>Total due today</span>
          <span id="lmTotalPayable">₹5,799</span>
        </div>
      </div>

      <div style="background:var(--bg-subtle);border-radius:var(--radius-md);padding:10px 14px;font-size:.78rem;color:var(--text-secondary);margin:14px 0;line-height:1.5">
        <strong style="color:var(--text-primary)">Direct Handover:</strong> Pickup and return are coordinated directly with the owner per the SkipIt rental agreement. The security deposit is held in escrow and released immediately upon return.
      </div>

      <button class="btn btn--primary btn--lg" style="width:100%;justify-content:center" id="lmRentBtn" onclick="handleRentRequest()">
        Rent Now
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:16px;height:16px"><path d="m5 12h14M12 5l7 7-7 7"/></svg>
      </button>

      <div id="lmRentSuccess" style="display:none;background:var(--green-50);border:1px solid #bbf7d0;color:var(--green-600);border-radius:var(--radius-md);padding:14px;margin-top:12px;font-size:0.875rem;font-weight:600;text-align:center">
        Rental request confirmed! The owner has been notified and will coordinate pickup with you.
      </div>
      <p style="font-size:.75rem;color:var(--text-muted);text-align:center;margin-top:8px">Protected by SkipIt Rental Escrow &amp; Trust Guarantee.</p>
    </div>
  </div>
</div>

<!-- ============================================================
     MOBILE STICKY CTA
     ============================================================ -->
<div class="mobile-cta-bar">
  <a href="#marketplace" class="btn btn--outline btn--sm">Explore</a>
  <a href="#for-owners" class="btn btn--primary btn--sm">List an Item</a>
</div>

<!-- ============================================================
     NAVBAR
     ============================================================ -->
<nav id="navbar" role="navigation" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="#hero" class="nav-logo" aria-label="SkipIt home">
      <div class="nav-logo-icon">
        <svg viewBox="0 0 38 38" fill="white" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 6C4 4.895 4.895 4 6 4H24C25.105 4 26 4.895 26 6V15H16C14.895 15 14 15.895 14 17V26H6C4.895 26 4 25.105 4 24V6Z"/>
          <rect x="17" y="17" width="17" height="9" rx="2"/>
          <circle cx="10" cy="32" r="4"/>
          <circle cx="24" cy="32" r="4"/>
        </svg>
      </div>
      <span class="nav-logo-text">skipit</span>
    </a>
    <div class="nav-links">
      <a href="#marketplace" class="nav-link">Marketplace</a>
      <a href="#how-it-works" class="nav-link">How It Works</a>
      <a href="#for-owners" class="nav-link">List an Item</a>
      <a href="#trust" class="nav-link">Safety</a>
      <a href="#cta-section" class="nav-link">About</a>
    </div>
    <div class="nav-actions">
      <button class="nav-search-btn js-open-search" aria-label="Search" id="navSearchBtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
        </svg>
      </button>
      <a href="auth.html" class="nav-login" id="navLoginBtn">Log in</a>
      <a href="#for-owners" class="btn btn--primary btn--sm">List an Item</a>
    </div>
    <button class="nav-hamburger" id="hamburger" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>

<!-- Mobile Nav Panel -->
<div class="mobile-nav" id="mobileNav">
  <div class="mobile-nav-links">
    <a href="#marketplace" class="mobile-nav-link">Marketplace</a>
    <a href="#how-it-works" class="mobile-nav-link">How It Works</a>
    <a href="#for-owners" class="mobile-nav-link">List an Item</a>
    <a href="#trust" class="mobile-nav-link">Safety &amp; Trust</a>
    <a href="#protection" class="mobile-nav-link">Protection Plans</a>
    <a href="#cta-section" class="mobile-nav-link">About SkipIt</a>
  </div>
  <div class="mobile-nav-actions" id="mobileNavActions">
    <a href="auth.html" class="btn btn--outline" id="mobileNavLoginBtn" style="justify-content:center">Log in</a>
    <a href="#for-owners" class="btn btn--primary" style="justify-content:center">List an Item</a>
  </div>
</div>

<main>

<!-- ============================================================
     1. HERO
     ============================================================ -->
<section id="hero" aria-label="Hero">
  <div class="hero-bg-pattern"></div>
  <div class="hero-inner">
    <!-- Left Content -->
    <div class="hero-left">
      <div class="hero-badge reveal">
        <div class="hero-badge-dot"></div>
        Peer-to-peer rental marketplace · India
      </div>
      <h1 class="hero-headline reveal reveal-delay-1">
        Why buy it when you can <span>SkipIt?</span>
      </h1>
      <p class="hero-subheadline reveal reveal-delay-2">
        Rent what you need. Use it when you need it. Return it when you're done.
      </p>
      <p class="hero-description reveal reveal-delay-3">
        SkipIt connects you with verified local owners to rent cameras, gaming consoles, electronics, tools, and outdoor gear — skip the high upfront cost and ownership burden.
      </p>
      <div class="hero-ctas reveal reveal-delay-4">
        <a href="#marketplace" class="btn btn--primary btn--lg" id="hero-explore-btn">
          Explore Rentals
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:16px;height:16px"><path d="m5 12h14M12 5l7 7-7 7"/></svg>
        </a>
        <a href="#for-owners" class="btn btn--outline btn--lg" id="hero-list-btn">List an Item</a>
      </div>
      <div class="hero-trust reveal reveal-delay-5">
        <div class="hero-trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          Verified owners
        </div>
        <div class="hero-trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          Secure payments
        </div>
        <div class="hero-trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          Protection plans
        </div>
      </div>
    </div>

    <!-- Right Image Grid -->
    <div class="hero-right reveal reveal-delay-2">
      <div class="hero-img-card hero-img-card--tall">
        <img src="images/product_camera.jpg" alt="Sony Alpha mirrorless camera available for rent" loading="eager">
      </div>
      <div class="hero-img-card" style="height:190px">
        <img src="images/product_ps5.jpg" alt="PlayStation 5 console available for rent" loading="eager">
      </div>
      <div class="hero-img-card" style="height:190px">
        <img src="images/product_projector.jpg" alt="Portable mini projector available for rent" loading="eager">
      </div>

      <!-- Floating Marketplace Badges -->
      <div class="hero-floating-card hero-fc--price">
        <div class="hero-floating-card-icon" style="background:var(--brand-light)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:16px;height:16px;color:var(--brand)"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <div>
          <div style="font-size:.7rem;color:var(--text-muted);font-weight:600">Starting from</div>
          <div style="color:var(--text-primary);font-weight:800">₹199 / day</div>
        </div>
      </div>

      <div class="hero-floating-card hero-fc--available">
        <div class="hero-floating-card-icon" style="background:var(--green-50)">
          <div style="width:8px;height:8px;background:var(--green-500);border-radius:50%"></div>
        </div>
        <div>
          <div style="font-size:.7rem;color:var(--text-muted);font-weight:600">Near you</div>
          <div style="color:var(--text-primary);font-weight:800">Available nearby</div>
        </div>
      </div>

      <div class="hero-floating-card hero-fc--verified">
        <div class="hero-floating-card-icon" style="background:var(--blue-50)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:16px;height:16px;color:var(--brand)"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <div>
          <div style="font-size:.7rem;color:var(--text-muted);font-weight:600">Owner status</div>
          <div style="color:var(--green-600);font-weight:800">Verified member</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     2. WORKFLOW (01 TO 05)
     ============================================================ -->
<section id="how-it-works" class="section" aria-label="How SkipIt works">
  <div class="container">
    <div class="section-header reveal">
      <span class="eyebrow">How SkipIt Works</span>
      <h2>Rent in five simple steps.</h2>
      <p>From discovering gear to returning it — our verified peer-to-peer workflow makes renting effortless, safe, and transparent.</p>
    </div>

    <div class="steps-grid">
      <div class="step-card reveal">
        <div class="step-num">01</div>
        <div class="step-icon-wrap">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
        </div>
        <h3>Discover</h3>
        <p>Browse high-demand gear from verified owners nearby with transparent daily rates and real-time availability.</p>
      </div>

      <div class="step-card reveal reveal-delay-1">
        <div class="step-num">02</div>
        <div class="step-icon-wrap">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <h3>Verify</h3>
        <p>Fast 1-minute government ID &amp; KYC check builds peer-to-peer accountability and protects our entire community.</p>
      </div>

      <div class="step-card reveal reveal-delay-2">
        <div class="step-num">03</div>
        <div class="step-icon-wrap">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>
        </div>
        <h3>Book &amp; Pay</h3>
        <p>Select your rental duration, review deposit terms, and complete secure payment held safely in platform escrow.</p>
      </div>

      <div class="step-card reveal reveal-delay-3">
        <div class="step-num">04</div>
        <div class="step-icon-wrap">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
        </div>
        <h3>Rent &amp; Use</h3>
        <p>Coordinate convenient handover directly with the verified owner and put professional gear to work on your terms.</p>
      </div>

      <div class="step-card reveal reveal-delay-4">
        <div class="step-num">05</div>
        <div class="step-icon-wrap">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 .49-3.25"/></svg>
        </div>
        <h3>Return &amp; Review</h3>
        <p>Return the item in agreed condition, receive your instant security deposit refund, and leave a community review.</p>
      </div>
    </div>

    <!-- OWNER SIDE BANNER -->
    <div class="owner-banner reveal">
      <div>
        <h3>Own it? Put it to work.</h3>
        <p>Have something sitting unused? List it on SkipIt, set your daily price, manage availability, and turn idle assets into recurring income on your schedule.</p>
      </div>
      <a href="auth.html?mode=signup" class="btn btn--outline btn--lg">Start Listing</a>
    </div>
  </div>
</section>

<!-- ============================================================
     3. MARKETPLACE PREVIEW
     ============================================================ -->
<section id="marketplace" class="section" aria-label="Marketplace">
  <div class="container">
    <div class="section-header reveal">
      <span class="eyebrow">Live Marketplace</span>
      <h2>Things you could rent instead of buying.</h2>
      <p>Browse real categories. Real products. From verified people in your community.</p>
    </div>

    <!-- Category Filter (Editorial Pills with Icons and Counts) -->
    <div class="categories-filter reveal">
      <button class="cat-btn active" data-cat="all">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="cat-icon"><circle cx="12" cy="12" r="3"/><circle cx="19" cy="5" r="2"/><circle cx="5" cy="5" r="2"/><circle cx="19" cy="19" r="2"/><circle cx="5" cy="19" r="2"/></svg>
        <span>All</span>
        <span class="cat-count">8</span>
      </button>
      <button class="cat-btn" data-cat="electronics">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="cat-icon"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
        <span>Electronics</span>
        <span class="cat-count">1</span>
      </button>
      <button class="cat-btn" data-cat="gaming">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="cat-icon"><rect x="2" y="6" width="20" height="12" rx="3"/><path d="M6 12h4m-2-2v4"/><circle cx="15" cy="11" r="1"/><circle cx="18" cy="13" r="1"/></svg>
        <span>Gaming</span>
        <span class="cat-count">2</span>
      </button>
      <button class="cat-btn" data-cat="photography">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="cat-icon"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
        <span>Photography</span>
        <span class="cat-count">1</span>
      </button>
      <button class="cat-btn" data-cat="tools">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="cat-icon"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
        <span>Tools</span>
        <span class="cat-count">1</span>
      </button>
      <button class="cat-btn" data-cat="vehicles">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="cat-icon"><circle cx="18.5" cy="17.5" r="3.5"/><circle cx="5.5" cy="17.5" r="3.5"/><circle cx="15" cy="5" r="1"/><path d="M12 17.5V14l-3-3 4-3 2 3h2"/></svg>
        <span>Vehicles</span>
        <span class="cat-count">1</span>
      </button>
      <button class="cat-btn" data-cat="sports">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="cat-icon"><path d="M19 21l-7-14-7 14"/><path d="M10 21l2-4 2 4"/></svg>
        <span>Sports</span>
        <span class="cat-count">1</span>
      </button>
      <button class="cat-btn" data-cat="events">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="cat-icon"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
        <span>Events</span>
        <span class="cat-count">1</span>
      </button>
    </div>

    <!-- Product Grid — populated dynamically by main.js -->
    <div class="listings-grid" id="listingsGrid"></div>
  </div>
</section>

<!-- ============================================================
     4. THE PROBLEM
     ============================================================ -->
<section id="the-problem" class="section" aria-label="The problem with buying">
  <div class="container">
    <div class="problem-grid">
      <div class="problem-left">
        <h2 class="reveal">Most things we buy spend more time sitting unused.</h2>
        <p class="reveal reveal-delay-1">
          People purchase expensive products for occasional use. After the need disappears, those products sit unused while others spend money buying the same things. It's an inefficient cycle — for individuals, and for the economy.
        </p>
        <div class="problem-pills">
          <div class="problem-pill reveal reveal-delay-2">
            <div class="problem-pill-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            </div>
            <div class="problem-pill-content">
              <h4>High upfront cost</h4>
              <p>Buying means paying the full price upfront — even for something you'll only use a few times.</p>
            </div>
          </div>
          <div class="problem-pill reveal reveal-delay-3">
            <div class="problem-pill-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            </div>
            <div class="problem-pill-content">
              <h4>Low utilization</h4>
              <p>Most purchased items are used only occasionally. The rest of the time, they sit idle.</p>
            </div>
          </div>
          <div class="problem-pill reveal reveal-delay-4">
            <div class="problem-pill-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="21 8 21 21 3 21 3 8"/><rect x="1" y="3" width="22" height="5"/><line x1="10" y1="12" x2="14" y2="12"/></svg>
            </div>
            <div class="problem-pill-content">
              <h4>Unused products collecting dust</h4>
              <p>After the need passes, the product ends up stored away — a sunk cost.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Comparison -->
      <div class="problem-right reveal reveal-delay-1">
        <div class="comparison-card comparison-card--buy">
          <div class="comparison-label">The old way — Buy</div>
          <div class="comparison-flow">
            <div class="flow-box">Pay full price</div>
            <div class="flow-arrow">→</div>
            <div class="flow-box">Use occasionally</div>
            <div class="flow-arrow">→</div>
            <div class="flow-box">Store it</div>
            <div class="flow-arrow">→</div>
            <div class="flow-box">Repeat</div>
          </div>
        </div>
        <div class="comparison-card comparison-card--rent">
          <div class="comparison-label">The smarter way — Rent via SkipIt</div>
          <div class="comparison-flow">
            <div class="flow-box">Pay only when needed</div>
            <div class="flow-arrow">→</div>
            <div class="flow-box">Use it</div>
            <div class="flow-arrow">→</div>
            <div class="flow-box">Return it</div>
          </div>
        </div>
        <div style="padding:24px;background:rgba(0,68,255,.1);border:1px solid rgba(0,68,255,.25);border-radius:var(--radius-xl)">
          <p style="font-size:.9375rem;color:rgba(255,255,255,.8);line-height:1.7">
            <strong style="color:var(--blue-300)">The insight:</strong> You don't need to own something to access it. You just need to know someone who has it — and a marketplace you can trust.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     5. THE SOLUTION
     ============================================================ -->
<section id="solution" class="section" aria-label="SkipIt solution">
  <div class="container">
    <div class="section-header reveal">
      <span class="eyebrow">The SkipIt Advantage</span>
      <h2>Skip the ownership. Keep the access.</h2>
      <p>SkipIt creates a marketplace where people access products at a fraction of the purchase cost, owners monetize idle assets, and communities share resources more efficiently.</p>
    </div>

    <!-- Benefits Grid -->
    <div class="solution-benefits">
      <div class="solution-benefit reveal">
        <div class="solution-benefit-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <h4>Lower upfront cost</h4>
        <p>Access products at a fraction of the purchase price.</p>
      </div>
      <div class="solution-benefit reveal reveal-delay-1">
        <div class="solution-benefit-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
        </div>
        <h4>Community sharing</h4>
        <p>Products in communities get utilized, not stored away.</p>
      </div>
      <div class="solution-benefit reveal reveal-delay-2">
        <div class="solution-benefit-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <h4>Owners earn</h4>
        <p>Turn unused assets into a source of supplemental income.</p>
      </div>
      <div class="solution-benefit reveal reveal-delay-3">
        <div class="solution-benefit-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
        </div>
        <h4>Higher utilization</h4>
        <p>Products get used instead of sitting idle in storage.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     6. TRUST & SAFETY (4 CORE PILLARS)
     ============================================================ -->
<section id="trust" class="section" aria-label="Trust and safety">
  <div class="container">
    <div class="section-header reveal">
      <span class="eyebrow">Trust &amp; Safety Infrastructure</span>
      <h2>Built around uncompromising trust.</h2>
      <p>Peer-to-peer rentals work only when both sides trust the platform. SkipIt is built with four robust layers of trust mechanisms designed specifically for the Indian rental market.</p>
    </div>

    <div class="trust-grid">
      <div class="trust-card reveal">
        <div class="trust-card-pillar">Pillar 01</div>
        <div class="trust-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        </div>
        <h3>Identity &amp; KYC Verification</h3>
        <p>Mandatory government ID and KYC verification for both renters and owners prior to platform access. Real-name verification establishes accountability across the community.</p>
      </div>

      <div class="trust-card reveal reveal-delay-1">
        <div class="trust-card-pillar">Pillar 02</div>
        <div class="trust-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <h3>Listing Integrity &amp; Moderation</h3>
        <p>Automated checks screen listings for prohibited items, duplicate uploads, and anomalous descriptions. Listing imagery and pricing outliers are moderated before going live.</p>
      </div>

      <div class="trust-card reveal reveal-delay-2">
        <div class="trust-card-pillar">Pillar 03</div>
        <div class="trust-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
        </div>
        <h3>Transaction Protection &amp; Escrow</h3>
        <p>Payments and deposits are processed safely through platform escrow. Security deposits are held separately and refunded automatically upon successful return.</p>
      </div>

      <div class="trust-card reveal reveal-delay-3">
        <div class="trust-card-pillar">Pillar 04</div>
        <div class="trust-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
        </div>
        <h3>Risk Controls &amp; Fraud Prevention</h3>
        <p>Continuous algorithmic monitoring flags suspicious patterns, unauthorized multiple bookings, and fraud indicators, backed by rapid dispute resolution support.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     7. PROTECTION PLANS
     ============================================================ -->
<section id="protection" class="section" aria-label="Protection plans">
  <div class="container">
    <div class="section-header reveal">
      <span class="eyebrow">Protection system</span>
      <h2>Protection for every rental.</h2>
      <p>SkipIt offers optional protection plans designed to reduce risk associated with accidental damage or eligible rental incidents. Plans are add-ons — not mandatory.</p>
    </div>

    <div class="plans-grid">
      <!-- Basic -->
      <div class="plan-card reveal">
        <div class="plan-name">Plan</div>
        <div class="plan-tier">Basic</div>
        <div class="plan-description">Essential protection for everyday rentals. Provides a baseline level of coverage for eligible incidents.</div>
        <div class="plan-features">
          <div class="plan-feature">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Coverage for eligible incidents
          </div>
          <div class="plan-feature">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Basic accidental damage protection
          </div>
          <div class="plan-feature">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Standard claim process
          </div>
        </div>
      </div>

      <!-- Premium -->
      <div class="plan-card plan-card--featured reveal reveal-delay-2">
        <div class="plan-badge">Most Popular</div>
        <div class="plan-name">Plan</div>
        <div class="plan-tier">Premium</div>
        <div class="plan-description">Enhanced protection for higher-value rentals. More coverage, faster response, and broader incident eligibility.</div>
        <div class="plan-features">
          <div class="plan-feature">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Expanded incident eligibility
          </div>
          <div class="plan-feature">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Enhanced accidental damage cover
          </div>
          <div class="plan-feature">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Priority claim processing
          </div>
          <div class="plan-feature">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Dedicated support
          </div>
        </div>
      </div>

      <!-- Platinum -->
      <div class="plan-card reveal reveal-delay-4">
        <div class="plan-name">Plan</div>
        <div class="plan-tier">Platinum</div>
        <div class="plan-description">Maximum available protection for high-value items and rental scenarios where risk is a primary concern.</div>
        <div class="plan-features">
          <div class="plan-feature">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Maximum coverage scope
          </div>
          <div class="plan-feature">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Broadest incident eligibility
          </div>
          <div class="plan-feature">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Expedited claim resolution
          </div>
          <div class="plan-feature">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            Premium 1:1 support
          </div>
        </div>
      </div>
    </div>

    <!-- Deposit Notice -->
    <div class="deposit-notice reveal">
      <p>
        <strong>About rental deposits:</strong> Deposits may be required depending on the item, category, owner requirements, and risk level. Deposits are a <strong>security mechanism</strong> — they are held separately in escrow and returned after a successful rental. They are not platform revenue.
      </p>
    </div>
  </div>
</section>

<!-- ============================================================
     8. FOR OWNERS
     ============================================================ -->
<section id="for-owners" class="section" aria-label="For owners">
  <div class="container">
    <div class="split-section">
      <div class="split-content reveal">
        <span style="display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--brand);background:var(--brand-light);padding:5px 12px;border-radius:var(--radius-full);margin-bottom:16px">For Owners</span>
        <h2>Your unused stuff could be earning.</h2>
        <p>Have something sitting unused? List it on SkipIt and turn idle assets into income. You set the price, manage availability, and earn whenever someone rents your item.</p>
        <div class="benefits-list">
          <div class="benefit-item">
            <div class="benefit-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
            </div>
            <div class="benefit-text">
              <h4>Create listings easily</h4>
              <p>List your item with photos, description, and pricing in just a few steps.</p>
            </div>
          </div>
          <div class="benefit-item">
            <div class="benefit-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            </div>
            <div class="benefit-text">
              <h4>Set your rental price</h4>
              <p>You decide the daily rate. Earn from every approved rental.</p>
            </div>
          </div>
          <div class="benefit-item">
            <div class="benefit-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            </div>
            <div class="benefit-text">
              <h4>Manage availability</h4>
              <p>Control when your item is available and review rental requests before approving.</p>
            </div>
          </div>
          <div class="benefit-item">
            <div class="benefit-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="m9 12 2 2 4-4"/></svg>
            </div>
            <div class="benefit-text">
              <h4>Build your reputation</h4>
              <p>Reviews from renters help you build credibility and attract more bookings.</p>
            </div>
          </div>
        </div>
        <a href="auth.html?mode=signup" class="btn btn--primary btn--lg">
          Start Listing
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:16px;height:16px"><path d="m5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>

      <div class="split-visual reveal reveal-delay-2">
        <div class="split-visual-img">
          <img src="images/product_camera.jpg" alt="Camera listing on SkipIt" loading="lazy">
        </div>
        <div style="margin-top:20px;padding:20px;background:var(--brand-light);border-radius:var(--radius-xl);border:1px solid var(--blue-200)">
          <div style="font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--brand);margin-bottom:12px">Example listing</div>
          <div style="font-family:var(--font-sans);font-size:1.0625rem;font-weight:700;color:var(--text-primary);margin-bottom:4px">Sony Alpha Mirrorless Camera</div>
          <div style="font-size:.875rem;color:var(--text-secondary);margin-bottom:12px">Listed by Rahul M. · Bengaluru</div>
          <div style="display:flex;align-items:center;justify-content:space-between">
            <div style="font-family:var(--font-sans);font-size:1.375rem;font-weight:900;color:var(--text-primary)">₹799<span style="font-size:.875rem;font-weight:500;color:var(--text-muted)">/day</span></div>
            <span style="background:var(--green-50);color:var(--green-600);font-size:.75rem;font-weight:700;padding:4px 10px;border-radius:var(--radius-full);border:1px solid rgba(34,197,94,0.2)">Available</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     9. FOR RENTERS
     ============================================================ -->
<section id="for-renters" class="section" aria-label="For renters">
  <div class="container">
    <div class="split-section">
      <!-- Visual first on this section -->
      <div class="split-visual reveal">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
          <div style="border-radius:var(--radius-xl);overflow:hidden">
            <img src="images/product_bike.jpg" alt="Bike rental" loading="lazy" style="width:100%;height:180px;object-fit:cover">
          </div>
          <div style="border-radius:var(--radius-xl);overflow:hidden">
            <img src="images/product_tent.jpg" alt="Tent rental" loading="lazy" style="width:100%;height:180px;object-fit:cover">
          </div>
        </div>
        <div style="margin-top:12px;padding:20px;background:#ffffff;border-radius:var(--radius-xl);border:1px solid var(--border);display:flex;align-items:center;gap:16px">
          <div style="width:48px;height:48px;border-radius:var(--radius-lg);background:var(--brand-light);border:1px solid var(--blue-200);display:flex;align-items:center;justify-content:center;flex-shrink:0">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:22px;height:22px;color:var(--brand)" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <div>
            <div style="font-family:var(--font-sans);font-weight:700;font-size:.9375rem">Flexible rental periods</div>
            <div style="font-size:.875rem;color:var(--text-secondary)">Rent for a day, a weekend, or longer — on your schedule.</div>
          </div>
        </div>
      </div>

      <div class="split-content reveal reveal-delay-2">
        <span style="display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--brand);background:var(--brand-light);padding:5px 12px;border-radius:var(--radius-full);margin-bottom:16px">For Renters</span>
        <h2>Get access without the commitment.</h2>
        <p>Stop buying things you'll only use a handful of times. SkipIt gives you access to a wide range of products from verified owners, at a fraction of the purchase cost.</p>
        <div class="benefits-list">
          <div class="benefit-item">
            <div class="benefit-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            </div>
            <div class="benefit-text">
              <h4>Lower upfront cost</h4>
              <p>Pay only for the duration you actually need the product.</p>
            </div>
          </div>
          <div class="benefit-item">
            <div class="benefit-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            </div>
            <div class="benefit-text">
              <h4>Discover products nearby</h4>
              <p>Browse listings from people in your city and neighbourhood.</p>
            </div>
          </div>
          <div class="benefit-item">
            <div class="benefit-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            </div>
            <div class="benefit-text">
              <h4>Verified users</h4>
              <p>All owners are verified. Ratings and reviews build a reliable trust layer.</p>
            </div>
          </div>
          <div class="benefit-item">
            <div class="benefit-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            </div>
            <div class="benefit-text">
              <h4>Flexible rental periods</h4>
              <p>Choose the exact dates you need — no long-term commitment required.</p>
            </div>
          </div>
        </div>
        <a href="#marketplace" class="btn btn--primary btn--lg">
          Explore Rentals
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:16px;height:16px"><path d="m5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     10. BUSINESS MODEL
     ============================================================ -->
<section id="business-model" class="section" aria-label="Business model">
  <div class="container">
    <div class="section-header reveal">
      <span class="eyebrow">How SkipIt Earns</span>
      <h2>A marketplace designed to scale.</h2>
      <p>SkipIt generates revenue primarily through a transparent commission on successful rental transactions.</p>
    </div>

    <div class="biz-grid">
      <!-- Revenue -->
      <div class="biz-card biz-card--revenue reveal">
        <div class="biz-card-label">Platform Revenue</div>
        <div class="commission-highlight">
          <span class="commission-percent">12</span>
          <span class="commission-suffix">%</span>
        </div>
        <h3>Commission per transaction</h3>
        <p>SkipIt earns a 12% commission on every successful rental transaction completed through the platform. This is our primary revenue mechanism.</p>
        <div class="revenue-items">
          <div class="rev-item"><div class="rev-item-dot"></div>Charged on rental value only</div>
          <div class="rev-item"><div class="rev-item-dot"></div>Optional protection plan add-on fees</div>
          <div class="rev-item"><div class="rev-item-dot"></div>No hidden platform or listing fees</div>
        </div>
      </div>
      <!-- Deposit -->
      <div class="biz-card biz-card--deposit reveal reveal-delay-2">
        <div class="biz-card-label">Security Mechanism</div>
        <h3>Rental deposits — not platform revenue</h3>
        <p style="margin-bottom:16px">Rental deposits may be required for certain items, categories, or risk levels. Here is the clear distinction:</p>
        <div style="display:flex;flex-direction:column;gap:12px">
          <div style="padding:16px;background:var(--bg-subtle);border-radius:var(--radius-lg);border:1px solid var(--border)">
            <div style="font-family:var(--font-sans);font-size:.875rem;font-weight:700;color:var(--text-primary);margin-bottom:4px">Deposits are held security</div>
            <div style="font-size:.875rem;color:var(--text-secondary);line-height:1.5">They are held in platform escrow and returned immediately upon completed rental. They are not earned by SkipIt.</div>
          </div>
          <div style="padding:16px;background:var(--bg-subtle);border-radius:var(--radius-lg);border:1px solid var(--border)">
            <div style="font-family:var(--font-sans);font-size:.875rem;font-weight:700;color:var(--text-primary);margin-bottom:4px">Commission is platform revenue</div>
            <div style="font-size:.875rem;color:var(--text-secondary);line-height:1.5">Only the 12% transaction fee on the rental value is retained by SkipIt as platform earnings.</div>
          </div>
        </div>
      </div>
    </div>

    <div style="margin-top:32px;padding:24px 32px;background:var(--bg-subtle);border:1px solid var(--border);border-radius:var(--radius-xl);text-align:center" class="reveal">
      <p style="font-size:.9375rem;color:var(--text-secondary);line-height:1.6">
        <strong>Direct Handover:</strong> SkipIt does not operate a physical logistics or delivery fleet. Handover and return arrangements are coordinated directly between the renter and owner.
      </p>
    </div>
  </div>
</section>

<!-- ============================================================
     11. SMART MARKETPLACE
     ============================================================ -->
<section id="smart-marketplace" class="section" aria-label="Smart marketplace technology">
  <div class="container">
    <div class="section-header reveal">
      <span class="eyebrow">Platform Technology</span>
      <h2>More than listings. A smarter marketplace.</h2>
      <p>SkipIt builds marketplace intelligence into the platform — helping maintain listing quality, detect issues early, and support a healthier rental community.</p>
    </div>

    <div class="smart-grid">
      <div class="smart-card reveal">
        <div class="smart-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
        </div>
        <h4>Automated Listing Checks</h4>
        <p>Listings are reviewed against content policies before going live on the marketplace.</p>
      </div>
      <div class="smart-card reveal reveal-delay-1">
        <div class="smart-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
        </div>
        <h4>Duplicate Detection</h4>
        <p>System-level checks identify and flag duplicate or near-identical listings.</p>
      </div>
      <div class="smart-card reveal reveal-delay-2">
        <div class="smart-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        </div>
        <h4>Spam &amp; Keyword Screening</h4>
        <p>Suspicious keywords and patterns are flagged before listing publication.</p>
      </div>
      <div class="smart-card reveal reveal-delay-3">
        <div class="smart-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <h4>Abnormal Pricing Detection</h4>
        <p>Pricing outliers — unusually high or suspiciously low — are flagged for review.</p>
      </div>
      <div class="smart-card reveal reveal-delay-1">
        <div class="smart-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>
        </div>
        <h4>Image &amp; Content Checks</h4>
        <p>Listing images and content are reviewed for quality, relevance, and policy compliance.</p>
      </div>
      <div class="smart-card reveal reveal-delay-2">
        <div class="smart-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <h4>Fraud Indicators</h4>
        <p>Behavioural patterns associated with fraudulent activity are monitored and actioned.</p>
      </div>
      <div class="smart-card reveal reveal-delay-3">
        <div class="smart-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        </div>
        <h4>Human Moderation</h4>
        <p>Listings flagged by automated systems are reviewed by our human moderation team.</p>
      </div>
      <div class="smart-card reveal reveal-delay-4">
        <div class="smart-card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
        </div>
        <h4>Risk-Based Monitoring</h4>
        <p>Ongoing monitoring focuses attention on higher-risk transaction patterns and users.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     12. COMMUNITY EFFECT
     ============================================================ -->
<section id="community" class="section" aria-label="Community impact">
  <div class="container">
    <div class="section-header reveal">
      <span class="eyebrow">The Bigger Picture</span>
      <h2>Access over ownership.</h2>
      <p>SkipIt is built on a simple idea: communities benefit when people share access to things rather than everyone buying the same items separately.</p>
    </div>

    <div class="community-stats">
      <div class="stat-card reveal">
        <div class="stat-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <div class="stat-value">Lower</div>
        <div class="stat-label">Upfront costs for renters</div>
      </div>
      <div class="stat-card reveal reveal-delay-1">
        <div class="stat-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
        </div>
        <div class="stat-value">Higher</div>
        <div class="stat-label">Asset utilization in communities</div>
      </div>
      <div class="stat-card reveal reveal-delay-2">
        <div class="stat-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <div class="stat-value">More</div>
        <div class="stat-label">Earning opportunities for owners</div>
      </div>
      <div class="stat-card reveal reveal-delay-3">
        <div class="stat-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
        </div>
        <div class="stat-value">Better</div>
        <div class="stat-label">Community-driven access</div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     13. FINAL CTA
     ============================================================ -->
<section id="cta-section" class="section" aria-label="Get started">
  <div class="container cta-inner reveal">
    <p class="cta-headline">Stop buying for the occasional.</p>
    <p class="cta-subtext">Find it. Rent it. Use it. Return it.</p>
    <div class="cta-btns">
      <a href="#marketplace" class="btn btn--white btn--lg" id="cta-explore-btn">
        Explore SkipIt
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:16px;height:16px"><path d="m5 12h14M12 5l7 7-7 7"/></svg>
      </a>
      <a href="#for-owners" class="btn btn--outline-white btn--lg" id="cta-list-btn">List an Item</a>
    </div>
  </div>
</section>

</main>

<!-- ============================================================
     14. FOOTER (SKIPIT DARK CHARCOAL SECTION)
     ============================================================ -->
<footer id="footer" aria-label="Site footer">
  <div class="container">
    <div class="footer-grid">
      <!-- Brand -->
      <div>
        <div class="footer-brand-logo">
          <div class="nav-logo-icon" style="background:var(--brand);width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center">
            <svg viewBox="0 0 38 38" fill="white" xmlns="http://www.w3.org/2000/svg" style="width:20px;height:20px">
              <path d="M4 6C4 4.895 4.895 4 6 4H24C25.105 4 26 4.895 26 6V15H16C14.895 15 14 15.895 14 17V26H6C4.895 26 4 25.105 4 24V6Z"/>
              <rect x="17" y="17" width="17" height="9" rx="2"/>
              <circle cx="10" cy="32" r="4"/>
              <circle cx="24" cy="32" r="4"/>
            </svg>
          </div>
          <span style="font-family:var(--font-sans);font-size:1.375rem;font-weight:800;color:white;letter-spacing:-.05em;text-transform:lowercase">skipit</span>
        </div>
        <p class="footer-tagline">Skip buying. Rent smarter.<br>Peer-to-peer rental marketplace — India.</p>
        <div class="footer-socials">
          <a href="#" class="social-btn" aria-label="Instagram" title="SkipIt on Instagram">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/>
            </svg>
          </a>
          <a href="#" class="social-btn" aria-label="LinkedIn" title="SkipIt on LinkedIn">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>
            </svg>
          </a>
          <a href="#" class="social-btn" aria-label="X (Twitter)" title="SkipIt on X">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
            </svg>
          </a>
        </div>
      </div>

      <!-- Marketplace -->
      <div class="footer-col">
        <h5>Marketplace</h5>
        <div class="footer-links">
          <a href="#marketplace" class="footer-link">Browse Listings</a>
          <a href="#how-it-works" class="footer-link">How It Works</a>
          <a href="#for-owners" class="footer-link">List an Item</a>
          <a href="#marketplace" class="footer-link">Categories</a>
          <a href="javascript:void(0)" class="footer-link js-open-search">Search</a>
        </div>
      </div>

      <!-- Company -->
      <div class="footer-col">
        <h5>Company</h5>
        <div class="footer-links">
          <a href="#cta-section" class="footer-link">About SkipIt</a>
          <a href="#trust" class="footer-link">Safety &amp; Trust</a>
          <a href="#protection" class="footer-link">Protection Plans</a>
          <a href="#business-model" class="footer-link">Business Model</a>
          <a href="mailto:support@skipit.in" class="footer-link">Contact Support</a>
        </div>
      </div>

      <!-- Legal -->
      <div class="footer-col">
        <h5>Legal</h5>
        <div class="footer-links">
          <a href="#" class="footer-link">Terms of Service</a>
          <a href="#" class="footer-link">Privacy Policy</a>
          <a href="#" class="footer-link">Rental Policy</a>
          <a href="#" class="footer-link">Refund Policy</a>
          <a href="#" class="footer-link">Security Safeguards</a>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <p class="footer-copy">&copy; 2024 SkipIt. All rights reserved. Peer-to-peer rental marketplace.</p>
      <div class="footer-legal">
        <a href="#">Terms</a>
        <a href="#">Privacy</a>
        <a href="#">Rental Policy</a>
        <a href="#">Refund Policy</a>
      </div>
    </div>
  </div>
</footer>

<script src="main.js"></script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"index.html successfully updated. Total bytes: {len(html_content)}")
