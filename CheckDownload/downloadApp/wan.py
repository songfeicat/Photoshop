# -*- coding: utf-8 -*-
import random
import urllib
import httplib
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.cache import cache
from django.utils import timezone
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def __get_authcode_key(phone):
    return 'authcode_%s' % phone

def __randCode():
    def randNumber():
        ar = [1,2,3,4,5,6,7,8,9,0]
        index = int(random.random()*len(ar))
        return ar[index]
    rs = ''
    for _ in range(4):
        rs = ''.join((rs,'%d' % randNumber()))
    return rs

@csrf_exempt
def show_register_phone(request):
    request.session['myname']='jie'
    return HttpResponse('jie')