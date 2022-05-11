from django.urls import path, include 

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('faculty/<int:fac_pk>', views.fac_detail, name='fac_detail'),
    path('edit/', views.fac_edit, name='edit'),
    path('research/<str:r_cat>', views.research_category, name='research_category'),
    #path('login/', views.login_user, name='login'),

]