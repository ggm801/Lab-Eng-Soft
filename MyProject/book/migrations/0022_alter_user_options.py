# Generated by Django 4.1.2 on 2022-12-01 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0021_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('view_voo_atual', 'can view voo atual'), ('access_relatorio', 'can access relatorio page'), ('generate_relatorio ', 'can generate relatorio'), ('access_atualizar', 'can access to atualizar voo page'), ('edit_atual', 'can edit oo real'))},
        ),
    ]
