/* SkipIt — Main JavaScript */

// ============================================================
// SCROLL REVEAL OBSERVER
// ============================================================
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      revealObserver.unobserve(e.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ============================================================
// NAVBAR — Scroll State
// ============================================================
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
  if (window.scrollY > 20) {
    navbar?.classList.add('scrolled');
  } else {
    navbar?.classList.remove('scrolled');
  }
}, { passive: true });

// ============================================================
// HAMBURGER & MOBILE NAVIGATION
// ============================================================
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');

hamburger?.addEventListener('click', () => {
  const isOpen = mobileNav.classList.contains('open');
  mobileNav.classList.toggle('open');
  document.body.style.overflow = isOpen ? '' : 'hidden';

  const spans = hamburger.querySelectorAll('span');
  if (!isOpen) {
    spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
    spans[1].style.opacity = '0';
    spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
  } else {
    spans[0].style.transform = '';
    spans[1].style.opacity = '';
    spans[2].style.transform = '';
  }
});

document.querySelectorAll('.mobile-nav-link').forEach(link => {
  link.addEventListener('click', () => {
    mobileNav?.classList.remove('open');
    document.body.style.overflow = '';
    const spans = hamburger?.querySelectorAll('span');
    spans?.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
  });
});

// ============================================================
// SEARCH MODAL
// ============================================================
const searchOverlay = document.getElementById('searchOverlay');
const searchInput = document.getElementById('searchInput');

function openSearch() {
  searchOverlay?.classList.add('open');
  document.body.style.overflow = 'hidden';
  setTimeout(() => searchInput?.focus(), 150);
}

function closeSearch() {
  searchOverlay?.classList.remove('open');
  document.body.style.overflow = '';
}

document.querySelectorAll('.js-open-search').forEach(btn => {
  btn.addEventListener('click', openSearch);
});

searchOverlay?.addEventListener('click', (e) => {
  if (e.target === searchOverlay) closeSearch();
});

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeSearch();
    closeListingModal();
  }
  if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
    e.preventDefault();
    openSearch();
  }
});

document.querySelectorAll('.search-quick-cat').forEach(cat => {
  cat.addEventListener('click', () => {
    if (searchInput) {
      searchInput.value = cat.textContent.trim();
      searchInput.focus();
    }
  });
});

document.getElementById('searchForm')?.addEventListener('submit', (e) => {
  e.preventDefault();
  const val = searchInput?.value?.trim().toLowerCase();
  if (val) {
    closeSearch();
    const market = document.getElementById('marketplace');
    market?.scrollIntoView({ behavior: 'smooth' });

    // Filter cards by search query
    document.querySelectorAll('.product-card').forEach(card => {
      const text = card.textContent.toLowerCase();
      card.style.display = text.includes(val) ? '' : 'none';
    });
  }
});

