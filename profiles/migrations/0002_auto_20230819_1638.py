from django.db import migrations


def migrate_copy_data_profiles(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')  # Ancien modèle
    NewProfile = apps.get_model('profiles', 'Profile')          # Nouveau modèle

    for old_obj in OldProfile.objects.all():
        new_obj = NewProfile()
        new_obj.user = old_obj.user
        new_obj.favorite_city = old_obj.favorite_city
        new_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_copy_data_profiles),
    ]
