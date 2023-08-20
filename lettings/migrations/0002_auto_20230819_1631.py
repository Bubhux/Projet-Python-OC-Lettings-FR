from django.db import migrations


def migrate_copy_data_address(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')  # Ancien modèle
    NewAddress = apps.get_model('lettings', 'Address')          # Nouveau modèle

    for old_obj in OldAddress.objects.all():
        new_obj = NewAddress()
        new_obj.number = old_obj.number
        new_obj.street = old_obj.street
        new_obj.city = old_obj.city
        new_obj.state = old_obj.state
        new_obj.zip_code = old_obj.zip_code
        new_obj.country_iso_code = old_obj.country_iso_code
        new_obj.save()

def migrate_copy_data_lettings(apps, schema_editor):
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')  # Ancien modèle
    NewLetting = apps.get_model('lettings', 'Letting')          # Nouveau modèle
    NewAddress = apps.get_model('lettings', 'Address')          # Nouveau modèle

    for old_obj in OldLetting.objects.all():
        new_obj = NewLetting()
        new_obj.title = old_obj.title

        # Récupérez l'instance correcte d'Address
        old_address = old_obj.address
        new_address = NewAddress.objects.get(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )
        new_obj.address = new_address

        new_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_copy_data_address),
        migrations.RunPython(migrate_copy_data_lettings),
    ]