// ============================================================
// PRODUCT DATA
// ============================================================
const products = [
  {
    id: 'camera',
    title: 'Sony Alpha Mirrorless Camera',
    category: 'Photography',
    catKey: 'photography',
    location: 'Bengaluru, KA',
    price: '₹799',
    deposit: '₹5,000',
    rating: '4.9',
    reviews: 34,
    owner: 'Rahul M.',
    image: 'images/product_camera.jpg',
    status: 'Available',
    description: 'Sony Alpha mirrorless camera with kit lens. Perfect for photography projects, events, travel shoots. Includes 2 batteries, fast charger, 64GB high-speed memory card, and shoulder bag.',
  },
  {
    id: 'ps5',
    title: 'PlayStation 5 Console',
    category: 'Gaming',
    catKey: 'gaming',
    location: 'Mumbai, MH',
    price: '₹599',
    deposit: '₹8,000',
    rating: '4.8',
    reviews: 22,
    owner: 'Priya K.',
    image: 'images/product_ps5.jpg',
    status: 'Available',
    description: 'PlayStation 5 disc edition with DualSense controller. Includes ultra-high speed HDMI cable and power adapter. Ideal for gaming weekends, tournaments, or trial gaming setups.',
  },
  {
    id: 'projector',
    title: 'Portable Mini Projector',
    category: 'Electronics',
    catKey: 'electronics',
    location: 'Pune, MH',
    price: '₹349',
    deposit: '₹2,500',
    rating: '4.7',
    reviews: 18,
    owner: 'Aditya S.',
    image: 'images/product_projector.jpg',
    status: 'Available',
    description: 'Compact 1080p portable projector ideal for home theatre movie nights, terrace screenings, or business pitch presentations. HDMI and USB-C connectivity.',
  },
  {
    id: 'bike',
    title: 'Mountain Bike — Carbon Frame',
    category: 'Vehicles',
    catKey: 'vehicles',
    location: 'Delhi, DL',
    price: '₹449',
    deposit: '₹3,000',
    rating: '4.6',
    reviews: 12,
    owner: 'Neha R.',
    image: 'images/product_bike.jpg',
    status: 'Available',
    description: 'High-performance carbon frame mountain bike with 21-speed Shimano gearing and dual disc brakes. Perfect for weekend trail rides or fitness cycling. Sanitized helmet included.',
  },
  {
    id: 'drill',
    title: 'Cordless Power Drill Kit',
    category: 'Tools',
    catKey: 'tools',
    location: 'Hyderabad, TS',
    price: '₹199',
    deposit: '₹1,500',
    rating: '4.8',
    reviews: 41,
    owner: 'Suresh P.',
    image: 'images/product_drill.jpg',
    status: 'Available',
    description: 'Professional 18V cordless drill with 24-piece drill & screwdriver bit set, 2 lithium-ion batteries, and carry case. Ideal for furniture assembly and home DIY improvements.',
  },
  {
    id: 'speaker',
    title: 'DJ Speaker System (1000W)',
    category: 'Events',
    catKey: 'events',
    location: 'Chennai, TN',
    price: '₹1,299',
    deposit: '₹6,000',
    rating: '4.9',
    reviews: 29,
    owner: 'Arjun V.',
    image: 'images/product_speaker.jpg',
    status: 'Available',
    description: 'Professional 1000W active DJ speaker with integrated mixer, Bluetooth connectivity, and dual wireless microphones. Ideal for parties, weddings, and community gatherings.',
  },
  {
    id: 'monitor',
    title: 'Curved Gaming Monitor 32"',
    category: 'Gaming',
    catKey: 'gaming',
    location: 'Bengaluru, KA',
    price: '₹499',
    deposit: '₹4,000',
    rating: '4.7',
    reviews: 15,
    owner: 'Dev T.',
    image: 'images/product_monitor.jpg',
    status: 'Available',
    description: '32-inch curved 165Hz QHD gaming monitor with 1ms response time and HDR support. Perfect for weekend LAN parties, video editing sprints, or temporary design workstations.',
  },
  {
    id: 'tent',
    title: '4-Person Camping Tent',
    category: 'Sports',
    catKey: 'sports',
    location: 'Jaipur, RJ',
    price: '₹299',
    deposit: '₹2,000',
    rating: '4.6',
    reviews: 37,
    owner: 'Kavya L.',
    image: 'images/product_tent.jpg',
    status: 'Available',
    description: 'Spacious waterproof 4-person dome tent with dual vestibules, ground tarp, and aluminum stakes. Sets up in under 5 minutes. Perfect for treks and camping getaways.',
  },
];

// Product lookup
window._products = {};
products.forEach(p => { window._products[p.id] = p; });

