# Generated by Django 2.1.4 on 2018-12-16 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VslaRegion',
            fields=[
                ('RegionId', models.AutoField(primary_key=True, serialize=False)),
                ('RegionCode', models.CharField(blank=True, max_length=255, null=True)),
                ('RegionName', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': True,
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
            },
        ),
    ]
