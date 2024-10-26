from django.urls import path
from .views import ProductView, OrderView, ProductUpdateView, ProductSupplierView
urlpatterns = [
    path('product/', ProductView.as_view()),
    path('product-update/<str:id>', ProductUpdateView.as_view()),
    path('product-suppliers/<str:id>', ProductSupplierView.as_view()),

    path('order/', OrderView.as_view()),

]
