# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-12 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='numero',
            field=models.CharField(max_length=10, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.Tipo', verbose_name='Tipo'),
        ),
    ]
