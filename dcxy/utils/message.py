# encoding=utf-8
from ..utils import common
import requests,json,hashlib

def encrypt(data,action,KEY_STORE="dc2017"):
    _data=KEY_STORE+common.ActionDic.get(action)+data
    key=hashlib.md5(_data.encode("utf-8")).hexdigest().upper()
    return key

def create_post_data(action,token="",**kwargs):
    data=json.dumps(kwargs).replace(" ","")
    key=encrypt(data,action)
    return dict(token=token,key=key,data=data,sid=common.ActionDic.get(action), \
                reqSource="DeviceManufacturer:Apple DeviceType:XS SystemVersion:19.0 AppVersionName:3.4.1 AppVersionCode:4")

def httpsend(pdata):
    try:
        resp=requests.post(common.ApiUrl,data=pdata,headers=common.Headers)
        return resp.json()
    except Exception as e:
        print(e.args.__str__())
        return
def msg_send():
    def _msg_send(func):
        def __msg_send(class_,**kwargs):
            pdata=func(class_,**kwargs)
            return httpsend(pdata)
        return __msg_send
    return _msg_send