// ============================================================
// RENDER PRODUCT CARDS (HBF EDITORIAL COMPOSITION)
// ============================================================
function renderProductCard(p) {
  const initials = p.owner.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2);
  return `
    <div class="product-card reveal" data-category="${p.catKey}" onclick="openListingModal(window._products['${p.id}'])">
      <div class="product-card-image">
        <img src="${p.image}" alt="${p.title}" loading="lazy">
        <div class="product-card-badges">
          <span class="product-badge-cat">${p.category}</span>
          <span class="badge badge--green">
            <svg viewBox="0 0 8 8" fill="currentColor" style="width:7px;height:7px"><circle cx="4" cy="4" r="3"/></svg>
            ${p.status}
          </span>
        </div>
        <button class="product-card-wishlist" aria-label="Save listing" onclick="event.stopPropagation(); toggleWishlist(this)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
          </svg>
        </button>
      </div>
      <div class="product-card-body">
        <div class="product-card-meta">
          <div class="product-card-location">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            ${p.location}
          </div>
          <div class="product-card-rating">
            <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            ${p.rating} (${p.reviews})
          </div>
        </div>
        <div class="product-card-title">${p.title}</div>
        <div class="product-card-owner">
          <div class="owner-avatar">${initials}</div>
          <span class="product-card-owner-name">${p.owner}</span>
          <div class="owner-verified">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            Verified
          </div>
        </div>
        <div class="product-card-deposit">Deposit: ${p.deposit} (Refundable)</div>
        <div class="product-card-footer">
          <div class="product-card-price">
            <span class="product-price-main">${p.price}</span>
            <span class="product-price-per">/ day</span>
          </div>
          <button class="btn btn--primary btn--sm" onclick="event.stopPropagation(); openListingModal(window._products['${p.id}'])">
            Rent Now
          </button>
        </div>
      </div>
    </div>
  `;
}

function toggleWishlist(btn) {
  const svg = btn.querySelector('svg');
  if (svg.getAttribute('fill') === 'currentColor') {
    svg.setAttribute('fill', 'none');
    svg.style.color = 'var(--gray-500)';
  } else {
    svg.setAttribute('fill', 'currentColor');
    svg.style.color = '#ef4444';
  }
}

// Render product grid
const listingsGrid = document.getElementById('listingsGrid');
if (listingsGrid) {
  listingsGrid.innerHTML = products.map(renderProductCard).join('');
  listingsGrid.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
}

// ============================================================
// CATEGORY FILTER
// ============================================================
document.querySelectorAll('.cat-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const cat = btn.dataset.cat;
    const cards = document.querySelectorAll('.product-card');

    cards.forEach(card => {
      if (cat === 'all' || card.dataset.category === cat) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  });
});

// ============================================================
// LISTING DETAIL MODAL & DYNAMIC PRICING CALCULATOR
// ============================================================
const listingOverlay = document.getElementById('listingOverlay');
let currentModalItem = null;
let currentDays = 1;
let currentProtectionPerDay = 0;

function updateModalPricing() {
  if (!currentModalItem) return;

  const dailyPrice = parseInt(currentModalItem.price.replace(/[^\d]/g, ''), 10) || 0;
  const deposit = parseInt(currentModalItem.deposit.replace(/[^\d]/g, ''), 10) || 0;

  // Duration discounts
  let discount = 1;
  if (currentDays >= 14) discount = 0.85;
  else if (currentDays >= 7) discount = 0.90;

  const rentalSubtotal = Math.round(dailyPrice * currentDays * discount);
  const protectionTotal = currentProtectionPerDay * currentDays;
  const total = rentalSubtotal + protectionTotal + deposit;

  const daysLabel = document.getElementById('lmDaysLabel');
  const subtotalEl = document.getElementById('lmRentalSubtotal');
  const protectionRow = document.getElementById('lmProtectionRow');
  const protectionFeeEl = document.getElementById('lmProtectionFee');
  const totalEl = document.getElementById('lmTotalPayable');
  const rentBtn = document.getElementById('lmRentBtn');

  if (daysLabel) daysLabel.textContent = `${currentDays} day${currentDays > 1 ? 's' : ''}`;
  if (subtotalEl) subtotalEl.textContent = `₹${rentalSubtotal.toLocaleString('en-IN')}`;

  if (protectionRow && protectionFeeEl) {
    if (protectionTotal > 0) {
      protectionRow.style.display = 'flex';
      protectionFeeEl.textContent = `+₹${protectionTotal.toLocaleString('en-IN')}`;
    } else {
      protectionRow.style.display = 'none';
    }
  }

  if (totalEl) totalEl.textContent = `₹${total.toLocaleString('en-IN')}`;
  if (rentBtn) rentBtn.innerHTML = `Rent Now &nbsp;·&nbsp; ₹${total.toLocaleString('en-IN')} <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:16px;height:16px"><path d="m5 12h14M12 5l7 7-7 7"/></svg>`;
}

