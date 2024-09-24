/* static confirmacion de citas js */

document.getElementById('citaForm').addEventListener('submit', function (event)
{
    const telefono = document.getElementById('telefono').value;
    const telefonoRegex = /^\d{10}$/; // Ejemplo: solo 10 dígitos

    if (telefono && !telefonoRegex.test(telefono))
    {
        alert('El número de teléfono debe tener 10 dígitos.');
        event.preventDefault(); // Detiene el envío del formulario
    }
});
