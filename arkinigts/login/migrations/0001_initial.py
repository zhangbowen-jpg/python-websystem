# Generated by Django 2.1.8 on 2020-08-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('managername', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
            ],
            options={
                'verbose_name': '管理员帐号',
                'verbose_name_plural': '管理员帐号',
            },
        ),
    ]
