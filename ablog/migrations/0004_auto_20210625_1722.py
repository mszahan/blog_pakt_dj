# Generated by Django 3.1.7 on 2021-06-25 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0003_mainpost_section'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MainPost',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
