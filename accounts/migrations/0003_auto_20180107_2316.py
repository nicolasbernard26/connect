# Generated by Django 2.0 on 2018-01-07 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180107_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='followers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='accounts.Profile'),
        ),
    ]