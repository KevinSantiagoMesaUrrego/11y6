(function () {
    const getStoredTheme = () => localStorage.getItem('theme')

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

        $(document).ready(function () {
            $("#frmCrearEvento").submit(function (event) {
                // Obtener los valores de las fechas
                var fechaInicio = new Date($("#id_fecha_inicio").val());
                var fechaFin = new Date($("#id_fecha_fin").val());
                var fechaActual = new Date();

                // Validar si la fecha de inicio es superior a la fecha actual
                if (fechaInicio <= fechaActual) {
                    alert("La fecha de inicio debe ser posterior a la fecha actual.");
                    event.preventDefault(); // Evitar el envío del formulario
                }

                // Validar si la fecha de fin es mayor a la fecha de inicio
                if (fechaFin <= fechaInicio) {
                    alert("La fecha de fin debe ser posterior a la fecha de inicio.");
                    event.preventDefault(); // Evitar el envío del formulario
                }
            });
        });