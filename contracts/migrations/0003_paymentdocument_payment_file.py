# Generated by Django 5.0.4 on 2024-05-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_paymentorder_pp_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdocument',
            name='payment_file',
            field=models.FileField(blank=True, null=True, upload_to='payment_docs/', verbose_name='Файл платежного документа'),
        ),
    ]
