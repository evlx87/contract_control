# Generated by Django 5.0.4 on 2024-09-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('kbk_type', models.CharField(max_length=26)),
                ('kosgu_type', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remaining_limit', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
