from django.db import migrations


def forwards(apps, schema_editor):
    from django.contrib.auth.models import User
    from django.db import transaction
    try:
        with transaction.atomic():
            superuser = User.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                password='admin'
            )
            superuser.save()
    except:
        pass
    # Your migration code goes here


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
