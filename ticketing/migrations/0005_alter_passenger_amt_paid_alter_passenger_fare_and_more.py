# Generated by Django 4.2.13 on 2024-05-14 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0004_auto_20240430_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='amt_paid',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='fare',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='fingerprint',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='paid',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]