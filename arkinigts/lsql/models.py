from django.db import models

# Create your models here.

class Operator(models.Model):
    name = models.CharField(max_length=100, verbose_name='代号')
    place = models.CharField(max_length=100, verbose_name='出身地')
    health = models.IntegerField(verbose_name='生命上限')
    attack = models.IntegerField(verbose_name='初始攻击')
    defined = models.IntegerField(verbose_name='初始防御')
    magic = models.IntegerField(verbose_name='初始魔抗')
    a_time = models.CharField(max_length=100, verbose_name='再部署时间')
    s_cost = models.IntegerField(verbose_name='初始部署费用')
    blocked = models.IntegerField(verbose_name='初始阻挡')
    between = models.CharField(max_length=100,verbose_name='初始攻击间隔')
class Zhenghe(models.Model):
    name = models.CharField(max_length=100,verbose_name='名称')
    level = models.CharField(max_length=100,verbose_name='地位')
    power = models.CharField(max_length=500,verbose_name='能力')
    attack = models.CharField(max_length=10,verbose_name='攻击')
    health = models.CharField(max_length=10,verbose_name='耐久')
    defined = models.CharField(max_length=10,verbose_name='防御')
    magic = models.CharField(max_length=10,verbose_name='魔法抗性')
    pace = models.CharField(max_length=100, verbose_name='物种')





