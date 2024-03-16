from django.urls import path
from . import views
urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products),
    path('deposit-products/', views.deposit_products),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options),
    path('save-saving-products/', views.save_saving_products),
    path('saving-products/', views.saving_products),
    path('make-newdeposits/', views.make_newdeposits),
    path('new-deposits/', views.new_deposits),
    path('make-newsavings/', views.make_newsavings),
    path('new-savings/', views.new_savings),
]