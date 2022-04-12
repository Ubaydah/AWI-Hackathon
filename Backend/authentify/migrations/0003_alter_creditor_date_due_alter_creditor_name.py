# Generated by Django 4.0.4 on 2022-04-12 12:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentify', '0002_creditor_wallet_wallettransaction_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditor',
            name='date_due',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 12, 12, 30, 7, 415938, tzinfo=utc), verbose_name='date_due'),
        ),
        migrations.AlterField(
            model_name='creditor',
            name='name',
            field=models.CharField(max_length=250, verbose_name='name'),
        ),
    ]