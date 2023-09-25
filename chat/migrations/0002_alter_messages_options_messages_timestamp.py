# Generated by Django 4.2.5 on 2023-09-25 17:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'ordering': ('timestamp',)},
        ),
        migrations.AddField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
