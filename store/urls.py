from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('phone/new/', views.PhoneCreateView.as_view(), name='phone_new'),
    path('phone/<slug:slug>/', views.PhoneDetailView.as_view(), name='phone_detail'),
    path('phone/<slug:slug>/edit/', views.PhoneUpdateView.as_view(), name='phone_edit'),
    path('phone/<slug:slug>/delete/', views.PhoneDeleteView.as_view(), name='phone_delete'),
]
