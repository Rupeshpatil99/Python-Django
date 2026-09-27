from django.urls import path
from . import views

#localhost:8000/GOT/
#localhost:8000/GOT/order/

urlpatterns = [
  path('', views.all_got, name='all_got'),
]  
