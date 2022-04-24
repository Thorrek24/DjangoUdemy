from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre", "apellido", "email"]
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not dominio == "iesfernandoaguilar" and extension == "es":
            raise forms.ValidationError("Utiliza un correo corporativo (iesfernandoaguilar.es)")

        return email

class SignUp(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=200)
    email = forms.EmailField()
    edad = forms.IntegerField()
    #Puesto = forms.CheckboxSelectMultiple(choices="Estudiante" "Profesor",)