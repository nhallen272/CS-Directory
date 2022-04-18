from django.urls import path

from . import views
#from .views import IndexView, FacView

urlpatterns = [
    path('', views.index, name='index'),
    path('faculty/<int:fac_pk>', views.fac_detail, name='fac_detail'),
    path('edit/<int:fac_pk>/', views.fac_edit, name='fac_edit'),
    path('testidx/', views.IndexView.as_view(), name='testidx'),
    path('facview/', views.FacView.as_view(), name='facview'),
]