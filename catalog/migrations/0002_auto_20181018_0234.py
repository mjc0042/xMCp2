from django.db import migrations
from django.conf import settings

def create_data(apps, schema_editor):
    Product = apps.get_model('catalog', 'Product')
    Product(sku='sku1',name='Product 1', description='Product 1', buyPrice=100 , sellPrice=100,unit='kilogram', quantity=100).save()
    Product(sku='sku2',name='Product 2', description='Product 2', buyPrice=25 , sellPrice=150,unit='kilogram', quantity=40).save()
    Product(sku='sku3',name='Product 3', description='Product 3', buyPrice=300 , sellPrice=200,unit='kilogram', quantity=75).save()

class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_data),
    ]
