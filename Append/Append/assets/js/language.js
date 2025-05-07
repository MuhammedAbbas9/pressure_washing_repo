function loadLanguage(lang) {
if (lang === 'fr') {
    fetch('./lang/fr.json')
    .then(response => response.json())
    .then(translations => {
        // Translate by ID (for unique elements)
        for (const key in translations) {
        const element = document.getElementById(key);
        if (element) {
            element.innerText = translations[key];
        }
        }

        // Translate all elements with data-key
        document.querySelectorAll('.translate').forEach(el => {
        const key = el.getAttribute('data-key');
        if (translations[key]) {
            el.innerText = translations[key];
        }
        });
    });
} else if (lang === 'en') {
    window.location.reload(); // Resets to original English content
}
}