# Generated by Django 2.1.4 on 2018-12-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarier', '0005_auto_20181218_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventarie',
            name='avdelning',
        ),
        migrations.RemoveField(
            model_name='inventarie',
            name='produkt',
        ),
        migrations.RemoveField(
            model_name='inventarie',
            name='ägare',
        ),
        migrations.AddField(
            model_name='inventarie',
            name='serienummer',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Avdelning',
        ),
        migrations.DeleteModel(
            name='Produkt',
        ),
    ]