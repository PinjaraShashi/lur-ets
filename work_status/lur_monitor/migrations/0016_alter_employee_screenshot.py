# Generated by Django 4.2.5 on 2023-12-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lur_monitor', '0015_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='screenshot',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]