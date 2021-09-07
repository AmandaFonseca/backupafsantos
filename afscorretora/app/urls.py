from django.contrib import admin
from django.urls import path
from app import views
from app.views import home, form, createview

urlpatterns = [
    path('form/', form, name="form"),
    path('createview/', createview, name="createview"),


    path("list/",views.ListClienteAPIView.as_view(),name="cliente_list"),
    path("create/", views.CreateClienteAPIView.as_view(),name="cliente_create"),
    path("update/<int:pk>/",views.UpdateClienteAPIView.as_view(),name="update_cliente"),
    path("delete/<int:pk>/",views.DeleteClienteAPIView.as_view(),name="delete_cliente")
]
