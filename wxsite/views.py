from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.utils.encoding import smart_str
from wx.msg import WxMsg

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def msgRev(request):
    msg =  WxMsg(smart_str(request.body))
    print(msg)
    return JsonResponse({'errCode':0}, safe=False)
