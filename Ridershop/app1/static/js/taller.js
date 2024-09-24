// static.js
document.addEventListener('DOMContentLoaded', function ()
{
    // Seleccionar el elemento header
    const header = document.querySelector('.header');

    // Aplicar la imagen de fondo
    header.style.backgroundImage = "url('/static/imagenes/header.jpg')";
    header.style.backgroundSize = 'cover';
    header.style.backgroundPosition = 'center';
    header.style.position = 'relative';
    header.style.color = '#fff';
    header.style.minHeight = '89vh'; // Ajusta la altura mínima al 100% de la ventana de visualización

    // Crear una capa de superposición oscura
    const overlay = document.createElement('div');
    overlay.style.position = 'absolute';
    overlay.style.top = 0;
    overlay.style.left = 0;
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
    overlay.style.zIndex = 1;

    // Insertar la superposición antes del contenido de la cabecera
    header.insertBefore(overlay, header.firstChild);

    // Ajustar la posición del contenido de la cabecera
    const headerContent = document.querySelector('.header-content');
    headerContent.style.position = 'relative';
    headerContent.style.zIndex = 2;
});


// Script para manejar el modal
document.addEventListener('DOMContentLoaded', function ()
{
    var modal = document.getElementById('estadoModal');
    var btn = document.getElementById('btnEstado');
    var span = document.getElementsByClassName('close')[0];
    var form = document.getElementById('modalForm');

    // Abrir el modal cuando se hace clic en el botón
    btn.onclick = function ()
    {
        modal.style.display = 'block';
    }

    // Cerrar el modal cuando se hace clic en la 'X'
    span.onclick = function ()
    {
        modal.style.display = 'none';
    }

    // Cerrar el modal cuando se hace clic fuera de él
    window.onclick = function (event)
    {
        if (event.target == modal)
        {
            modal.style.display = 'none';
        }
    }

    // Captura del formulario
    form.onsubmit = function (event)
    {
        event.preventDefault();
        alert('Datos enviados correctamente');
        modal.style.display = 'none';
    }
});

