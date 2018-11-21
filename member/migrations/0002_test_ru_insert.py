from django.db import migrations
from django.conf import settings

def create_data(apps, schema_editor):
    RegisteredUser = apps.get_model('member', 'RegisteredUser')
    RegisteredUser(username='testuser',name='Test Name',password='$2b$12$bdbj8egTcl3d6jQECGOL2.fJpbbnbk/A7cpbmdwd89sixXhXpGBIa',email='testemail@gmail.com',age='27',gender='Male',income='27000',member_id='13245687').save()
    #password: pword = $2b$12$bdbj8egTcl3d6jQECGOL2.fJpbbnbk/A7cpbmdwd89sixXhXpGBIa

class Migration(migrations.Migration):
    dependencies = [
        #('member', '0001_initial'),
        ('member', '0002_test_member_insert'),
    ]
    operations = [
        migrations.RunPython(create_data),
    ]
