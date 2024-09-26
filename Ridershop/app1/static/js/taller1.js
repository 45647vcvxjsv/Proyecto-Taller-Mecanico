document.addEventListener('DOMContentLoaded', function ()
{
    // Inicializar Flatpickr para la fecha
    const fechaInput = document.getElementById('fecha');
    const fechaHiddenInput = document.getElementById('fecha_hidden');

    flatpickr(fechaInput, {
        dateFormat: "d/m/Y",
        minDate: "today",
        inline: true,
        locale: "es",
        onChange: function (selectedDates, dateStr)
        {
            fechaHiddenInput.value = dateStr;
        }
    });

    // Inicializar Flatpickr para la hora
    flatpickr("#hora", {
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
        minTime: "09:00",
        maxTime: "18:00",
        locale: "es"
    });

    // Validación del formulario
    const form = document.getElementById('citaForm');
    form.addEventListener('submit', function (event)
    {
        let isValid = true;

        // Validar fecha
        if (!fechaHiddenInput.value)
        {
            isValid = false;
            mostrarError(fechaInput, 'Por favor, selecciona una fecha');
        } else
        {
            ocultarError(fechaInput);
        }

        // Validar hora
        const hora = document.getElementById('hora');
        if (!hora.value)
        {
            isValid = false;
            mostrarError(hora, 'Por favor, selecciona una hora');
        } else
        {
            ocultarError(hora);
        }

        // Validar tipo de servicio
        const tipoServicio = document.getElementById('tipo_servicio');
        if (!tipoServicio.value)
        {
            isValid = false;
            mostrarError(tipoServicio, 'Por favor, selecciona un tipo de servicio');
        } else
        {
            ocultarError(tipoServicio);
        }

        if (!isValid)
        {
            event.preventDefault();
        }
    });

    function mostrarError(elemento, mensaje)
    {
        let error = elemento.nextElementSibling;
        if (!error || !error.classList.contains('error'))
        {
            error = document.createElement('div');
            error.classList.add('error');
            elemento.parentNode.insertBefore(error, elemento.nextSibling);
        }
        error.textContent = mensaje;
    }

    function ocultarError(elemento)
    {
        let error = elemento.nextElementSibling;
        if (error && error.classList.contains('error'))
        {
            error.textContent = '';
        }
    }
});