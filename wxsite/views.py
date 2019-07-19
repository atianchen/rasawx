from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.utils.encoding import smart_str
from wx.message import WxMsg
from wx.api import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def msgRecv(request):
    msg =  WxMsg(smart_str(request.body))
    #HttpResponse(open('myxmlfile.xml').read(), content_type='text/xml')
    return JsonResponse({'errCode':0}, safe=False)

def token(request):
    return JsonResponse(getToken(), safe=False)
