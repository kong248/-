# Generated by Django 3.2.16 on 2023-01-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_alter_userinfo_depart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateField(verbose_name='入职时间'),
        ),
    ]