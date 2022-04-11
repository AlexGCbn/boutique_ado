from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),  # URL for adding item to bag
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),  # URL for adjusting bag items
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),  # URL for deleting bag items
]