function openListingModal(data) {
  if (!listingOverlay || !data) return;
  currentModalItem = data;
  currentDays = 1;
  currentProtectionPerDay = 0;

  const img = document.getElementById('lmImage');
  const title = document.getElementById('lmTitle');
  const location = document.getElementById('lmLocation');
  const price = document.getElementById('lmPrice');
  const desc = document.getElementById('lmDesc');
  const ownerName = document.getElementById('lmOwnerName');
  const ownerInitial = document.getElementById('lmOwnerInitial');
  const deposit = document.getElementById('lmDeposit');
  const categoryBadge = document.getElementById('lmCategoryBadge');
  const ratingEl = document.getElementById('lmRating');

  if (img) img.src = data.image;
  if (title) title.textContent = data.title;
  if (location) location.textContent = data.location;
  if (price) price.textContent = data.price;
  if (desc) desc.textContent = data.description;
  if (ownerName) ownerName.textContent = data.owner;
  if (ownerInitial) ownerInitial.textContent = data.owner.charAt(0).toUpperCase();
  if (deposit) deposit.textContent = data.deposit;
  if (categoryBadge) categoryBadge.textContent = data.category;
  if (ratingEl) ratingEl.textContent = `${data.rating} (${data.reviews} reviews)`;

  // Reset duration pills
  document.querySelectorAll('#lmDurationSelector .duration-pill').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.days === '1');
  });

  // Reset protection radio
  const defaultRadio = document.querySelector('input[name="lmProtection"][value="0"]');
  if (defaultRadio) defaultRadio.checked = true;
  document.querySelectorAll('.protection-pill').forEach(pill => {
    pill.classList.toggle('active', pill.querySelector('input')?.value === '0');
  });

  // Reset success state
  const successDiv = document.getElementById('lmRentSuccess');
  const rentBtn = document.getElementById('lmRentBtn');
  if (successDiv) successDiv.style.display = 'none';
  if (rentBtn) rentBtn.style.display = 'inline-flex';

  updateModalPricing();

  listingOverlay.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeListingModal() {
  listingOverlay?.classList.remove('open');
  document.body.style.overflow = '';
}

listingOverlay?.addEventListener('click', (e) => {
  if (e.target === listingOverlay) closeListingModal();
});

document.getElementById('lmClose')?.addEventListener('click', closeListingModal);

// Duration selector buttons
document.querySelectorAll('#lmDurationSelector .duration-pill').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('#lmDurationSelector .duration-pill').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentDays = parseInt(btn.dataset.days, 10) || 1;
    updateModalPricing();
  });
});

// Protection plan radio inputs
document.querySelectorAll('input[name="lmProtection"]').forEach(input => {
  input.addEventListener('change', () => {
    document.querySelectorAll('.protection-pill').forEach(pill => {
      pill.classList.toggle('active', pill.querySelector('input')?.checked);
    });
    currentProtectionPerDay = parseInt(input.value, 10) || 0;
    updateModalPricing();
  });
});

