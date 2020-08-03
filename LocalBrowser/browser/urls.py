from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='browser-home'),
    path('browser/', views.browser, name='browser-browser'),
    path('about/', views.about, name='browser-about'),
    path('contact/', views.contact, name='browser-contact'),
    path('panel/', views.panel, name='give-panel'),
    path('reset/', views.reset, name='reset')
]