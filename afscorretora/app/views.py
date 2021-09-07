from django.shortcuts import render
from django.http import HttpResponse
from .forms import ClienteForm

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from app.serializers import ClienteSerializer
from app.models import Cliente

# Create your views here.
class ListClienteAPIView(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CreateClienteAPIView(CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class UpdateClienteAPIView(UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class DeleteClienteAPIView(DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'form.html', data)