from django.shortcuts import render

def listar_pub(request):
    return render(request, 'blog/listar_pub.html',{})
