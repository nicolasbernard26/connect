# Generated by Django 2.0 on 2018-05-01 20:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'add'), (2, 'delete'), (3, 'update'), (4, 'other')], default=4)),
                ('message', models.CharField(blank=True, max_length=300)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('date_removed', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delete', models.BooleanField(default=False)),
                ('see', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('background', models.ImageField(blank=True, null=True, upload_to='backgrounds/')),
                ('inscrit_newsletter', models.BooleanField(default=False)),
                ('connections', models.ManyToManyField(related_name='_profilemodel_connections_+', to='account.ProfileModel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
