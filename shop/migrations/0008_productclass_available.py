# Generated by Django 2.0.2 on 2018-03-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20180225_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='productclass',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
