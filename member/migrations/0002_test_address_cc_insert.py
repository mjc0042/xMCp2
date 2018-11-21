from django.db import migrations
from django.conf import settings

def create_data(apps, schema_editor):
    Address = apps.get_model('member', 'Address')
    Address(street='100 Barney Lane',zipcode='14567',city='Test City',state='PA',member_id='13245687').save()

    CreditCard = apps.get_model('member', 'CreditCard')
    CreditCard(member_id='13245687',cardtype='VISA',number='4321876590127654',name='Test A Name',expiration='03/20').save()

class Migration(migrations.Migration):
    dependencies = [
        #('member', '0001_initial'),
        #('member', '0002_test_member_insert'),
        ('member', '0002_test_ru_insert'),
    ]
    operations = [
        migrations.RunPython(create_data),
    ]
