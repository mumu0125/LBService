# @Time : 2020/4/26 23:06 
# @Author : 张成涛
# @File : urls.py 
# @Software: PyCharm
from django.conf.urls import url

from ranking.views import Ranking

urlpatterns = [
    url(r'rank/mark/$', Ranking.as_view()),   #客户端分数排行榜增post查get接口
]