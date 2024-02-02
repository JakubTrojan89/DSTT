from django.contrib import admin
from django.urls import path, include
from gijutsu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPageView.as_view(), name='main'),
    path('accounts/', include('accounts.urls')),
    path('gijutsu/', include('gijutsu.urls')),
]