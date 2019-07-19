from wxsite.models import Token
from django.utils import timezone
from wx.settings import *
import datetime
import requests
#获取token#
def getToken():
    try:
        qs = Token.objects.all()
        if qs.count() > 0 :
            token = qs.first()
        else:
            token = Token()
        if not token.expireDate is None and token.expireDate>timezone.now():
            return {'token':token.token}
        get_token_url = APIADDR["token"] % (APPCONFIG["appId"],APPCONFIG["appSecret"])
        r = requests.get(get_token_url)
        request_json = r.json()
        r.close()
        if "access_token" in request_json:
            token.token = request_json['access_token']
            token.expireDate = datetime.datetime.now()+datetime.timedelta(seconds=int(request_json['expires_in']))
            token.save()
            return {'token':token.token}
        else:
            if not token.id is None:
                token.delete()
            return {'err': request_json["errmsg"]}
    except:
        return {'err': "unknown error"}

