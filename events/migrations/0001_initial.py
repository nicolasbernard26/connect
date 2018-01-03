# Generated by Django 2.0 on 2017-12-31 10:05

from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=42)),
                ('description', models.TextField(null=True)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Involvement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=events.models.file_path)),
                ('orientation', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='entries',
            field=models.ManyToManyField(through='events.Involvement', to='accounts.Profile'),
        ),
    ]