// ============================================================
// RENT REQUEST HANDLER
// ============================================================
window.handleRentRequest = function() {
  const userJson = localStorage.getItem('skipit_user');
  const rentBtn = document.getElementById('lmRentBtn');
  const successDiv = document.getElementById('lmRentSuccess');

  if (!userJson) {
    const itemId = currentModalItem?.id || '';
    window.location.href = `auth.html?redirect=rental&item=${encodeURIComponent(itemId)}`;
    return;
  }

  let user = { name: 'Member' };
  try { user = JSON.parse(userJson); } catch(_) {}
  const renterName = user.name || user.email?.split('@')[0] || 'Member';

  if (rentBtn) rentBtn.style.display = 'none';
  if (successDiv) {
    successDiv.innerHTML = `
      <div style="margin-bottom:6px;font-size:1rem;font-weight:700">🎉 Rental Request Confirmed!</div>
      <div style="font-weight:400;font-size:0.875rem;line-height:1.5">
        Thanks, ${renterName}! ${currentModalItem?.owner} has received your request for ${currentModalItem?.title} (${currentDays} days).
        You will receive coordination details in your inbox.
      </div>
    `;
    successDiv.style.display = 'block';

    // Store rental in history
    try {
      const history = JSON.parse(localStorage.getItem('skipit_rentals') || '[]');
      history.push({
        id: 'req_' + Date.now(),
        item: currentModalItem?.title,
        owner: currentModalItem?.owner,
        days: currentDays,
        date: new Date().toLocaleDateString('en-IN')
      });
      localStorage.setItem('skipit_rentals', JSON.stringify(history));
    } catch(_) {}

    setTimeout(() => {
      closeListingModal();
      setTimeout(() => {
        if (rentBtn) rentBtn.style.display = 'inline-flex';
        if (successDiv) successDiv.style.display = 'none';
      }, 400);
    }, 2800);
  }
};

// ============================================================
// AUTHENTICATION STATE & NAVBAR USER BADGE
// ============================================================
function updateAuthStateUI() {
  const userJson = localStorage.getItem('skipit_user');
  if (!userJson) return;

  try {
    const user = JSON.parse(userJson);
    if (!user || (!user.email && !user.name)) return;

    const displayName = user.name || user.email.split('@')[0];
    const initial = displayName.charAt(0).toUpperCase();

    // Desktop navbar update
    const navLogin = document.getElementById('navLoginBtn');
    if (navLogin) {
      const container = document.createElement('div');
      container.className = 'nav-user-wrap';
      container.style.display = 'inline-flex';
      container.style.alignItems = 'center';
      container.style.gap = '8px';
      container.innerHTML = `
        <div class="owner-avatar" style="width:32px;height:32px;font-size:0.75rem;background:linear-gradient(135deg,var(--brand-deep),var(--brand));color:#ffffff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700" title="${user.email}">${initial}</div>
        <span style="font-size:0.875rem;font-weight:700;color:var(--text-primary);max-width:110px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${displayName}</span>
        <button id="navLogoutBtn" style="font-size:0.75rem;font-weight:600;color:var(--text-muted);padding:5px 10px;border-radius:var(--radius-full);cursor:pointer;border:1px solid var(--border);background:#ffffff;transition:all var(--duration-fast)">Log out</button>
      `;
      navLogin.replaceWith(container);

      document.getElementById('navLogoutBtn')?.addEventListener('click', () => {
        localStorage.removeItem('skipit_user');
        window.location.reload();
      });
    }

    // Mobile nav update
    const mobileLogin = document.getElementById('mobileNavLoginBtn');
    if (mobileLogin) {
      mobileLogin.textContent = `Sign out (${displayName})`;
      mobileLogin.href = '#';
      mobileLogin.addEventListener('click', (e) => {
        e.preventDefault();
        localStorage.removeItem('skipit_user');
        window.location.reload();
      });
    }
  } catch(_) {}
}

// Smooth scrolling for in-page anchors
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', (e) => {
    const href = link.getAttribute('href');
    if (!href || href === '#') return;
    const target = document.querySelector(href);
    if (target) {
      e.preventDefault();
      const top = target.getBoundingClientRect().top + window.scrollY - 76;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

document.addEventListener('DOMContentLoaded', updateAuthStateUI);
updateAuthStateUI();
