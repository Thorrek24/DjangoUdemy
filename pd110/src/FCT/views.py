from multiprocessing import context
from webbrowser import get
from django.shortcuts import render

from .forms import SignUp, RegModelForm
from .models import Registrado

# Create your views here.

def inicio(request):
    form = RegModelForm(request.POST or None)
    titulo = "Registrese en la FCT"
    context = {"the_form": form, "titulo": titulo,}

    if request.user.is_authenticated:
        titulo = "Bienvenido {}".format(request.user)
        context = {"the_form": form, "titulo": titulo,}
    

    if form.is_valid():
       instance = form.save(commit=False)
       correo = form.cleaned_datadata.get("email")
       usuario = form.cleaned_datadata.get("nombre")
       userape = form.cleaned_datadata.get("apellido")
       if not instance.nombre:
           instance.nombre = "Usuario"
           instance.save()
       if not nombre:
            nombre = "anonimo"
            context = {"titulo": "Gracias {}".format(nombre)}
       #registro = Registrado.objects.create(email=correo, nombre=usuario, apellido=userape)

    
    return render(request, "inicio.html", context)