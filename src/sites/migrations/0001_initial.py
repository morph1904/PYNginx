# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-03 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('ssl', models.BooleanField(default=False)),
                ('reverse_proxy', models.BooleanField(default=False)),
                ('proxy_destination', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]