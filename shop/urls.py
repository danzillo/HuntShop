from django.urls import path
from .views import HomePageView, CustomersListView, OrdersListView, SearchView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('customers', CustomersListView.as_view(), name='customers'),
    path('orders', OrdersListView.as_view(), name='orders'),
    path('search', SearchView.as_view(), name='search'),
]
