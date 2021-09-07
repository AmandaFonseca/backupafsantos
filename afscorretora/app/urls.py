from django.contrib import admin
from django.urls import path
from app import views
from app.views import home, form

urlpatterns = [
    path('', home),
    path('form/', form),
    path("list/",views.ListClienteAPIView.as_view(),name="cliente_list"),
    path("create/", views.CreateClienteAPIView.as_view(),name="cliente_create"),
    path("update/<int:pk>/",views.UpdateClienteAPIView.as_view(),name="update_cliente"),
    path("delete/<int:pk>/",views.DeleteClienteAPIView.as_view(),name="delete_cliente")
]
