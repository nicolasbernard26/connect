# Generated by Django 2.0 on 2018-01-09 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180107_2316'),
        ('events', '0004_auto_20180109_1724'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='involvement',
            unique_together={('event', 'profile')},
        ),
    ]
