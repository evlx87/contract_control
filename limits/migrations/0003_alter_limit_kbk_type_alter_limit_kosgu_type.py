# Generated by Django 5.0.4 on 2024-09-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limits', '0002_alter_limit_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='limit',
            name='kbk_type',
            field=models.CharField(max_length=26),
        ),
        migrations.AlterField(
            model_name='limit',
            name='kosgu_type',
            field=models.CharField(max_length=3),
        ),
    ]
