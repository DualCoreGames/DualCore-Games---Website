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

        // Dynamic Active State Logic
        const setNavActive = () => {
            const currentPath = window.location.pathname;
            const navLinks = document.querySelectorAll('.nav-link, .dropdown-link');

            navLinks.forEach(link => {
                link.classList.remove('active');
                const linkPath = link.getAttribute('href');

                // Handle various path styles (absolute, relative, index)
                if (linkPath) {
                    const normalizedLinkPath = linkPath.replace(/\.\.\//g, '').replace(/^\//, '');
                    const normalizedCurrentPath = currentPath.replace(/^\//, '');

                    // Exact match or logical parent match
                    if (normalizedLinkPath === normalizedCurrentPath ||
                        (normalizedCurrentPath === '' && normalizedLinkPath === 'index.html') ||
                        (normalizedCurrentPath.includes(normalizedLinkPath.replace('/index.html', '')) && normalizedLinkPath !== 'index.html')) {
                        link.classList.add('active');
                    }
                }
            });
        };
        setNavActive();
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

});
