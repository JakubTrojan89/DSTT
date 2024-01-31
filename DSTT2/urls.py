from django.contrib import admin
from django.urls import path

from gijutsu import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('main/', views.MainPageView.as_view(), name='main'),
    path('martialart/', views.MartialArtView.as_view(), name='martial_art'),
    path('addmartialart/', views.AddMartialArtView.as_view(), name='add_martial_art'),
    path('addtechniquetype/', views.AddTechniqueTypeView.as_view(), name='add_technique_type')
]