from django.contrib import admin

from .models import Registrado #importación relativa
from .forms import RegModelForm
# Register your models here.

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "email"]
    form = RegModelForm
    list_display_links = ["nombre"]
    list_filter = ["timestamp"]
    list_editable = ["email"]
    list_fields = ["email", "nombre"]

#    class Meta:
#        model = Registrado

admin.site.register(Registrado, AdminRegistrado)