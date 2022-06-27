# Generated by Django 3.1.6 on 2021-05-17 10:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rescueapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rescueclass',
            name='des',
        ),
        migrations.RemoveField(
            model_name='rescueclass',
            name='email',
        ),
        migrations.AddField(
            model_name='rescueclass',
            name='city',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='rescueclass',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='rescueclass',
            name='lama',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='rescueclass',
            name='pin',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='rescueclass',
            name='state',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='rescueclass',
            name='strt',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(default='None', max_length=500)),
                ('dt', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]