import datetime

from django.db import models

# Create your models here.

class Mark(models.Model):
    client = models.CharField(max_length=100, verbose_name='客户端号')
    mark = models.IntegerField(max_length=10000, verbose_name='分数')
    update_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name='更新时间')

    class Meta:
        db_table = 'mark'