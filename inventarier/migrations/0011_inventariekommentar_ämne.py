# Generated by Django 2.1.4 on 2018-12-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarier', '0010_inventariekommentar'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventariekommentar',
            name='ämne',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
