# Generated by Django 3.2.16 on 2023-01-17 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='depart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.department'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(1, '男'), (2, '女')], null=True, verbose_name='性别'),
        ),
    ]
