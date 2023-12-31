# Generated by Django 4.2.5 on 2023-12-23 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lur_monitor', '0014_remove_employee_ecompany_remove_employee_empid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=50)),
                ('cEmail', models.EmailField(max_length=254)),
                ('cLogo', models.ImageField(blank=True, null=True, upload_to='media')),
                ('cUrl', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='empId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empid', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'empId',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eFname', models.CharField(max_length=50, unique='true')),
                ('eLname', models.CharField(max_length=50)),
                ('eEmail', models.EmailField(max_length=50)),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='media')),
                ('url', models.URLField(null=True)),
                ('apps', models.CharField(max_length=100, null=True)),
                ('ePhone', models.CharField(max_length=50, null=True)),
                ('eCompany', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lur_monitor.company')),
                ('empId', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lur_monitor.empid')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Proj_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Proj_status',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default=0, max_length=50)),
            ],
            options={
                'db_table': 'Role',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(default=0, max_length=50)),
                ('ePhone', models.CharField(max_length=50)),
                ('eCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lur_monitor.company')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lur_monitor.employee')),
                ('pclient', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lur_monitor.clients')),
                ('status', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lur_monitor.proj_status')),
            ],
            options={
                'db_table': 'Project',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='empRole',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lur_monitor.role'),
        ),
        migrations.AddField(
            model_name='clients',
            name='eCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lur_monitor.company'),
        ),
        migrations.AddField(
            model_name='clients',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lur_monitor.employee'),
        ),
        migrations.AddField(
            model_name='clients',
            name='pro_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lur_monitor.role'),
        ),
    ]
