# vendor_app/urls.py
from django.urls import path
from .views import VendorListCreateView, VendorRetrieveUpdateDeleteView
from .views import PurchaseOrderListCreateView, PurchaseOrderRetrieveUpdateDeleteView
from .views import HistoricalPerformanceListCreateView, HistoricalPerformanceRetrieveUpdateDeleteView
from .views import VendorPerformanceView

urlpatterns = [
    path('api/vendor/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendor/<int:pk>/', VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
     path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchase-order-retrieve-update-delete'),
     path('api/historical_performance/', HistoricalPerformanceListCreateView.as_view(), name='historical-performance-list-create'),
    path('api/historical_performance/<int:pk>/', HistoricalPerformanceRetrieveUpdateDeleteView.as_view(), name='historical-performance-retrieve-update-delete'),
    path('api/vendor/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),

]








# vendor_app/urls.py





