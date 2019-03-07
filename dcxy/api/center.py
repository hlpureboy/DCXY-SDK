# encoding=utf-8
from dcxy.utils.message import msg_send,httpsend,create_post_data

class User(object):
    def __init__(self,account,password):
        self.__account=account
        self.__password=password
        self.__token=""
        self.__userid=""
    def Login(self):
        pdata=create_post_data("Login",account=self.__account,password=self.__password)
        resp=httpsend(pdata)
        if resp.get("data"):
            self.__token=resp.get("data").get("token")
            self.__userid=resp.get("data").get("userId")
            print(self.__token)
            return resp
        else:
            return resp

    @msg_send()
    def __msg_http_send(self,action=""):
        return create_post_data(action,token=self.__token,account=self.__account,userId=self.__userid)
    def RefreshIdBar(self):
        return self.__msg_http_send(action="RefreshIdBar")
    def FindUserAccount(self):
        return self.__msg_http_send(action="FindUserAccount")
    def GetUserInfo(self):
        return self.__msg_http_send(action="GetUserInfo")
    @msg_send()
    def ChangeDevicePwd(self,devicepwd="2222"):
        return create_post_data("ChangeDevicePwd",token=self.__token,account=self.__account,userId=self.__userid,newpwd=devicepwd,oldPwd=self.__password, \
                                updateType="3")