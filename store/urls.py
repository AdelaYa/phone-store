from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('phone/new/', views.PhoneCreateView.as_view(), name='phone_new'),
    path('phone/<slug:slug>/', views.phone_detail, name='phone_detail'),
    path('phone/<slug:slug>/edit/', views.PhoneUpdateView.as_view(), name='phone_edit'),
    path('phone/<slug:slug>/delete/', views.PhoneDeleteView.as_view(), name='phone_delete'),
    path('phone/<slug:slug>/review/<int:id>/', views.delete_review, name='delete_review')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
