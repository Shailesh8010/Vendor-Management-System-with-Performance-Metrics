# vendor_app/serializers.py
from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'vendor_code', 'name', 'contact_details', 'address']




from .models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


from .models import HistoricalPerformance

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'



from .models import VendorPerformance

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPerformance
        fields = '__all__'
