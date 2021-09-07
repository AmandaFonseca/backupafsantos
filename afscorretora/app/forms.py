from django.forms import ModelForm
from app.models import Cliente
from django import  forms

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
