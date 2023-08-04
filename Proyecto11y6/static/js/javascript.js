(function () {
    const getStoredTheme = () => localStorage.getItem('theme')
    const setStoredTheme = theme => localStorage.setItem('theme', theme)
    const getPreferredTheme = () => {
        const storedTheme = getStoredTheme()
        if (storedTheme) {
            return storedTheme
        }
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    }

    const setTheme = theme => {
        if (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.setAttribute('data-bs-theme', 'light')
        } else {
            document.documentElement.setAttribute('data-bs-theme', theme)
        }
    }

    setTheme(getPreferredTheme())

    document.querySelectorAll('[data-bs-theme-value]').forEach(toggle => {
        toggle.addEventListener('click', () => {
            const theme = toggle.getAttribute('data-bs-theme-value')
            setStoredTheme(theme)
            setTheme(theme)
        })
    })

    var labels = {
        resetTitle: 'Reiniciar',
        closeTitle: 'Cerrar',
        menuTitle: 'Menú de Accesibilidad',
        increaseText: 'Aumentar tamaño de texto',
        decreaseText: 'Disminuir tamaño de texto',
        increaseTextSpacing: 'Aumentar espaciado de texto',
        decreaseTextSpacing: 'Disminuir espaciado de texto',
        increaseLineHeight: 'Aumentar altura de línea',
        decreaseLineHeight: 'Disminuir altura de línea',
        invertColors: 'Invertir colores',
        grayHues: 'Tonos grises',
        underlineLinks: 'Subrayar enlaces',
        bigCursor: 'Cursor grande',
        readingGuide: 'Guía de lectura',
        textToSpeech: 'Texto a voz',
        speechToText: 'Voz a texto',
        disableAnimations: 'Desactivar animaciones'
    };

    var options = {
        labels: labels,
        hotkeys: {
            enabled: true
        },
        session: {
            persistent: true
        },
        icon: {
            circular: true,
            backgroundColor: '#E89E2E',
            color: '#fff',
            useEmojis: false,
            img: "accessible",

        },
    };
    options.textToSpeechLang = 'es-ES';
    options.speechToTextLang = 'es-ES';

    options.modules = {
        increaseText: true,
        decreaseText: true,
        invertColors: true,
        increaseTextSpacing: true,
        decreaseTextSpacing: true,
        increaseLineHeight: true,
        decreaseLineHeight: true,
        grayHues: true,
        underlineLinks: true,
        bigCursor: true,
        readingGuide: true,
        textToSpeech: true,
        speechToText: true,
        disableAnimations: true
    };

    window.addEventListener('load', function () { new Accessibility(options); }, false);
})();