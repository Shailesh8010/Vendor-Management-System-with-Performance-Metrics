# vendor_app/views.py
from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


# vendor_app/views.py

from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer



from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer

class HistoricalPerformanceListCreateView(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

class HistoricalPerformanceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer


# vendor_app/views.py

from .models import Vendor, VendorPerformance, PurchaseOrder
from .serializers import VendorPerformanceSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = VendorPerformance.objects.all()
    serializer_class = VendorPerformanceSerializer

    def get_object(self):
        vendor_id = self.kwargs['vendor_id']
        vendor = generics.get_object_or_404(Vendor, pk=vendor_id)
        return generics.get_object_or_404(VendorPerformance, vendor=vendor)
