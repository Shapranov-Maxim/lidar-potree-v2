# Generated by Django 4.2.5 on 2024-07-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("las_files", "0003_alter_lasfilemodel_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lasfilemodel",
            name="name",
            field=models.CharField(max_length=100000),
        ),
    ]
