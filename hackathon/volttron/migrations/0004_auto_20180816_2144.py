# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-16 21:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volttron', '0003_auto_20180803_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volttron',
            name='jupyter_port',
            field=models.IntegerField(choices=[(8896, 8896), (8897, 8897), (8898, 8898), (8899, 8899), (8900, 8900), (8881, 8881), (8882, 8882), (8883, 8883), (8884, 8884), (8885, 8885), (8886, 8886), (8887, 8887), (8888, 8888), (8889, 8889), (8890, 8890), (8891, 8891), (8892, 8892), (8893, 8893), (8894, 8894), (8895, 8895)], help_text=b'Port for Jupyter Notebook', unique=True),
        ),
        migrations.AlterField(
            model_name='volttron',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='volttron',
            name='vc_port',
            field=models.IntegerField(choices=[(8096, 8096), (8097, 8097), (8098, 8098), (8099, 8099), (8100, 8100), (8081, 8081), (8082, 8082), (8083, 8083), (8084, 8084), (8085, 8085), (8086, 8086), (8087, 8087), (8088, 8088), (8089, 8089), (8090, 8090), (8091, 8091), (8092, 8092), (8093, 8093), (8094, 8094), (8095, 8095)], help_text=b'Port for volttron central', unique=True),
        ),
        migrations.AlterField(
            model_name='volttron',
            name='vip_port',
            field=models.IntegerField(choices=[(22912, 22912), (22913, 22913), (22914, 22914), (22915, 22915), (22916, 22916), (22917, 22917), (22918, 22918), (22919, 22919), (22920, 22920), (22921, 22921), (22922, 22922), (22923, 22923), (22924, 22924), (22925, 22925), (22926, 22926), (22927, 22927), (22928, 22928), (22929, 22929), (22930, 22930), (22911, 22911)], help_text=b'Instance port for the vip address', unique=True),
        ),
    ]
