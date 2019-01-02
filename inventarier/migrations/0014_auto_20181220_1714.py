# Generated by Django 2.1.4 on 2018-12-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarier', '0013_auto_20181220_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avdelning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avdelning_namn', models.CharField(max_length=255)),
                ('kostnadsställe', models.CharField(max_length=10)),
                ('lokal', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='inventarie',
            name='rum',
            field=models.CharField(default='', max_length=255),
        ),
    ]