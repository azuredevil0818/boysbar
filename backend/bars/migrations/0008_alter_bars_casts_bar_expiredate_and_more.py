# Generated by Django 4.2.6 on 2023-10-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0007_remove_cast_cast_barid_cast_fk_bars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bars_casts',
            name='bar_expiredate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='bars_casts',
            name='bar_recorddate',
            field=models.DateField(null=True),
        ),
    ]