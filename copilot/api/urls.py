
from django.urls import path

from . import views 

urlpatterns = [
    path('time/', views.get_current_time),
    path('hello/', views.hello_world_view),
    path('azure-vms', views.get_azure_vms),
]
