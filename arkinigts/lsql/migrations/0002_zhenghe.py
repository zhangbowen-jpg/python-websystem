# Generated by Django 2.1.8 on 2020-08-04 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsql', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zhenghe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('level', models.CharField(max_length=100, verbose_name='地位')),
                ('power', models.CharField(max_length=500, verbose_name='能力')),
                ('attack', models.CharField(max_length=10, verbose_name='攻击')),
                ('health', models.CharField(max_length=10, verbose_name='耐久')),
                ('defined', models.CharField(max_length=10, verbose_name='防御')),
                ('magic', models.CharField(max_length=10, verbose_name='魔法抗性')),
            ],
        ),
    ]
