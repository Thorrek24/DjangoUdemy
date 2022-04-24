from multiprocessing import context
from webbrowser import get
from django.shortcuts import render

from .forms import SignUp
from .models import Registrado

# Create your views here.

def inicio(request):
    form = SignUp(request.POST or None)
    if form.is_valid():
       form_data = form.cleaned_data
       correo = form_data.get("email")
       usuario = form_data.get("nombre")
       userape = form_data.get("apellido")
       registro = Registrado.objects.create(email=correo, nombre=usuario, apellido=userape)
       
    context = {"the_form": form,}
    return render(request, "inicio.html", context)