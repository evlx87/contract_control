# Generated by Django 5.1.4 on 2024-12-28 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KBK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=26, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='KOSGU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remaining_limit', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('year', models.PositiveIntegerField(default=2024)),
                ('kbk', models.ForeignKey(default='00', on_delete=django.db.models.deletion.PROTECT, to='limits.kbk')),
                ('kosgu', models.ForeignKey(default='00', on_delete=django.db.models.deletion.PROTECT, to='limits.kosgu')),
            ],
        ),
    ]
