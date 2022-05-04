from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('faculty/<int:fac_pk>', views.fac_detail, name='fac_detail'),
    path('edit/<int:fac_pk>/', views.fac_edit, name='fac_edit'),
    path('research/<str:r_cat>', views.research_category, name='research_category'),
    path('login/', views.fac_login, name='fac_login'),
]