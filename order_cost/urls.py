from django.urls import path, include
from .views import GetOrderValue

urlpatterns=[
    path('get_order_value/', GetOrderValue.as_view(), name='get_order_value'),
]