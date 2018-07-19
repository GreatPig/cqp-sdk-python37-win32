import sys
import os
# 不支持改变目录，当前文件读写目录还是酷Q的目录
# os.chdir('C:/Users/Administrator/Downloads/cq/cq/app/com.example.democ')

def out(s):
    with open('cqsdk-测试.txt', 'ab+') as f:
        f.write((s+'\r\n').encode())


import cqsdk
from cqsdk import CqSdk


sdk = CqSdk()

global AUTH_CODE
AUTH_CODE = 0 # 调用cpq.dll用

# 尽量不要使用多线程，gil会死锁
# cqp_event_group_msg 内置一个群消息自动回复

# return True 拦截消息
# return False 忽略消息


# Type=1002 酷Q退出
# 无论本应用是否被启用，本函数都会在酷Q退出前执行一次，请在这里执行插件关闭代码。
# 本函数调用完毕后，酷Q将很快关闭，请不要再通过线程等方式执行其他代码。

def cqp_event_exit() -> None:
    out('cqp_event_exit')
    pass


# Type=1003 应用已被启用
# 当应用被启用后，将收到此事件。
# 如果酷Q载入时应用已被启用，则在_eventStartup(Type=1001,酷Q启动)被调用后，本函数也将被调用一次。
# 如非必要，不建议在这里加载窗口。（可以添加菜单，让用户手动打开窗口）

def cqp_event_enable(auth_code:int, appid:str)-> None:
    global AUTH_CODE
    AUTH_CODE = auth_code

    # 当前目录是cq, 我在C++内改变当前目录，插件就无法重载代码，所以传appid也就是目录名，给你自己修改
    # 传入appid, 其实就是目录名:com.xx.xx
    # 那么你改变当前目录，就是 curdir = '/app/' + appid

    out('cqp_event_enable')
    pass


# Type=1004 应用将被停用
# 当应用被停用前，将收到此事件。
# 如果酷Q载入时应用已被停用，则本函数*不会*被调用。
# 无论本应用是否被启用，酷Q关闭前本函数都*不会*被调用。

def cqp_event_disable()-> None:
    out('cqp_event_disable')
    pass



# Type=21 私聊消息
# subType 子类型，11/来自好友 1/来自在线状态 2/来自群 3/来自讨论组

def cqp_event_private_msg(subType:int, msgId:int, fromQQ:int, msg:str, font:int) -> int:
    out('cqp_event_private_msg')
    return 0



# Type=2 群消息

def cqp_event_group_msg(subType:int, msgId:int, fromGroup:int, fromQQ:int, fromAnonymous:str, msg:str, font:int) -> int:
    sdk.sendGroupMsg(AUTH_CODE, fromGroup, msg)        
    # return cqsdk.EVENT_BLOCK
    return False

# Type=4 讨论组消息

def cqp_event_discuss_msg(subType:int, msgId:int, fromDiscuss:int, fromQQ:int, msg:str, font:int) -> int:
    out('cqp_event_discuss_msg')
    return 0


# Type=101 群事件-管理员变动
# subType 子类型，1/被取消管理员 2/被设置管理员

def cqp_event_group_admin(subType:int, sendTime:int, fromGroup:int, beingOperateQQ:int) -> int:
    out('cqp_event_group_admin')
    return 0


# Type=102 群事件-群成员减少
# subType 子类型，1/群员离开 2/群员被踢 3/自己(即登录号)被踢
# fromQQ 操作者QQ(仅subType为2、3时存在)
# beingOperateQQ 被操作QQ

def cqp_event_group_member_decrease(subType:int, sendTime:int, fromGroup:int, fromQQ:int, beingOperateQQ:int) -> int:
    out('cqp_event_group_member_decrease')
    return 0



# Type=103 群事件-群成员增加
# subType 子类型，1/管理员已同意 2/管理员邀请
# fromQQ 操作者QQ(即管理员QQ)
# beingOperateQQ 被操作QQ(即加群的QQ)

def cqp_event_group_member_increase(subType:int, sendTime:int, fromGroup:int, fromQQ:int, beingOperateQQ:int) -> int:
    out('cqp_event_group_member_increase')
    return 0


# Type=201 好友事件-好友已添加

def cqp_event_group_friend_add(subType:int, sendTime:int, fromQQ:int) -> int:
    out('cqp_event_group_friend_add')
    return 0


# Type=301 请求-好友添加
# msg 附言
# responseFlag 反馈标识(处理请求用)

def cqp_event_add_friend(subType:int, sendTime:int, fromQQ:int, msg:str, responseFlag:str) -> int:
    out('cqp_event_add_friend')
    return 0


# Type=302 请求-群添加
# subType 子类型，1/他人申请入群 2/自己(即登录号)受邀入群
# msg 附言
# responseFlag 反馈标识(处理请求用)

def cqp_event_add_group(subType:int, sendTime:int, fromGroup:int, fromQQ:int, msg:str, responseFlag:str) -> int:
    out('cqp_event_add_group')
    return


# 一共10个菜单，index分别是1 - 10
def cqp_event_menu(index:int) -> None:
    pass