# vendor_app/models.py
from django.db import models

class Vendor(models.Model):
    vendor_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, unique=True)
    vendor_reference = models.CharField(max_length=50)
    order_date = models.DateField()
    items = models.TextField()
    quantity = models.PositiveIntegerField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    quality_rating = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_performance_metrics()

    def update_performance_metrics(self):
        if self.status == 'completed':
            self.update_on_time_delivery_rate()
            self.update_quality_rating_avg()
        if self.acknowledgment_date:
            self.update_average_response_time()
        self.update_fulfillment_rate()

    # Update the 'update_on_time_delivery_rate' method in the PurchaseOrder model
    def update_on_time_delivery_rate(self):
        completed_orders = PurchaseOrder.objects.filter(
            vendor=self.vendor,
            status='completed',
            delivery_date__isnull=False).count()

        on_time_deliveries = PurchaseOrder.objects.filter(
            vendor=self.vendor,
            status='completed',
            delivery_date__isnull=False,
            delivery_date__lte=models.F('acknowledgment_date')).count()

        if completed_orders > 0:
            self.vendor.performance.on_time_delivery_rate = on_time_deliveries / completed_orders
            self.vendor.performance.save()

    # Update the 'update_quality_rating_avg' method in the PurchaseOrder model
    def update_quality_rating_avg(self):
        completed_orders_with_ratings = PurchaseOrder.objects.filter(
            vendor=self.vendor,
            status='completed',
            quality_rating__isnull=False)

        total_ratings = completed_orders_with_ratings.aggregate(models.Avg('quality_rating'))['quality_rating__avg']

        if total_ratings:
            self.vendor.performance.quality_rating_avg = total_ratings
            self.vendor.performance.save()

    # Update the 'update_average_response_time' method in the PurchaseOrder model
    def update_average_response_time(self):
        acknowledged_orders = PurchaseOrder.objects.filter(
            vendor=self.vendor,
            acknowledgment_date__isnull=False)

        total_response_time = acknowledged_orders.aggregate(models.Avg(models.F('acknowledgment_date') - models.F('order_date')))['acknowledgment_date__avg']

        if total_response_time:
            self.vendor.performance.average_response_time = total_response_time.total_seconds() / 60  # convert to minutes
            self.vendor.performance.save()

    # Update the 'update_fulfillment_rate' method in the PurchaseOrder model
    def update_fulfillment_rate(self):
        total_orders = PurchaseOrder.objects.filter(vendor=self.vendor).count()
        fulfilled_orders = PurchaseOrder.objects.filter(
            vendor=self.vendor,
            status='completed',
            issues__isnull=True).count()

        if total_orders > 0:
            self.vendor.performance.fulfillment_rate = fulfilled_orders / total_orders
            self.vendor.performance.save()




    

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
    

# vendor_app/models.py
class VendorPerformance(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name='performance')
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return f"{self.vendor.name} Performance"

