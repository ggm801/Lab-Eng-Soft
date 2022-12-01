# Generated by Django 4.1.2 on 2022-12-01 18:02

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_alter_voo_nm_aeroporto_chegada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voo',
            name='DH_PREVISTO_CHEGADA',
            field=models.DateTimeField(validators=[book.models.Voo.clean]),
        ),
        migrations.AlterField(
            model_name='voo',
            name='NM_AEROPORTO_CHEGADA',
            field=models.CharField(max_length=50),
        ),
    ]
