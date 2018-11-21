from django.db import migrations
from django.conf import settings

def create_data(apps, schema_editor):
    Member = apps.get_model('member', 'Member')
    Member(member_id='13245687',phone_number='8005551000').save()

class Migration(migrations.Migration):
    dependencies = [
        ('member', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_data),
    ]
