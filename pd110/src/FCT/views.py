from multiprocessing import context
from django.shortcuts import render

from .forms import SignUp

# Create your views here.

def inicio(request):
    form = SignUp()
    context = {"the_form": form,}
    return render(request, "inicio.html", context)