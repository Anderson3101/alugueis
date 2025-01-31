# Generated by Django 5.1.4 on 2025-01-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0004_alter_despesa_descricao_alter_despesa_kw_final_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='descricao',
            field=models.CharField(choices=[('Energia', 'Energia'), ('Água', 'Água')], max_length=50),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='kw_final',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='kw_inicial',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
