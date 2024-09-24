from django.test import TestCase
from django.contrib.auth.models import User
from app1.models import Vehiculo, Reparacion, Cita, Mecánico
from datetime import date, time
from django.urls import reverse

class ModelosTestCase(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.usuario = User.objects.create_user(username='testuser', password='12345')
        
        # Crear un vehículo de prueba
        self.vehiculo = Vehiculo.objects.create(
            usuario=self.usuario,
            modelo='Corolla',
            marca='Toyota',
            fecha_ultima_reparacion=date(2023, 1, 1)
        )
        
        # Crear una reparación de prueba
        self.reparacion = Reparacion.objects.create(
            vehiculo=self.vehiculo,
            fecha_ingreso=date(2023, 2, 1),
            estado='En proceso',
            descripcion='Cambio de aceite'
        )
        
        # Crear una cita de prueba
        self.cita = Cita.objects.create(
            usuario=self.usuario,
            vehiculo=self.vehiculo,  
            fecha='2024-09-17',
            hora='10:00',
            tipo_servicio='Reparación'
        )

    def test_vehiculo(self):
        vehiculo = Vehiculo.objects.get(modelo='Corolla')
        self.assertEqual(vehiculo.marca, 'Toyota')
        self.assertEqual(vehiculo.usuario, self.usuario)

    def test_reparacion(self):
        reparacion = Reparacion.objects.get(vehiculo=self.vehiculo)
        self.assertEqual(reparacion.estado, 'En proceso')
        self.assertEqual(reparacion.descripcion, 'Cambio de aceite')

    def test_cita(self):
        cita = Cita.objects.get(usuario=self.usuario)
        self.assertEqual(cita.tipo_servicio, 'Reparación')
        self.assertEqual(cita.fecha, date(2024, 9, 17))

class FlujoCitaTestCase(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='testuser', password='12345')
        self.vehiculo = Vehiculo.objects.create(
            usuario=self.usuario,
            modelo='Modelo Test',
            marca='Marca Test',
            fecha_ultima_reparacion='2024-01-01',
            estado='no_reparado'
        )
        # Crear un mecánico de prueba
        self.mecanico = Mecánico.objects.create(
            nombre='Juan',
            apellido='Pérez',
            especialidad='Mecánica general',
            telefono='123456789',
            email='juan.perez@example.com'
        )
   
    def test_crear_cita(self):
        """
        Prueba de integración: Crear una cita, asignar un mecánico y actualizar el estado del vehículo
        """
        response = self.client.post(reverse('crear_cita'), {
            'vehiculo': self.vehiculo.id,
            'mecanico': self.mecanico.id,
            'fecha': '2024-09-20',
            'hora': '10:00',
            'tipo_servicio': 'Revisión general',
            'usuario': self.usuario.id
        })
        self.assertEqual(response.status_code, 302)
        
        cita = Cita.objects.get(vehiculo=self.vehiculo)
        self.assertEqual(cita.mecanico, self.mecanico)
        self.assertEqual(cita.vehiculo, self.vehiculo)
        
        self.vehiculo.estado = "reparado"
        self.vehiculo.save()
        
        vehiculo_actualizado = Vehiculo.objects.get(id=self.vehiculo.id)
        self.assertEqual(vehiculo_actualizado.estado, "reparado")
