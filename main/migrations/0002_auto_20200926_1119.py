# Generated by Django 3.1 on 2020-09-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.TextField(choices=[('男性', '男性'), ('女性', '女性'), ('未選択', '未選択')], verbose_name='性別'),
        ),
    ]