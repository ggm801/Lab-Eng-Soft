# Generated by Django 4.1.3 on 2022-12-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0025_alter_vooreal_nm_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField(blank=True, null=True)),
                ('data_fim', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Relatorio',
            },
        ),
    ]
