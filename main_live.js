/* SkipIt — Main JavaScript */

// ============================================================
// SCROLL REVEAL
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
// NAVBAR — scroll state
// ============================================================
const navbar = document.getElementById('navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  if (scrollY > 20) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
  lastScroll = scrollY;
}, { passive: true });

// ============================================================
// HAMBURGER / MOBILE NAV
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
    mobileNav.classList.remove('open');
    document.body.style.overflow = '';
    const spans = hamburger.querySelectorAll('span');
    spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
  });
});

// ============================================================
// SEARCH MODAL
// ============================================================
const searchOverlay = document.getElementById('searchOverlay');
const searchInput = document.getElementById('searchInput');

function openSearch() {
  searchOverlay.classList.add('open');
  document.body.style.overflow = 'hidden';
  setTimeout(() => searchInput?.focus(), 200);
}

function closeSearch() {
  searchOverlay.classList.remove('open');
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
    if (searchInput) searchInput.value = cat.textContent;
    searchInput?.focus();
  });
});

// ============================================================
// LISTING MODAL
// ============================================================
const listingOverlay = document.getElementById('listingOverlay');

function openListingModal(data) {
  if (!listingOverlay) return;
  const img = document.getElementById('lmImage');
  const title = document.getElementById('lmTitle');
  const location = document.getElementById('lmLocation');
  const price = document.getElementById('lmPrice');
  const desc = document.getElementById('lmDesc');
  const ownerName = document.getElementById('lmOwnerName');
  const ownerInitial = document.getElementById('lmOwnerInitial');
  const deposit = document.getElementById('lmDeposit');

  if (img) img.src = data.image;
  if (title) title.textContent = data.title;
  if (location) location.textContent = data.location;
  if (price) price.textContent = data.price;
  if (desc) desc.textContent = data.description;
  if (ownerName) ownerName.textContent = data.owner;
  if (ownerInitial) ownerInitial.textContent = data.owner.charAt(0).toUpperCase();
  if (deposit) deposit.textContent = data.deposit;

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
    description: 'Sony Alpha mirrorless camera with kit lens. Perfect for photography projects, events, travel shoots. Includes battery, charger, memory card, and carry bag.',
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
    description: 'PlayStation 5 disc edition with DualSense controller. Includes HDMI cable and power adapter. Perfect for gaming weekends or events.',
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
    description: 'Compact portable projector ideal for home theatre nights, office presentations, or outdoor movie screenings. HD output, HDMI and USB-C compatible.',
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
    description: 'High-performance carbon frame mountain bike with Shimano gears. Perfect for trails, weekend rides, or cycling events. Helmet included.',
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
    description: 'Professional cordless drill with drill bits, screwdriver bits, and carrying case. 18V battery included. Great for home improvement projects.',
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
    description: 'Professional 1000W DJ speaker with mixer support. Ideal for parties, events, and outdoor gatherings. Includes cables and transport handles.',
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
    description: '32" curved ultrawide gaming monitor with RGB lighting, 165Hz refresh rate. Ideal for gaming setups, design work, or temporary workstations.',
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
    description: 'Spacious 4-person dome tent with rain cover, ventilation windows, and carrying bag. Perfect for treks, camping trips, and outdoor adventures.',
  },
];

// ============================================================
// RENDER PRODUCT CARDS
// ============================================================
function renderProductCard(p) {
  const initials = p.owner.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2);
  return `
    <div class="product-card reveal" data-category="${p.catKey}" onclick="openListingModal(window._products['${p.id}'])">
      <div class="product-card-image">
        <img src="${p.image}" alt="${p.title}" loading="lazy">
        <div class="product-card-status">
          <span class="badge badge--green">
            <svg viewBox="0 0 8 8" fill="currentColor"><circle cx="4" cy="4" r="3"/></svg>
            ${p.status}
          </span>
        </div>
        <button class="product-card-wishlist" aria-label="Save listing" onclick="event.stopPropagation()">
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
            ${p.rating}
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
        <div class="product-card-footer">
          <div class="product-card-price">
            <div class="product-price-main">${p.price}</div>
            <div class="product-price-per">per day</div>
          </div>
          <button class="btn btn--primary btn--sm" onclick="event.stopPropagation(); openListingModal(window._products['${p.id}'])">
            View Listing
          </button>
        </div>
      </div>
    </div>
  `;
}

// Store products globally for modal access
window._products = {};
products.forEach(p => { window._products[p.id] = p; });

// Render all cards
const listingsGrid = document.getElementById('listingsGrid');
if (listingsGrid) {
  listingsGrid.innerHTML = products.map(renderProductCard).join('');
  // Re-observe new elements
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
// SMOOTH SCROLL for anchor links
// ============================================================
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute('href'));
    if (target) {
      const top = target.getBoundingClientRect().top + window.scrollY - 80;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

// ============================================================
// SEARCH form submit
// ============================================================
document.getElementById('searchForm')?.addEventListener('submit', (e) => {
  e.preventDefault();
  const val = searchInput?.value?.trim();
  if (val) {
    closeSearch();
    document.getElementById('marketplace')?.scrollIntoView({ behavior: 'smooth' });
  }
});

