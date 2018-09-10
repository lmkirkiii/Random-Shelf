from django.urls import path
from . import views

urlpatterns = [
    path('', views.treasure_list, name='treasure_list'),
    path('treasures/<int:pk>', views.treasure_detail, name='treasure_detail'),
    path('treasures/new', views.treasure_create, name='treasure_create'),
    path('treasures/<int:pk>/edit', views.treasure_edit, name='treasure_edit'),
]
