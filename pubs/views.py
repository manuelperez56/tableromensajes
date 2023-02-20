from django.views.generic import ListView
from .models import Publicacion

# Create your views here.
class VistaPaginaInicio(ListView):
  model = Publicacion
  template_name = 'inicio.html'