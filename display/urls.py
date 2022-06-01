from django.urls import path, include 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('faculty/<int:fac_pk>', views.fac_detail, name='fac_detail'),
    path('edit/<int:fac_pk>', views.FacEditView.as_view(), name='edit'),
    path('research/<str:r_cat>', views.research_category, name='research_category'),
    path('welcome/', views.welcome, name='welcome'),

]
urlpatterns += staticfiles_urlpatterns()
