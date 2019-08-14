from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.utils.encoding import smart_str
from wx.message import WxMsg
from wx.api import *
import time

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def msgRecv(request):
    if request.method == "POST":
        recvMsg = WxMsg(smart_str(request.body))
        sendMsg = WxMsg()
        sendMsg.content = "Hello"
        sendMsg.msgType = recvMsg.msgType
        sendMsg.fromUserName = recvMsg.toUserName
        sendMsg.toUserName = recvMsg.fromUserName
        sendMsg.createTime = int(round(time.time() * 1000))
        # HttpResponse(open('myxmlfile.xml').read(), content_type='text/xml')
        return HttpResponse(bytes(str, encoding='utf8'), content_type="text/xml")
    else:
        signature = request.GET.get('msg_signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echo_str = request.GET.get('echostr', '')
        try:
            ret, sEchoStr = wxcpt.VerifyURL(signature, timestamp, nonce, echo_str)
            if (ret != 0):
                print("ERR: VerifyURL ret: " + str(ret))
        except InvalidSignatureException:
            return HttpResponse("Weixin-NO")
        return HttpResponse(sEchoStr, content_type="text/plain")


def token(request):
    return JsonResponse(getToken(), safe=False)