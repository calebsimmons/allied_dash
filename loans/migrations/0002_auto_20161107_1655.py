# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedloan',
            name='est_funding_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='closedloan',
            name='funded_milestone_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='closedloan',
            name='funds_sent_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='closedloan',
            name='total_loan_ammount',
            field=models.IntegerField(null=True),
        ),
    ]