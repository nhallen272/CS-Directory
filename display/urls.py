from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fac_pk>/', views.fac_detail, name='fac_detail'),
    path('edit/<int:fac_pk>/', views.fac_edit, name='fac_edit'),
]