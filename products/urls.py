from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),  # Product detail view
    path('add/', views.add_product, name='add_product'),  # Add product  view
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),  # Add product  view
]
