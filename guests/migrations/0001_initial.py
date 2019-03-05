# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-24 23:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Homem'), ('F', 'Mulher'), ('ND', 'N\xe3o Informado')], default='ND', max_length=3)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(99)])),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('work', models.BooleanField(default=False)),
                ('study', models.BooleanField(default=False)),
                ('smoking', models.BooleanField(default=False)),
                ('garage', models.BooleanField(default=False)),
                ('max_value', models.IntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(2000)])),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.City')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.State')),
            ],
            options={
                'verbose_name_plural': 'Guests',
            },
        ),
    ]
