document.addEventListener('DOMContentLoaded', () => {
    // Nav Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        const toggleMenu = (open) => {
            const isOpen = open !== undefined ? open : !navMenu.classList.contains('active');
            navMenu.classList.toggle('active', isOpen);
            navToggle.classList.toggle('active', isOpen);
            document.body.classList.toggle('nav-open', isOpen);
        };

        navToggle.addEventListener('click', () => toggleMenu());

        // Handle Close Button inside menu if it exists
        const navClose = navMenu.querySelector('.nav-close');
        if (navClose) {
            navClose.addEventListener('click', () => toggleMenu(false));
        }

        // Handle mobile dropdowns
        const dropdowns = document.querySelectorAll('.has-dropdown');
        dropdowns.forEach(dropdown => {
            const toggleWrapper = dropdown.querySelector('.dropdown-toggle');
            if (toggleWrapper) {
                toggleWrapper.addEventListener('click', (e) => {
                    if (window.innerWidth <= 1024) {
                        // Only prevent default and toggle if exactly clicking the chevron icon or its immediate hit area
                        if (e.target.classList.contains('dropdown-icon') || e.target.closest('.dropdown-icon')) {
                            e.preventDefault();
                            dropdown.classList.toggle('active');
                        }
                    }
                });
            }
        });

        // Close menu on link click (excluding dropdown toggles)
        document.querySelectorAll('.nav-link:not(.dropdown-toggle), .dropdown-menu .dropdown-link, .nav-menu .btn').forEach(link => {
            link.addEventListener('click', () => toggleMenu(false));
        });
    }

    // FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            // Close all items
            faqItems.forEach(faq => faq.classList.remove('active'));

            // Open clicked if it wasn't active
            if (!isActive) {
                item.classList.add('active');
            }
        });
    });

    // Sticky Header
    const header = document.querySelector('header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }
    // Hero Mouse Glow & Energy Ripple
    const hero = document.querySelector('.hero');
    if (hero) {
        let lastRippleTime = 0;
        let targetX = -2000;
        let targetY = -2000;
        let currentInnerX = -2000;
        let currentInnerY = -2000;
        let isHovering = false;
        let breathTimeout = null;

        let currentFarX = 0, currentFarY = 0;
        let currentMidX = 0, currentMidY = 0;
        let currentNearX = 0, currentNearY = 0;

        const layerFar = hero.querySelector('.layer-far');
        const layerMid = hero.querySelector('.layer-mid');
        const layerNear = hero.querySelector('.layer-near');

        // Smooth Lerp loop for inner energy tracking and physics parallax
        const updateGlow = () => {
            if (!isHovering) return;

            // Outer boundaries for parallax calculation (normalized -1 to 1)
            const rect = hero.getBoundingClientRect();
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const normalizedX = (targetX - centerX) / centerX;
            const normalizedY = (targetY - centerY) / centerY;

            // Inverted targets for depth effect
            const targetFarX = normalizedX * -6;
            const targetFarY = normalizedY * -6;

            const targetMidX = normalizedX * -10;
            const targetMidY = normalizedY * -10;

            const targetNearX = normalizedX * -14;
            const targetNearY = normalizedY * -14;

            // Apply lerp friction
            currentInnerX += (targetX - currentInnerX) * 0.12;
            currentInnerY += (targetY - currentInnerY) * 0.12;

            currentFarX += (targetFarX - currentFarX) * 0.08;
            currentFarY += (targetFarY - currentFarY) * 0.08;

            currentMidX += (targetMidX - currentMidX) * 0.08;
            currentMidY += (targetMidY - currentMidY) * 0.08;

            currentNearX += (targetNearX - currentNearX) * 0.08;
            currentNearY += (targetNearY - currentNearY) * 0.08;

            // Set CSS variables and Transforms
            hero.style.setProperty('--mouse-x-inner', `${currentInnerX}px`);
            hero.style.setProperty('--mouse-y-inner', `${currentInnerY}px`);

            if (layerFar) layerFar.style.transform = `translate3d(${currentFarX}px, ${currentFarY}px, 0)`;
            if (layerMid) layerMid.style.transform = `translate3d(${currentMidX}px, ${currentMidY}px, 0)`;
            if (layerNear) layerNear.style.transform = `translate3d(${currentNearX}px, ${currentNearY}px, 0)`;

            requestAnimationFrame(updateGlow);
        };

        hero.addEventListener('mouseenter', (e) => {
            if (window.innerWidth < 768) return;

            const rect = hero.getBoundingClientRect();
            targetX = e.clientX - rect.left;
            targetY = e.clientY - rect.top;
            currentInnerX = targetX;
            currentInnerY = targetY;

            isHovering = true;
            hero.classList.add('is-ignited');
            hero.classList.add('hero-fast-breath');

            clearTimeout(breathTimeout);
            breathTimeout = setTimeout(() => {
                hero.classList.remove('hero-fast-breath');
            }, 2000);

            requestAnimationFrame(updateGlow);
        });

        hero.addEventListener('mouseleave', () => {
            isHovering = false;
            hero.classList.remove('is-ignited');
            hero.classList.remove('hero-fast-breath');

            // Smoothly reset parallax layers to center on leave
            if (layerFar) layerFar.style.transform = `translate3d(0, 0, 0)`;
            if (layerMid) layerMid.style.transform = `translate3d(0, 0, 0)`;
            if (layerNear) layerNear.style.transform = `translate3d(0, 0, 0)`;
            currentFarX = 0; currentFarY = 0;
            currentMidX = 0; currentMidY = 0;
            currentNearX = 0; currentNearY = 0;
        });

        hero.addEventListener('mousemove', (e) => {
            // Disable interactions entirely on mobile mapping to the lowest tier 768 ruleset for physics
            if (window.innerWidth < 768) return;

            const rect = hero.getBoundingClientRect();
            targetX = e.clientX - rect.left;
            targetY = e.clientY - rect.top;

            // Atmospheric hover glow tracking (Layer 1 tracks instantly)
            hero.style.setProperty('--mouse-x', `${targetX}px`);
            hero.style.setProperty('--mouse-y', `${targetY}px`);

            // Energy displacement ripple logic
            const now = Date.now();
            if (now - lastRippleTime > 150) { // 150ms throttle prevents FPS drop and controls node creation
                const currentRipples = hero.querySelectorAll('.hero-ripple');

                // Cap active energy ripples to 4 max to prevent brightness blowout
                if (currentRipples.length < 4) {
                    lastRippleTime = now;

                    const ripple = document.createElement('div');
                    ripple.className = 'hero-ripple';
                    ripple.style.left = `${targetX}px`;
                    ripple.style.top = `${targetY}px`;

                    hero.appendChild(ripple);

                    // Cleanup trailing nodes exactly when their animation sequence fades out
                    setTimeout(() => {
                        if (ripple.parentNode) {
                            ripple.parentNode.removeChild(ripple);
                        }
                    }, 900);
                }
            }
        });
    }
});
