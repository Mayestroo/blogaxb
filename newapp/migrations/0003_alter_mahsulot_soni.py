# Generated by Django 5.0.3 on 2024-04-04 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_mahsulot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='soni',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.message'),
        ),
    ]
