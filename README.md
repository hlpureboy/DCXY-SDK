# DCXY-SDK
多彩校园app python版sdk

代码实例

```python
from dcxy.api.center import User
u=User("phone","password")
data=u.login()
# 登陆
data=u.RefreshIdBar()
# 刷新一维码
# 其一维码的生成是code128的编码方式
data=u.FindUserAccount()
# 获取用户剩余金额
data=u.GetUserInfo()
# 获取用户个人信息
data=u.ChangeDevicePwd(devicepwd="2222")
# 注意 四位密码
# 改变用户设备密码
```

> java版本的稍后更新