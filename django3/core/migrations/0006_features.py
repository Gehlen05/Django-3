# Generated by Django 4.0.6 on 2022-07-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_instagran_funcionario_instagram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('feature', models.CharField(max_length=100, verbose_name='Feature')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-laptop-phone', 'Notebook'), ('lni-leaf', 'Folha'), ('lni-layers', 'Design'), ('lni-rocket', 'Foguete')], max_length=16, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Serviço',
            },
        ),
    ]
