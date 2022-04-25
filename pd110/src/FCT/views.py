from multiprocessing import context
from webbrowser import get
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactForm, RegModelForm
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
       correo = form.cleaned_data.get("email")
       usuario = form.cleaned_data.get("nombre")
       userape = form.cleaned_data.get("apellido")
       if not instance.nombre:
           instance.nombre = "Usuario"
           instance.save()
       if not nombre:
            nombre = "anonimo"
            context = {"titulo": "Gracias {}".format(nombre)}
       #registro = Registrado.objects.create(email=correo, nombre=usuario, apellido=userape)

    
    return render(request, "inicio.html", context)

def contact(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():
        #Formas de controlar el display
        #1.
         form_email = form.cleaned_data.get("email")
         form_nombre = form.cleaned_data.get("nombre")
         form_apellido = form.cleaned_data.get("apellido")
         form_mensaje = form.cleaned_data.get("mensaje")
         asunto = "Form de Contacto"
         email_from = settings.EMAIL_HOST_USER
         email_to = [email_from, "anotherone@gmail.com"]
         email_mensaje = "{} {}:{} enviado por {}".format(form_nombre, form_apellido, form_mensaje, form_email)
         
         send_mail(asunto, email_mensaje, email_from, email_to, fail_silently=False)
         print (form_email, form_nombre, form_apellido, form_mensaje)
        #2.
        # for key in form.changed_data:
        #     print(key)
        #     print(form.cleaned_data.get(key))
        #3.
        # for key, value in form.cleaned_data.iteritems():
        #     print(key, value)
    context ={"form": form,}

    return render(request, "forms.html", context)