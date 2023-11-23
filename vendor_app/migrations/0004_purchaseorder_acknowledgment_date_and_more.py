# Generated by Django 4.1.4 on 2023-11-23 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0003_historicalperformance'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='acknowledgment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='quality_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='VendorPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_time_delivery_rate', models.FloatField(default=0)),
                ('quality_rating_avg', models.FloatField(default=0)),
                ('average_response_time', models.FloatField(default=0)),
                ('fulfillment_rate', models.FloatField(default=0)),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='performance', to='vendor_app.vendor')),
            ],
        ),
    ]