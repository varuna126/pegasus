# Generated by Django 2.1.4 on 2018-12-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventarie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventarie_nummer', models.IntegerField()),
                ('tillverkare', models.CharField(max_length=255)),
                ('modell', models.CharField(max_length=255)),
                ('inköpt', models.DateField()),
                ('rum', models.CharField(max_length=255)),
            ],
        ),
    ]
