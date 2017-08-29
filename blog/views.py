from django.shortcuts import render
from django.utils import timezone
from .models import Publicar

def listar_pub(request):
    posts = Publicar.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html', {'posts': posts})
