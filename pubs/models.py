from django.db import models

# Create your models here.
class Publicacion(models.Model):
  texto = models.TextField()

  def _str_(self):
    return self.texto[:50]
  
