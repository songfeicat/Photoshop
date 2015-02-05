# -*- coding: utf-8 -*-
from django.conf.urls import url
from downloadApp import wan
    
from . import views

urlpatterns = [
     url(r'^$', views.index),
     url(r'^download/$', views.download),
     url(r'^novel_detail/$', views.novel),
     url(r'^nav/$', views.nav),
     url(r'^dbTest/$', views.dbTest),
     url(r'^novel_content/([0-9]*)/$', views.novelContent),
     url(r'^bysi/$',views.Bysi),
     url(r'^bysiLogin/$',views.BysiLogin),
     url(r'^csv/$',views.Csv),
     url(r'^fetchnew/$',views.FetchNewData),
     url(r'^show_register_phone/$', wan.show_register_phone),
]