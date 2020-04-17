from django.urls import path
from .views import (
    HomeView, 
    checkout_view, 
    ItemDetailView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('checkout/', checkout_view, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name="product"),

]