# Generated by Django 4.1.3 on 2022-12-01 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vooreal',
            name='DH_REAL_CHEGADA',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='vooreal',
            name='DH_REAL_SAIDA',
            field=models.DateTimeField(),
        ),
    ]
