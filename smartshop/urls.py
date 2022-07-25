from django.urls import path
from . import views



urlpatterns = [
    path('', views.ProductList, name='product-list1'),
    path('<category_slug>/', views.products_by_category, name='product-categories'),
]