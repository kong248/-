# Generated by Django 3.2.16 on 2023-01-17 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_remove_userinfo_depart'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='depart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.department'),
        ),
    ]
