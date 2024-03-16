from django.urls import path
from . import views
urlpatterns = [
    path('save-rates/', views.save_exchange_rates),
    path('exchange/', views.get_exchange_rates)
]