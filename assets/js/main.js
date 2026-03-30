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
            } else {
                heroH1.textContent = "We Build Scalable Game Systems.";
            }
        }
    };
    updateHeroHeadline();

    // 2. Strategic Funnel & Intent Handling
    const handleContactIntent = () => {
        const urlParams = new URLSearchParams(window.location.search);
        const intent = urlParams.get('intent');
        const contactH1 = document.querySelector('main h1');
        const messageField = document.querySelector('#message');
        const projectField = document.querySelector('#project');

        if (window.location.pathname.includes('contact.html')) {
            if (intent === 'specs') {
                if (contactH1) contactH1.textContent = "Get Production Pipeline Specs";
                if (messageField) messageField.value = "I am interested in downloading the DualCore Production Pipeline Specifications. Please provide the latest technical documentation.";
                if (projectField) projectField.value = "Technical Pipeline Specs";
            } else if (intent === 'audit') {
                if (contactH1) contactH1.textContent = "Request Architecture Audit";
                if (messageField) messageField.value = "I would like to request a technical architecture audit for our current project.";
                if (projectField) projectField.value = "Architecture Audit";
            }
        }
    };
    handleContactIntent();

    // 3. Conversion Tracking
    window.trackConversion = (label) => {
        console.log(`[GTM-STAGED] Conversion Event: ${label}`);
        // Add actual GTM dataLayer push here if needed
        // window.dataLayer = window.dataLayer || [];
        // window.dataLayer.push({'event': 'conversion', 'label': label});
    };

    // Attach tracking to specific buttons
    document.querySelectorAll('a[href*="intent="]').forEach(btn => {
        btn.addEventListener('click', () => {
            const intent = new URLSearchParams(btn.search).get('intent');
            trackConversion(`Intent: ${intent}`);
        });
    });
    // 4. Form Submission & AJAX Redirect
    const forms = document.querySelectorAll('#contactForm, #contactFormTwo');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.textContent;
            
            submitBtn.disabled = true;
            submitBtn.textContent = 'SENDING...';

            const formData = new FormData(form);
            fetch(form.action, {
                method: 'POST',
                body: formData,
                mode: 'no-cors'
            })
            .then(() => {
                window.location.href = 'thank-you.html';
            })
            .catch(() => {
                alert("Oops! There was a problem submitting your form. Please try again.");
                submitBtn.disabled = false;
                submitBtn.textContent = originalBtnText;
            });
        });
    });


    // 5. Nav Toggle & Accessibility
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

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
        // ... (remaining nav logic preserved)
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
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            faqItems.forEach(faq => {
                faq.classList.remove('active');
                faq.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
            });

            if (!isActive) {
                item.classList.add('active');
                question.setAttribute('aria-expanded', 'true');
            }
        });
    });
});

