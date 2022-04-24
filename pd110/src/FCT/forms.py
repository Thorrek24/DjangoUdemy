from django import forms

class SignUp(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=200)
    edad = forms.IntegerField()
    #Puesto = forms.CheckboxSelectMultiple(choices="Estudiante" "Profesor",)