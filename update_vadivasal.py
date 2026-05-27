import sys

file_path = r'c:\Users\anbua\Downloads\turfvadi\vadivasal-turf.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

def get_content(start_idx, end_idx):
    return "".join(lines[start_idx:end_idx])

# Chunk 1: Hero CSS
c1_start = 187
c1_end = 199
c1_replacement = """    .sf-hero-bg {
      position: absolute;
      inset: -5%;
      width: 110%; height: 110%;
      background-image: url('./image.png');
      background-size: cover;
      background-position: center;
      z-index: 1;
      filter: brightness(0.3) blur(5px);
      transform: scale(1.2);
    }
    .sf-hero-leaves {
      position: absolute;
      inset: -20%;
      width: 140%; height: 140%;
      background-image: url('./tree_overlay.png');
      background-size: cover;
      background-position: center;
      mix-blend-mode: multiply;
      z-index: 2;
      pointer-events: none;
      transform-origin: center center;
    }
"""

# Chunk 2: Preloader CSS
c2_start = 1330
c2_end = 1491
c2_replacement = """    /* ══════════════════════════════════════════
       CINEMATIC PRELOADER
    ══════════════════════════════════════════ */
    #preloader {
      position: fixed;
      inset: 0;
      z-index: 99999;
      background: #050e07;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: opacity 1.2s cubic-bezier(0.76,0,0.24,1), visibility 1.2s;
    }
    #preloader.hidden {
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }
    .preloader-brand {
      text-align: center;
      margin-bottom: 2rem;
    }
    .pl-brand-top {
      font-family: var(--font-serif);
      font-size: clamp(2rem, 4vw, 3rem);
      letter-spacing: 0.2em;
      color: #fff;
      line-height: 1;
    }
    .pl-brand-bottom {
      font-family: var(--font-serif);
      font-size: 0.9rem;
      letter-spacing: 0.3em;
      color: rgba(255,255,255,0.65);
      margin-top: 0.5rem;
      display: flex;
      gap: 0.6rem;
      align-items: center;
      justify-content: center;
    }
    .pl-stars { font-size: 0.7rem; letter-spacing: 0.15em; }
    .preloader-progress-container {
      width: 200px;
      text-align: center;
    }
    .preloader-bar-bg {
      width: 100%;
      height: 2px;
      background: rgba(255,255,255,0.2);
      margin-bottom: 0.8rem;
    }
    .preloader-bar {
      width: 0%;
      height: 100%;
      background: var(--gold);
      transition: width 0.1s linear;
    }
    .preloader-text {
      font-family: var(--font-sans);
      font-weight: 600;
      font-size: 0.85rem;
      color: rgba(255,255,255,0.6);
      letter-spacing: 0.1em;
    }
"""

# Chunk 3: Preloader HTML
c3_start = 1532
c3_end = 1562
c3_replacement = """<!-- ══ CINEMATIC PRELOADER ══ -->
<div id="preloader">
  <div class="preloader-brand">
    <div class="pl-brand-top">VADIVASAL</div>
    <div class="pl-brand-bottom"><span class="pl-stars">✦ ✦ ✦ ✦</span> T U R F</div>
  </div>
  <div class="preloader-progress-container">
    <div class="preloader-bar-bg">
      <div class="preloader-bar" id="preloaderBar"></div>
    </div>
    <div class="preloader-text" id="preloaderText">0%</div>
  </div>
</div>
"""

# Chunk 4: Hero HTML
c4_start = 1591
c4_end = 1595
c4_replacement = """<!-- ── SF HERO ── -->
<section id="hero" class="sf-hero">
  <div class="sf-hero-bg" id="heroBg"></div>
  <div class="sf-hero-leaves" id="heroLeaves"></div>
</section>
"""

# Chunk 5: JS Preloader Logic
c5_start = 2085
c5_end = 2380
c5_replacement = """  // ══════════════════════════════════════════════════════════════
  //  CINEMATIC PRELOADER LOGIC
  // ══════════════════════════════════════════════════════════════
  const preloader = document.getElementById('preloader');
  const preloaderBar = document.getElementById('preloaderBar');
  const preloaderText = document.getElementById('preloaderText');

  function playHeroAnimations() {
    gsap.fromTo('.sf-brand',    { y: -20, opacity: 0 }, { y: 0, opacity: 1, duration: 1.5, ease: 'power3.out', delay: 0.2 });
    gsap.fromTo('.nav-trigger', { opacity: 0 }, { opacity: 1, duration: 1.5, ease: 'power3.out', delay: 0.2 });
  }

  if (sessionStorage.getItem('hasVisited')) {
    preloader.style.display = 'none';
    gsap.set('#heroBg', { scale: 1, filter: 'brightness(1) blur(0px)' });
    gsap.set('#heroLeaves', { scale: 5, opacity: 0, display: 'none' }); 
    playHeroAnimations();
  } else {
    // Initial state: dim ground, leaves present
    gsap.set('#heroBg', { scale: 1.2, filter: 'brightness(0.3) blur(5px)' });
    gsap.set('#heroLeaves', { scale: 1, opacity: 1 });

    let pct = 0;
    const loadingInterval = setInterval(() => {
      pct += Math.floor(Math.random() * 8) + 2;
      if (pct > 100) pct = 100;
      preloaderBar.style.width = pct + '%';
      preloaderText.textContent = pct + '%';
      
      if (pct >= 100) {
        clearInterval(loadingInterval);
        setTimeout(() => {
          preloader.classList.add('hidden');
          sessionStorage.setItem('hasVisited', 'true');
          
          // Fly through the trees! Trees scale up immensely and fade out
          gsap.to('#heroLeaves', {
            scale: 6,
            opacity: 0,
            duration: 3,
            ease: 'power2.inOut'
          });

          // Turf zooms out slightly and becomes perfectly clear
          gsap.to('#heroBg', {
            scale: 1,
            filter: 'brightness(1) blur(0px)',
            duration: 3,
            ease: 'power2.inOut',
            onComplete: playHeroAnimations
          });
        }, 500);
      }
    }, 40);
  }
"""

new_lines = lines[:c1_start] + [c1_replacement] + lines[c1_end:c2_start] + [c2_replacement] + lines[c2_end:c3_start] + [c3_replacement] + lines[c3_end:c4_start] + [c4_replacement] + lines[c4_end:c5_start] + [c5_replacement] + lines[c5_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Updates applied successfully.")
