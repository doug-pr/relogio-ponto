# Generated by Django 5.1.6 on 2025-02-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada_1', models.DateTimeField()),
                ('saida_1', models.DateTimeField()),
                ('entrada_2', models.DateTimeField()),
                ('saida_2', models.DateTimeField()),
                ('entrada_3', models.DateTimeField()),
                ('saida_3', models.DateTimeField()),
            ],
        ),
    ]
