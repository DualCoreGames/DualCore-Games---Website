document.addEventListener('DOMContentLoaded', () => {
  // ── Anti-Spam Interceptor ──────────────────────────────────────────────────
  // Blacklist of known spam patterns. If matched, show fake success and do NOT
  // send the form data or fire any GTM events.
  const SPAM_BLACKLIST = [
    /\$[0-9,]+,000/i,         // Money amounts like $27,000,000
    /casino/i,
    /jackpot/i,
    /meumini\.link/i,
    /cut\.gl/i,
    /linkypay/i,
    /earn.*per.*day/i,
    /make.*money.*online/i,
    /adult.*content/i,
    /xxx/i,
    /viagra/i,
    /cialis/i,
    /\bseo\b.*service/i,     // SEO service spam
    /buy.*backlinks/i,
    /crypto.*investment/i,
    /binary.*options/i,
  ];

  function isSpam(formData) {
    const fieldsToCheck = ['message', 'project', 'name', 'email'];
    for (const field of fieldsToCheck) {
      const value = formData.get(field) || '';
      for (const pattern of SPAM_BLACKLIST) {
        if (pattern.test(value)) {
          console.warn('[AntiSpam] Blocked submission matching pattern:', pattern);
          return true;
        }
      }
    }
    return false;
  }
  // ─────────────────────────────────────────────────────────────────────────────

    // 1. Dynamic Keyword Insertion (DKI)
    const updateHeroHeadline = () => {
        const urlParams = new URLSearchParams(window.location.search);
        const utmTerm = urlParams.get('utm_term');
        const heroH1 = document.querySelector('.hero h1');
        if (heroH1) {
            if (utmTerm) {
                const formattedTerm = decodeURIComponent(utmTerm).replace(/\+/g, ' ');
                heroH1.textContent = `Engineering-First Systems for ${formattedTerm}`;
            }
        }
    };
    updateHeroHeadline();

    // 2. Strategic Funnel & Intent Handling
    const handleContactIntent = () => {
        const urlParams = new URLSearchParams(window.location.search);
        const intent = urlParams.get('intent');
        const contactH1 = document.querySelector('main h1');
        const contactSub = document.querySelector('main p.text-muted, main p.lead');
        const messageField = document.querySelector('#message');
        const projectField = document.querySelector('#project');

        if (window.location.pathname.includes('/contact/')) {
            if (intent === 'specs') {
                if (contactH1) contactH1.textContent = "Get Production Pipeline Specs";
                if (contactSub) contactSub.textContent = "Enter your details below to receive our latest B2B production pipeline specifications.";
                if (messageField) messageField.value = "I am interested in downloading the DualCore Production Pipeline Specifications. Please provide the latest technical documentation.";
                if (projectField) projectField.value = "Technical Pipeline Specs";
            } else if (intent === 'audit') {
                if (contactH1) contactH1.textContent = "Request Technical Audit";
                if (contactSub) contactSub.textContent = "Tell us about your project infrastructure to request a free engineering architecture audit.";
                if (messageField) messageField.value = "I would like to request a technical architecture audit for our current project.";
                if (projectField) projectField.value = "Architecture Audit";
            }
        }
    };
    handleContactIntent();

    // 3. Conversion Tracking
    window.trackConversion = (label) => {
        console.log(`[GTM-STAGED] Conversion Event: ${label}`);
    };

    // Attach tracking to specific buttons
    document.querySelectorAll('a[href*="intent="]').forEach(btn => {
        btn.addEventListener('click', () => {
            const intent = new URLSearchParams(btn.search).get('intent');
            trackConversion(`Intent: ${intent}`);
        });
    });

    // 4. Form Submission & AJAX Redirect
    const forms = document.querySelectorAll('form.contact-form, form.beta-form, #contactForm, #contactFormTwo, #reclairosBetaForm, #paapiContactForm, #roomRaiderForm, #audit-form-element, #notd-form, #newsletterForm');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Honeypot spam bot check
            const honeypot = form.querySelector('input[name="honeypot_field"]');
            
            const spamKeywords = [
                "seo ranking", "seo agency", "backlinks", "guest post", "buy traffic", 
                "crypto", "forex", "trading signals", "whatsapp +", "telegram: @", 
                "jackpot", "$27,000,000", "http://", "https://", "mega.nz", "telegra.ph",
                "psychophysical", "satellite weapons", "gru report"
            ];
            const messageField = form.querySelector('textarea[name="message"]');
            const nameField = form.querySelector('input[name="name"]');
            const messageContent = messageField ? messageField.value.toLowerCase() : "";
            const nameContent = nameField ? nameField.value.toLowerCase() : "";
            const isSpam = spamKeywords.some(keyword => messageContent.includes(keyword) || nameContent.includes(keyword));

            if ((honeypot && honeypot.value) || isSpam) {
                console.warn("Spam submission blocked.");
                const submitBtn = form.querySelector('button[type="submit"]');
                if (submitBtn) {
                    submitBtn.disabled = true;
                    submitBtn.textContent = 'SENDING...';
                    setTimeout(() => {
                        submitBtn.textContent = 'MESSAGE SENT';
                        submitBtn.style.backgroundColor = '#10B981';
                        submitBtn.style.color = '#fff';
                        submitBtn.style.borderColor = '#10B981';
                    }, 800);
                }
                return;
            }

            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn ? submitBtn.textContent : 'Submit';
            
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = 'SENDING...';
            }

            const formData = new FormData(form);
            const defaultAction = 'https://script.google.com/macros/s/AKfycbzoije_tJBOEAofZS25gWx2Ge65ky5n0d8Uh-rWZN3tjtRHkTxYLnid8UUOKouhmm8/exec';
            const submissionUrl = form.action && form.action !== window.location.href ? form.action : defaultAction;

            fetch(submissionUrl, {
                method: 'POST',
                body: formData,
                mode: 'no-cors'
            })
            .then(() => {
                // Fire GTM generate_lead event for legitimate submissions
                if (window.dataLayer) {
                    window.dataLayer.push({
                        'event': 'generate_lead',
                        'form_id': form.id || 'unknown',
                        'source_page': window.location.pathname
                    });
                }
                
                // Calculate relative prefix depending on directory depth to point to root thank-you.html correctly
                const parts = window.location.pathname.split('/').filter(Boolean);
                if (parts.length > 0 && parts[parts.length - 1].includes('.')) {
                    parts.pop(); // Remove filename if present to get correct folder depth
                }
                const prefix = '../'.repeat(parts.length);
                window.location.href = prefix + 'thank-you/';
            })
            .catch((err) => {
                console.error("Submission error:", err);
                alert("Oops! There was a problem submitting your form. Please try again.");
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.textContent = originalBtnText;
                }
            });
        });
    });

    // 5. Nav Toggle & Accessibility
    document.querySelectorAll('.has-dropdown').forEach(dropdown => {
        const toggle = dropdown.querySelector('.dropdown-toggle');
        const menu = dropdown.querySelector('.dropdown-menu');
        if (toggle && menu) {
            const href = toggle.getAttribute('href');
            const text = toggle.textContent.trim().replace('▼', '').trim();
            if (!menu.querySelector('.mobile-overview-link')) {
                const li = document.createElement('li');
                li.className = 'mobile-overview-link';
                const label = text === 'Services' ? 'All Services / Overview →' : 'All Projects / Overview →';
                li.innerHTML = `<a class="dropdown-link" href="${href}" style="font-weight: 700; color: var(--core-tech);">${label}</a>`;
                
                menu.insertBefore(li, menu.firstChild);
                
                const divider = document.createElement('li');
                divider.className = 'mobile-overview-divider dropdown-divider';
                menu.insertBefore(divider, menu.children[1]);
            }
        }
    });

    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const navClose = document.querySelector('.nav-close');
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    if (navToggle && navMenu) {
        const toggleMenu = (open) => {
            const isOpen = open !== undefined ? open : !navMenu.classList.contains('active');
            navMenu.classList.toggle('active', isOpen);
            navToggle.classList.toggle('active', isOpen);
            navToggle.setAttribute('aria-expanded', isOpen);
            navMenu.setAttribute('aria-hidden', !isOpen);
            document.body.classList.toggle('nav-open', isOpen);
        };

        navToggle.addEventListener('click', () => toggleMenu());
        if (navClose) {
            navClose.addEventListener('click', () => toggleMenu(false));
        }

        dropdownToggles.forEach(toggle => {
            toggle.addEventListener('click', (event) => {
                if (window.innerWidth > 1024) return;
                const dropdownItem = toggle.closest('.has-dropdown');
                if (!dropdownItem) return;
                event.preventDefault();
                const isActive = dropdownItem.classList.contains('active');
                document.querySelectorAll('.has-dropdown.active').forEach(item => {
                    if (item !== dropdownItem) item.classList.remove('active');
                });
                dropdownItem.classList.toggle('active', !isActive);
            });
        });

        navMenu.querySelectorAll('a:not(.dropdown-toggle)').forEach(link => {
            link.addEventListener('click', () => toggleMenu(false));
        });
    }

    // 6. Optimized Animations (rAF)
    const header = document.querySelector('header');
    let lastScrollY = window.scrollY;
    let scrollTicking = false;

    const updateHeader = () => {
        if (lastScrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
        scrollTicking = false;
    };

    window.addEventListener('scroll', () => {
        lastScrollY = window.scrollY;
        if (!scrollTicking) {
            requestAnimationFrame(updateHeader);
            scrollTicking = true;
        }
    }, { passive: true });

    // Hero Mouse Tracking with cached bounds
    const heroSection = document.querySelector('.hero');
    const networkAnimation = document.querySelector('.hero-network-animation');
    let heroRect = heroSection ? heroSection.getBoundingClientRect() : null;
    let mouseX = 0, mouseY = 0;
    let animTicking = false;

    window.addEventListener('resize', () => {
        if (heroSection) heroRect = heroSection.getBoundingClientRect();
    }, { passive: true });

    const updateNetworkAnim = () => {
        if (heroRect && networkAnimation) {
            const centerX = heroRect.width / 2;
            const centerY = heroRect.height / 2;
            const moveX = ((mouseX - centerX) / centerX) * -10;
            const moveY = ((mouseY - centerY) / centerY) * -10;
            networkAnimation.style.transform = `translate3d(${moveX}px, ${moveY}px, 0)`;
        }
        animTicking = false;
    };

    if (heroSection && networkAnimation && window.innerWidth >= 768) {
        heroSection.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            if (!animTicking) {
                requestAnimationFrame(updateNetworkAnim);
                animTicking = true;
            }
        }, { passive: true });
    }

    // 7. FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (!question) return;
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            faqItems.forEach(faq => {
                faq.classList.remove('active');
                faq.querySelector('.faq-question')?.setAttribute('aria-expanded', 'false');
            });

            if (!isActive) {
                item.classList.add('active');
                question.setAttribute('aria-expanded', 'true');
            }
        });
    });

        // Why Choose — scroll entrance + mouse parallax
    (function () {
    const section = document.querySelector('.why-choose-section');
    if (!section) return;

    const targets = section.querySelectorAll('.pillar-card, .metric-item, .section-header');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
        if (entry.isIntersecting) entry.target.classList.add('visible');
        });
    }, { threshold: 0.12 });

    targets.forEach((el) => observer.observe(el));

    section.addEventListener('mousemove', (e) => {
        const rect = section.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width - 0.5) * 20;
        const y = ((e.clientY - rect.top) / rect.height - 0.5) * 14;
        section.style.backgroundPosition = `calc(50% + ${x}px) calc(50% + ${y}px)`;
    });

    section.addEventListener('mouseleave', () => {
        section.style.transition = 'background-position 1s ease';
        section.style.backgroundPosition = 'center center';
        setTimeout(() => section.style.transition = '', 1000);
    });
    })();

      // .philosophy-narrative — scroll entrance + mouse parallax
    (function () {
    const section = document.querySelector('.philosophy-narrative');
    if (!section) return;

    const targets = section.querySelectorAll('.pillar-card, .metric-item, .section-header');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
        if (entry.isIntersecting) entry.target.classList.add('visible');
        });
    }, { threshold: 0.12 });

    targets.forEach((el) => observer.observe(el));

    section.addEventListener('mousemove', (e) => {
        const rect = section.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width - 0.5) * 20;
        const y = ((e.clientY - rect.top) / rect.height - 0.5) * 14;
        section.style.backgroundPosition = `calc(50% + ${x}px) calc(50% + ${y}px)`;
    });

    section.addEventListener('mouseleave', () => {
        section.style.transition = 'background-position 1s ease';
        section.style.backgroundPosition = 'center center';
        setTimeout(() => section.style.transition = '', 1000);
    });
    })();

    // 6. Interactive Hero Particle Canvas System
    (function () {
        // Bypass completely on mobile to eliminate CPU rendering overhead
        if (window.innerWidth < 768) {
            const canvas = document.getElementById('hero-canvas');
            if (canvas) canvas.style.display = 'none';
            return;
        }

        const initCanvas = () => {
            const canvas = document.getElementById('hero-canvas');
            if (!canvas) return;

            const ctx = canvas.getContext('2d');
            const heroSection = document.querySelector('.hero');
            if (!heroSection) return;

            let width = canvas.width = heroSection.offsetWidth;
            let height = canvas.height = heroSection.offsetHeight;

            const particles = [];
            const maxParticles = 120;
            const mouse = { x: null, y: null, active: false, radius: 180 };

            class Particle {
                constructor() {
                    this.reset();
                }

                reset() {
                    this.x = Math.random() * width;
                    this.y = Math.random() * height + height * 0.1;
                    this.size = Math.random() * 2 + 0.8;
                    this.speedX = (Math.random() - 0.5) * 0.4;
                    this.speedY = -Math.random() * 0.5 - 0.15; // slow drift upward
                    this.alpha = Math.random() * 0.5 + 0.15;
                    this.angle = Math.random() * Math.PI * 2;
                    this.spinSpeed = (Math.random() - 0.5) * 0.02;
                }

                update() {
                    this.y += this.speedY;
                    this.x += this.speedX + Math.sin(this.angle) * 0.15;
                    this.angle += this.spinSpeed;

                    // Mouse attraction effect
                    if (mouse.active && mouse.x !== null && mouse.y !== null) {
                        const dx = mouse.x - this.x;
                        const dy = mouse.y - this.y;
                        const distance = Math.hypot(dx, dy);

                        if (distance < mouse.radius) {
                            const force = (mouse.radius - distance) / mouse.radius;
                            this.x += (dx / distance) * force * 1.2;
                            this.y += (dy / distance) * force * 1.2;
                            this.alpha = Math.min(0.9, this.alpha + 0.04);
                        }
                    }

                    // Recycle particle
                    if (this.y < 0 || this.x < 0 || this.x > width) {
                        this.reset();
                        this.y = height;
                    }
                }

                draw() {
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    
                    // Color transition mapping based on horizontal split philosophy
                    const ratio = this.x / width;
                    let hue;
                    if (ratio < 0.45) {
                        hue = 190; // Tech/Cyan
                    } else if (ratio > 0.55) {
                        hue = 25; // Art/Orange
                    } else {
                        const blend = (ratio - 0.45) / 0.1;
                        hue = 190 + (25 - 190) * blend; // linear transition in the synergy zone
                    }
                    
                    ctx.fillStyle = `hsla(${hue}, 100%, 70%, ${this.alpha})`;
                    ctx.fill();
                }
            }

            // Spawn loop
            for (let i = 0; i < maxParticles; i++) {
                particles.push(new Particle());
            }

            // Hover listeners
            heroSection.addEventListener('mousemove', (e) => {
                const rect = heroSection.getBoundingClientRect();
                mouse.x = e.clientX - rect.left;
                mouse.y = e.clientY - rect.top;
                mouse.active = true;
            }, { passive: true });

            heroSection.addEventListener('mouseleave', () => {
                mouse.active = false;
                mouse.x = null;
                mouse.y = null;
            }, { passive: true });

            // Click shockwave
            heroSection.addEventListener('mousedown', (e) => {
                const rect = heroSection.getBoundingClientRect();
                const clickX = e.clientX - rect.left;
                const clickY = e.clientY - rect.top;
                
                particles.forEach(p => {
                    const dx = p.x - clickX;
                    const dy = p.y - clickY;
                    const distance = Math.hypot(dx, dy);
                    if (distance < 160) {
                        const force = (160 - distance) / 40;
                        p.speedX += (dx / distance) * force * 0.8;
                        p.speedY += (dy / distance) * force * 0.8;
                    }
                });
            }, { passive: true });

            // Window resize handle
            let resizeTimeout;
            window.addEventListener('resize', () => {
                clearTimeout(resizeTimeout);
                resizeTimeout = setTimeout(() => {
                    width = canvas.width = heroSection.offsetWidth;
                    height = canvas.height = heroSection.offsetHeight;
                }, 150);
            }, { passive: true });

            // Render loop
            function animate() {
                ctx.clearRect(0, 0, width, height);
                for (let i = 0; i < particles.length; i++) {
                    particles[i].update();
                    particles[i].draw();
                }
                requestAnimationFrame(animate);
            }
            animate();
        };

        // Defer particle loop startup until after the page loads
        if (document.readyState === 'complete') {
            initCanvas();
        } else {
            window.addEventListener('load', initCanvas);
        }
    })();

    // 8. Obfuscated YouTube Video Facade Loader
    (function() {
        const videoMap = {
            "mv": "d21uQWxkbDFGY2c=", // Mayaaverse
            "cp": "M3pBUHhvNlhWN2M=", // Crazy Planet
            "rc": "WUttUHpkLUVDdDg=", // Reclairos
            "rr": "eDI3WnY2d2lDNXc=", // Room Raider
            "pg": "SjJNQXl5eFY1ejQ="  // Paapi Gudia
        };

        const getVid = (key) => atob(videoMap[key] || '');

        const facades = document.querySelectorAll('.video-facade');
        facades.forEach(facade => {
            facade.addEventListener('click', () => {
                const videoKey = facade.getAttribute('data-video');
                const videoId = getVid(videoKey);
                if (!videoId) return;

                // Create iframe
                const iframe = document.createElement('iframe');
                iframe.setAttribute('src', `https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&rel=0&modestbranding=1&controls=1`);
                iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
                iframe.setAttribute('allowfullscreen', 'true');
                iframe.style.width = '100%';
                iframe.style.height = '100%';
                iframe.style.border = 'none';

                // Replace facade content
                facade.innerHTML = '';
                facade.appendChild(iframe);
            });
        });
    })();

    // 9. Interactive Portfolio Filter Tabs
    (function() {
        const filterTabs = document.querySelectorAll('.filter-tab');
        const sections = document.querySelectorAll('.portfolio-section');
        
        if (filterTabs.length > 0 && sections.length > 0) {
            filterTabs.forEach(tab => {
                tab.addEventListener('click', (e) => {
                    const category = tab.getAttribute('data-category');
                    if (!category) return;
                    
                    e.preventDefault();
                    
                    // Toggle active tab class
                    filterTabs.forEach(t => t.classList.remove('active'));
                    tab.classList.add('active');
                    
                    // Show/hide sections with transition
                    sections.forEach(section => {
                        const secCat = section.getAttribute('data-category');
                        if (category === 'all' || secCat === category) {
                            section.classList.remove('hidden');
                        } else {
                            section.classList.add('hidden');
                        }
                    });
                });
            });
        }
    })();

    // 10. Interactive Subpage Hero Grid Animation
    (function () {
        const mainSection = document.querySelector('main > section:first-of-type');
        const isHomepage = document.querySelector('section.hero') !== null;
        // Only run on parent/listing pages — not on project pages or homepage
        const pageType = document.body ? document.body.getAttribute('data-page-type') : null;
        if (!mainSection || isHomepage || pageType !== 'parent') return;

        // Dynamically inject canvas element
        const canvas = document.createElement('canvas');
        canvas.className = 'subpage-hero-canvas';
        canvas.style.position = 'absolute';
        canvas.style.inset = '0';
        canvas.style.width = '100%';
        canvas.style.height = '100%';
        canvas.style.zIndex = '1';
        canvas.style.pointerEvents = 'none';

        // Prepare parent container styles
        if (getComputedStyle(mainSection).position === 'static') {
            mainSection.style.position = 'relative';
        }
        const container = mainSection.querySelector('.container');
        if (container) {
            container.style.position = 'relative';
            container.style.zIndex = '2';
        }

        mainSection.insertBefore(canvas, mainSection.firstChild);

        // Animation logic
        const ctx = canvas.getContext('2d');
        let width, height;
        const mouse = { x: null, y: null, active: false, radius: 120 };
        const nodes = [];

        // Generate grid node positions
        class GridNode {
            constructor(x, y) {
                this.baseX = x;
                this.baseY = y;
                this.x = x;
                this.y = y;
                this.angle = Math.random() * Math.PI * 2;
                this.speed = 0.01 + Math.random() * 0.01;
                this.range = 5 + Math.random() * 5; // slow floating range
            }

            update() {
                // Gentle breathing drift
                this.angle += this.speed;
                let targetX = this.baseX + Math.sin(this.angle) * this.range;
                let targetY = this.baseY + Math.cos(this.angle) * this.range;

                // Mouse interaction / warp grid field
                if (mouse.active && mouse.x !== null && mouse.y !== null) {
                    const dx = mouse.x - targetX;
                    const dy = mouse.y - targetY;
                    const dist = Math.hypot(dx, dy);

                    if (dist < mouse.radius) {
                        const force = (mouse.radius - dist) / mouse.radius;
                        // Pull nodes gently toward mouse
                        targetX += (dx / dist) * force * 14;
                        targetY += (dy / dist) * force * 14;
                    }
                }

                this.x += (targetX - this.x) * 0.1;
                this.y += (targetY - this.y) * 0.1;
            }
        }

        const initGrid = () => {
            nodes.length = 0;
            width = canvas.width = mainSection.offsetWidth;
            height = canvas.height = mainSection.offsetHeight;
            
            // Optimize grid spacing: wider spacing on mobile to reduce rendering nodes
            const gridSpacing = width < 768 ? 120 : 80;

            for (let x = 0; x < width + gridSpacing; x += gridSpacing) {
                const col = [];
                for (let y = 0; y < height + gridSpacing; y += gridSpacing) {
                    col.push(new GridNode(x, y));
                }
                nodes.push(col);
            }
        };

        // Event Listeners
        const handleMouseMove = (e) => {
            const rect = mainSection.getBoundingClientRect();
            mouse.x = e.clientX - rect.left;
            mouse.y = e.clientY - rect.top;
            mouse.active = true;
        };

        const handleTouchMove = (e) => {
            if (e.touches.length > 0) {
                const rect = mainSection.getBoundingClientRect();
                mouse.x = e.touches[0].clientX - rect.left;
                mouse.y = e.touches[0].clientY - rect.top;
                mouse.active = true;
            }
        };

        mainSection.addEventListener('mousemove', handleMouseMove, { passive: true });
        mainSection.addEventListener('touchmove', handleTouchMove, { passive: true });

        mainSection.addEventListener('mouseleave', () => { mouse.active = false; }, { passive: true });
        mainSection.addEventListener('touchend', () => { mouse.active = false; }, { passive: true });

        let resizeTimeout;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(initGrid, 150);
        }, { passive: true });

        // Animation Loop
        const animate = () => {
            ctx.clearRect(0, 0, width, height);

            // Draw Warp Grid Lines
            ctx.lineWidth = 1;
            for (let i = 0; i < nodes.length; i++) {
                for (let j = 0; j < nodes[i].length; j++) {
                    const node = nodes[i][j];
                    if (!node) continue;
                    node.update();

                    // Connect to right neighbor (horizontal line)
                    if (i < nodes.length - 1) {
                        const rightNode = nodes[i + 1][j];
                        if (rightNode) {
                            ctx.beginPath();
                            ctx.moveTo(node.x, node.y);
                            ctx.lineTo(rightNode.x, rightNode.y);
                            
                            const ratio = node.x / width;
                            const opacity = 0.02 + (mouse.active ? (1 - Math.min(Math.hypot(mouse.x - node.x, mouse.y - node.y), 200)/200) * 0.04 : 0);
                            ctx.strokeStyle = `hsla(${ratio < 0.5 ? 190 : 25}, 100%, 70%, ${opacity})`;
                            ctx.stroke();
                        }
                    }

                    // Connect to bottom neighbor (vertical line)
                    if (j < nodes[i].length - 1) {
                        const bottomNode = nodes[i][j + 1];
                        if (bottomNode) {
                            ctx.beginPath();
                            ctx.moveTo(node.x, node.y);
                            ctx.lineTo(bottomNode.x, bottomNode.y);
                            
                            const ratio = node.x / width;
                            const opacity = 0.02 + (mouse.active ? (1 - Math.min(Math.hypot(mouse.x - node.x, mouse.y - node.y), 200)/200) * 0.04 : 0);
                            ctx.strokeStyle = `hsla(${ratio < 0.5 ? 190 : 25}, 100%, 70%, ${opacity})`;
                            ctx.stroke();
                        }
                    }
                }
            }

            // Draw glowing node points
            for (let i = 0; i < nodes.length; i++) {
                for (let j = 0; j < nodes[i].length; j++) {
                    const node = nodes[i][j];
                    if (!node) continue;
                    const ratio = node.x / width;
                    const distToMouse = mouse.active && mouse.x !== null ? Math.hypot(mouse.x - node.x, mouse.y - node.y) : 999;
                    
                    ctx.beginPath();
                    ctx.arc(node.x, node.y, distToMouse < 100 ? 2 : 1, 0, Math.PI * 2);
                    
                    const hue = ratio < 0.45 ? 190 : (ratio > 0.55 ? 25 : 190 + (25 - 190) * ((ratio - 0.45)/0.1));
                    const alpha = distToMouse < 120 ? 0.3 + (1 - distToMouse/120) * 0.45 : 0.08;
                    
                    ctx.fillStyle = `hsla(${hue}, 100%, 70%, ${alpha})`;
                    ctx.fill();
                }
            }

            requestAnimationFrame(animate);
        };

        // Initialize
        initGrid();
        animate();
    })();

});
