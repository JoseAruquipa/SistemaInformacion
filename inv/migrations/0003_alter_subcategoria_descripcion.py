# Generated by Django 4.2.13 on 2024-06-06 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0002_subcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoria',
            name='descripcion',
            field=models.CharField(help_text='Descripcion de categoria', max_length=100),
        ),
    ]
