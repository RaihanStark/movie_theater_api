# Generated by Django 3.1.1 on 2020-09-16 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200917_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theater',
            name='showtime',
        ),
        migrations.AddField(
            model_name='theater',
            name='showtime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='showtime', to='api.showtime'),
        ),
    ]
