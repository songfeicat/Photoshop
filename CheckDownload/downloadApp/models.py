#coding:utf8
from django.db import models
from django.utils.timezone import now


class Record(models.Model):
    desc = models.CharField(max_length = 500, verbose_name = u'描述')
    pic = models.FileField(upload_to = 'record/', verbose_name = u'图片')
    time = models.DateTimeField(default = now, verbose_name = u'上传时间')
    zan = models.IntegerField(default = 0, verbose_name = u'赞')
    cai = models.IntegerField(default = 0, verbose_name = u'踩')
    forward = models.IntegerField(default = 0, verbose_name = u'转发数')
    comment_num = models.IntegerField(default = 0, verbose_name = u'评论数')
    
    class Meta:
        verbose_name_plural = verbose_name = u"笑话记录"
    
class Comment(models.Model):
    record = models.ForeignKey(Record, verbose_name = u'条目')
    content = models.CharField(max_length = 500, verbose_name = u'评论')
    
    class Meta:
        verbose_name_plural = verbose_name = u"评论"