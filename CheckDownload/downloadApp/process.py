import json
from django.http.response import HttpResponse

def response_json(data):
    return HttpResponse(content=json.dumps(data),content_type='text/json')

def response_success(**args):
    datas = args.pop('data',None)
    return response_json(datas)

def response_failure(**args):
    datas = args.pop('code',-1)
    return response_json(datas)