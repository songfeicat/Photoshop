# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http.response import HttpResponse
from django.templatetags.static import static
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import *
from django.core.cache import cache
from django.template import loader, Context
import json
from process import *
# Create your views here.

def index(request):
    request.session['sessiontest']=3
    return render(request,'downloadApp/index.html');

def download(request):
    #data=json.dumps({'a':1,'b':2})
    #return HttpResponse(data);
    data=request.session['myname']
    return HttpResponse(data)

def novel(request):
    demotitle=u'风雷的挑衅'
    return render(request,'downloadApp/novel_detail.html',{'novelId':0,'demotitle':demotitle});

def nav(request):
    return render(request,'downloadApp/novel.html');

def novelContent(request,novelId):
    chapter = request.REQUEST.get('chapter','1');
    print 'chapterId:',chapter,' novelId:',novelId;
    return render(request,'downloadApp/novel_content.html');

def dbTest(request):
    print 'hi'
    member = Members.objects.all();

    #print member.first();
    return HttpResponse('yes')

def Bysi_Paging(request,data,pageSize,template):
    pageIndex = request.REQUEST.get('page',1);
    paginator = Paginator(data, pageSize)
    try:
        pagedata = paginator.page(pageIndex)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pagedata = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pagedata = paginator.page(paginator.num_pages)
    funny_page = render_to_string(template, {"records": pagedata}) 
    return {'funny_page':funny_page,"is_end": pagedata.number == paginator.num_pages}

def FetchNewData(request):
    records = Record.objects.all().order_by('-time');
    newNum = len(records);
    length = int(request.COOKIES.get('length',0))
    r = newNum - length
    print newNum,' ',length
    print r
    data = records[:r]
    print data
    funny_page = render_to_string('downloadApp/data_bysi.html', {"records": data}) 
    context = json.dumps(funny_page)
    response = HttpResponse(context)
    response.set_cookie('length',newNum)
    return response

def FetchNew(request):
    records = Record.objects.all().order_by('-time');
    newNum = len(records);
    length = int(request.COOKIES.get('length',0))
    if newNum<=length:
        return response_failure(code=0)
    else:
        return response_failure(code=1)

def Bysi(request):
    records = Record.objects.all();
    def query():
        return Bysi_Paging(request,records,1,'downloadApp/data_bysi.html') 
    if request.is_ajax():
        is_new = request.REQUEST.get('new','0')
        if is_new == '1':
            return FetchNew(request)
        else:
            context = json.dumps(query());
            return HttpResponse(context)
    else:
        length = len(records)
        context = query();
        response = render(request,'downloadApp/bysi.html',context);
        response.set_cookie('length',length)
        return response

def BysiLogin(request):
    return render(request,'downloadApp/bysilogin.html');

def Csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="The secret of Photoshop.doc"'
    t = loader.get_template('downloadApp/document.doc')
    c = Context({})
    response.write(t.render(c))
    return response