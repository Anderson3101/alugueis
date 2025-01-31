# Generated by Django 5.1.4 on 2025-01-09 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('casas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes_referencia', models.DateField()),
                ('valor_aluguel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pago', models.BooleanField(default=False)),
                ('casa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alugueis', to='casas.casa')),
            ],
        ),
    ]
