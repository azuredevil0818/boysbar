# Generated by Django 4.2.6 on 2023-10-25 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0010_alter_bar_bar_eid_alter_bar_bar_position_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bars_Casts',
            new_name='Bar_Fk_Casts',
        ),
    ]
