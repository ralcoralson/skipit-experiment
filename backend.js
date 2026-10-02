/**
 * SkipIt — Backend Configuration & API Client
 * ═══════════════════════════════════════════════════════════════
 *  Connects the frontend to:
 *   • Firebase  (Auth + Firestore)
 *   • Supabase  (PostgreSQL + Storage + Realtime)
 *   • skip-it-2.0 NestJS API
 *
 *  SETUP STEPS:
 *  1. Firebase  → https://console.firebase.google.com
 *                 → Your Project → Project Settings → Web App
 *  2. Supabase  → https://app.supabase.com
 *                 → Your Project → Settings → API
 *  3. SkipIt API → Your skip-it-2.0 server URL
 *  NOTE: This file is an ES Module. Load with <script type="module">
 *                  (local dev: http://localhost:3001)
 * ═══════════════════════════════════════════════════════════════
 */

const CONFIG = {

  // ───────────────────────────────────────────────────────────
  // FIREBASE CONFIG
  // Copy from: Firebase Console → Project Settings → General
  // ───────────────────────────────────────────────────────────
  firebase: {
    apiKey:            "YOUR_FIREBASE_API_KEY",
    authDomain:        "YOUR_PROJECT_ID.firebaseapp.com",
    projectId:         "YOUR_PROJECT_ID",
    storageBucket:     "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId:             "YOUR_APP_ID",
    measurementId:     "YOUR_MEASUREMENT_ID",
  },

  // ───────────────────────────────────────────────────────────
  // SUPABASE CONFIG
  // ───────────────────────────────────────────────────────────
  supabase: {
    url:     "https://uhrskxkgbpzzanehwefm.supabase.co",
    anonKey: "sb_publishable_4KlmMgS5oNhcAZUWPOTGBA_Pgrndepm",
  },

  // ───────────────────────────────────────────────────────────
  // SKIP-IT 2.0 NESTJS API
  // skip-it-2.0-main backend server URL
  // Local:      http://localhost:3000
  // Production: https://api.yourdomain.com
  // ───────────────────────────────────────────────────────────
  api: {
    baseUrl: "http://localhost:3000",
    url(path) { return `${this.baseUrl}/api${path}`; },
  },
};

export default CONFIG;

// ═══════════════════════════════════════════════════════════════
// API CLIENT — wraps fetch with Firebase Auth headers
// ═══════════════════════════════════════════════════════════════
export class SkipItAPI {

  static async _headers() {
    try {
      const { getAuth } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js');
      const user = getAuth().currentUser;
      if (user) return { Authorization: `Bearer ${await user.getIdToken()}` };
    } catch(_) {}
    return {};
  }

  static async _fetch(path, opts = {}) {
    const h = await this._headers();
    const res = await fetch(CONFIG.api.url(path), {
      headers: { 'Content-Type': 'application/json', ...h },
      ...opts,
    });
    if (!res.ok) throw new Error(`[SkipIt API] ${res.status} ${await res.text()}`);
    return res.json();
  }

  static get(path)          { return this._fetch(path); }
  static post(path, body)   { return this._fetch(path, { method:'POST',   body: JSON.stringify(body) }); }
  static put(path, body)    { return this._fetch(path, { method:'PUT',    body: JSON.stringify(body) }); }
  static patch(path, body)  { return this._fetch(path, { method:'PATCH',  body: JSON.stringify(body) }); }
  static delete(path)       { return this._fetch(path, { method:'DELETE' }); }

  // ── Auth ────────────────────────────────────────────────
  static syncUser(u)          { return this.post('/auth/sync', { uid:u.uid, email:u.email, displayName:u.displayName, photoURL:u.photoURL, provider:u.providerData[0]?.providerId }); }
  static getMe()              { return this.get('/auth/me'); }

  // ── Listings ─────────────────────────────────────────────
  static getListings(q={})    { return this.get('/listings?'  + new URLSearchParams(q)); }
  static getListing(id)       { return this.get(`/listings/${id}`); }
  static createListing(d)     { return this.post('/listings', d); }
  static updateListing(id, d) { return this.put(`/listings/${id}`, d); }
  static deleteListing(id)    { return this.delete(`/listings/${id}`); }

  // ── Bookings ─────────────────────────────────────────────
  static getBookings(q={})    { return this.get('/bookings?'  + new URLSearchParams(q)); }
  static getBooking(id)       { return this.get(`/bookings/${id}`); }
  static createBooking(d)     { return this.post('/bookings', d); }
  static updateBooking(id, d) { return this.patch(`/bookings/${id}`, d); }

  // ── Users ─────────────────────────────────────────────────
  static getProfile(uid)      { return this.get(`/users/${uid}`); }
  static updateProfile(uid,d) { return this.put(`/users/${uid}`, d); }
  static getMyListings()      { return this.get('/users/me/listings'); }
  static getMyBookings()      { return this.get('/users/me/bookings'); }

  // ── Reviews ───────────────────────────────────────────────
  static getReviews(listingId){ return this.get(`/listings/${listingId}/reviews`); }
  static createReview(d)      { return this.post('/reviews', d); }
}

