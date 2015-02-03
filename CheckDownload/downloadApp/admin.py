# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id','desc')
    list_filter = ('zan','cai','forward','comment_num')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','record')

admin.site.register(Record,RecordAdmin)
admin.site.register(Comment,CommentAdmin)
