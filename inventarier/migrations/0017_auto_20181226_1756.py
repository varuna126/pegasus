# Generated by Django 2.1.4 on 2018-12-26 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventarier', '0016_auto_20181226_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventarie',
            name='avdelning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avdelning_inventarier_set', to='inventarier.Avdelning'),
        ),
    ]
