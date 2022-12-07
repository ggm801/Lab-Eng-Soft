# Generated by Django 4.1.3 on 2022-12-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_alter_vooreal_id_voo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vooreal',
            name='NM_STATUS',
            field=models.CharField(choices=[('EM', 'Embarcando'), ('CA', 'Cancelado'), ('PR', 'Programado'), ('TA', 'Taxeando'), ('PO', 'Pronto'), ('AU', 'Autorizado'), ('VO', 'Em voo')], default='EM', max_length=50),
        ),
    ]
