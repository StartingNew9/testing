from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_item, name='add_item'),
    path('claim/<int:item_id>/', views.mark_claimed, name='mark_claimed'),
]
