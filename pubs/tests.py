from django.test import TestCase
from django.urls import reverse

from .models import Publicacion

# Create your tests here.
class PruebasPublicacion(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.publicacion = Publicacion.objects.create(texto='ESTO ES UNA PRUEBA!')

  def test_contenido_modelo(self):
    self.assertEqual(self.publicacion.texto, 'ESTO ES UNA PRUEBA!')

  def test_url_existe_en_ubicacion_correcta(self):
    respuesta = self.client.get('/')
    self.assertEqual(respuesta.status_code, 200)

  def test_url_disponible_por_nombre(self):
    respuesta = self.client.get(reverse('inicio'))
    self.assertEqual(respuesta.status_code, 200)

  def test_contenido_plantilla(self):
    respuesta = self.client.get(reverse('inicio'))
    self.assertContains(respuesta, 'ESTO ES UNA PRUEBA!')

  def test_pagina_inicio(self):
    respuesta = self.client.get(reverse('inicio'))
    self.assertEqual(respuesta.status_code, 200)
    self.assertTemplateUsed(respuesta, 'inicio.html')  #VERIFICA QUE EL TEMPLATE QUE SE OBTIENE SEA IGUAL A INICIO.HTML
    self.assertContains(respuesta, 'ESTO ES UNA PRUEBA!')
    
