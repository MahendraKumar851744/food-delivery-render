from django.contrib import admin
from django.urls import path
from delivery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate_delivery_price/', views.calculate_delivery_price),
]