// ═══════════════════════════════════════════════════════════════
// SUPABASE HELPERS
// ═══════════════════════════════════════════════════════════════
export class SkipItDB {
  static _sb = null;

  static client() {
    if (this._sb) return this._sb;
    if (!window.supabase) throw new Error('Supabase JS not loaded');
    this._sb = window.supabase.createClient(CONFIG.supabase.url, CONFIG.supabase.anonKey);
    return this._sb;
  }

  // Upsert user after Firebase login
  static upsertUser(profile) {
    return this.client().from('users').upsert({ ...profile, firebase_uid: profile.uid }, { onConflict: 'firebase_uid' });
  }

  // Fetch listings with optional filters
  static async getListings({ category, location, limit = 20, offset = 0 } = {}) {
    let q = this.client().from('listings').select('*').eq('available', true).range(offset, offset + limit - 1);
    if (category) q = q.eq('category', category);
    if (location) q = q.ilike('location', `%${location}%`);
    return q;
  }

  // Real-time listings subscription
  static onListingChange(cb) {
    return this.client().channel('listings')
      .on('postgres_changes', { event: '*', schema: 'public', table: 'listings' }, cb)
      .subscribe();
  }

  // Upload image to Supabase Storage → returns public URL
  static async uploadImage(file, folder = 'listings') {
    const path = `${folder}/${Date.now()}_${file.name}`;
    const sb = this.client();
    const { error } = await sb.storage.from('skipit-images').upload(path, file, { upsert: true });
    if (error) throw error;
    return sb.storage.from('skipit-images').getPublicUrl(path).data.publicUrl;
  }
}

// ═══════════════════════════════════════════════════════════════
// AUTH HELPERS — combined Firebase + Supabase + API sync
// ═══════════════════════════════════════════════════════════════
export async function onAuthSuccess(firebaseUser) {
  const profile = {
    uid:         firebaseUser.uid,
    email:       firebaseUser.email,
    displayName: firebaseUser.displayName || '',
    photoURL:    firebaseUser.photoURL    || '',
    provider:    firebaseUser.providerData[0]?.providerId || 'email',
    role:        'user',
    createdAt:   new Date().toISOString(),
  };

  // 1. Save to Firestore
  try {
    const { getFirestore, doc, setDoc } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js');
    const { getApp } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js');
    await setDoc(doc(getFirestore(getApp()), 'users', profile.uid), profile, { merge: true });
  } catch(e) { console.warn('Firestore save:', e.message); }

  // 2. Upsert to Supabase
  try { await SkipItDB.upsertUser(profile); }
  catch(e) { console.warn('Supabase save:', e.message); }

  // 3. Sync with skip-it-2.0 backend
  try { await SkipItAPI.syncUser(firebaseUser); }
  catch(e) { console.warn('Backend sync:', e.message); }

  // 4. Store locally
  localStorage.setItem('skipit_user', JSON.stringify({ uid: profile.uid, email: profile.email, name: profile.displayName }));

  return profile;
}

export default CONFIG;

/*
══════════════════════════════════════════════════════════════
  SUPABASE SETUP — Run this SQL in Supabase SQL Editor
  Dashboard → SQL Editor → New Query → Paste → Run
══════════════════════════════════════════════════════════════

create table if not exists public.users (
  id            uuid default gen_random_uuid() primary key,
  firebase_uid  text unique not null,
  email         text unique not null,
  display_name  text,
  photo_url     text,
  provider      text default 'email',
  role          text default 'user',
  created_at    timestamptz default now(),
  updated_at    timestamptz default now()
);

create table if not exists public.listings (
  id            uuid default gen_random_uuid() primary key,
  owner_uid     text not null references public.users(firebase_uid),
  title         text not null,
  description   text,
  category      text,
  price_per_day decimal(10,2) not null,
  deposit       decimal(10,2) default 0,
  location      text,
  images        text[],
  available     boolean default true,
  created_at    timestamptz default now(),
  updated_at    timestamptz default now()
);

create table if not exists public.bookings (
  id           uuid default gen_random_uuid() primary key,
  listing_id   uuid not null references public.listings(id),
  renter_uid   text not null references public.users(firebase_uid),
  owner_uid    text not null,
  start_date   date not null,
  end_date     date not null,
  total_amount decimal(10,2),
  status       text default 'pending',
  created_at   timestamptz default now()
);

create table if not exists public.reviews (
  id          uuid default gen_random_uuid() primary key,
  listing_id  uuid not null references public.listings(id),
  reviewer_uid text not null references public.users(firebase_uid),
  rating      int check (rating between 1 and 5),
  comment     text,
  created_at  timestamptz default now()
);

-- Enable Row Level Security
alter table public.users    enable row level security;
alter table public.listings enable row level security;
alter table public.bookings enable row level security;
alter table public.reviews  enable row level security;

-- RLS Policies
create policy "anyone can read listings"   on public.listings for select using (true);
create policy "owner manages listings"     on public.listings for all    using (owner_uid = (select firebase_uid from users where id = auth.uid()::uuid));
create policy "users read own bookings"    on public.bookings for select using (renter_uid = (select firebase_uid from users where id = auth.uid()::uuid));
create policy "anyone reads reviews"       on public.reviews  for select using (true);
*/
