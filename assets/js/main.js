document.addEventListener('DOMContentLoaded', () => {
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

        if (window.location.pathname.includes('contact.html')) {
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
    const forms = document.querySelectorAll('form.contact-form, form.beta-form, #contactForm, #contactFormTwo, #reclairosBetaForm, #paapiContactForm, #roomRaiderForm, #audit-form-element, #notd-form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Honeypot spam bot check
            const honeypot = form.querySelector('input[name="honeypot_field"]');
            if (honeypot && honeypot.value) {
                console.warn("Spam submission blocked via honeypot.");
                const parts = window.location.pathname.split('/').filter(Boolean);
                if (parts.length > 0 && parts[parts.length - 1].includes('.')) {
                    parts.pop();
                }
                const prefix = '../'.repeat(parts.length);
                window.location.href = prefix + 'thank-you.html';
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
                // Calculate relative prefix depending on directory depth to point to root thank-you.html correctly
                const parts = window.location.pathname.split('/').filter(Boolean);
                if (parts.length > 0 && parts[parts.length - 1].includes('.')) {
                    parts.pop(); // Remove filename if present to get correct folder depth
                }
                const prefix = '../'.repeat(parts.length);
                window.location.href = prefix + 'thank-you.html';
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

});
