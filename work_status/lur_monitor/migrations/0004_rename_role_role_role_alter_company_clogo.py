# Generated by Django 4.2.5 on 2023-12-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lur_monitor', '0003_project_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='Role',
            new_name='role',
        ),
        migrations.AlterField(
            model_name='company',
            name='cLogo',
            field=models.FileField(blank=True, null='true', upload_to='images'),
        ),
    ]