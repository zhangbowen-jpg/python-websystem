from django.db import models

# Create your models here.
class Manager(models.Model):
    managername = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=30,verbose_name='密码')
    nickname = models.CharField(max_length=20,verbose_name='昵称')
    def __str__(self):
        return self.nickname
    class Meta:
        verbose_name = '管理员帐号'
        verbose_name_plural = verbose_name

