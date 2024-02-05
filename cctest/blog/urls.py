from django.urls import path, include
from .apis.products import ProductApi

urlpatterns = [
    path('product/',ProductApi.as_view(),name="product")
]