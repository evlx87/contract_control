# Generated by Django 5.0.4 on 2024-05-03 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_alter_contract_contract_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Наименование объекта закупки'),
        ),
    ]