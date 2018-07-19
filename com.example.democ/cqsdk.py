## 作者: alphafase
# import win32api
# pywin32  有bug，不能加载


from ctypes import *
class CqSdk:
    EVENT_IGNORE = 0          #事件_忽略
    EVENT_BLOCK = 1           #事件_拦截

    REQUEST_ALLOW = 1         #请求_通过
    REQUEST_DENY = 2          #请求_拒绝

    REQUEST_GROUPADD = 1      #请求_群添加
    REQUEST_GROUPINVITE = 2   #请求_群邀请

    CQLOG_DEBUG = 0           #调试 灰色
    CQLOG_INFO = 10           #信息 黑色
    CQLOG_INFOSUCCESS = 11    #信息(成功) 紫色
    CQLOG_INFORECV = 12       #信息(接收) 蓝色
    CQLOG_INFOSEND = 13       #信息(发送) 绿色
    CQLOG_WARNING = 20        #警告 橙色
    CQLOG_ERROR = 30          #错误 红色
    CQLOG_FATAL = 40          #致命错误 深红

    def __init__(self):
        self.CQDLL = WinDLL('cqp.dll')


    """
    发送私聊消息, 成功返回消息ID
    QQID 目标QQ号
    msg 消息内容
    """
    def sendPrivateMsg(AuthCode:int, QQID:int, msg:str) -> int:
        return self.CQDLL.CQ_sendPrivateMsg(c_int(AUTH_CODE), c_longlong(QQID), c_char_p(msg.encode('gbk')))
    """
    发送群消息, 成功返回消息ID
    groupid 群号
    msg 消息内容
    """
    def sendGroupMsg(self, AUTH_CODE:int, fromGroup:int, msg:str) -> int:
        return self.CQDLL.CQ_sendGroupMsg(c_int(AUTH_CODE), c_longlong(fromGroup), c_char_p(msg.encode('gbk')))
    """
    发送讨论组消息, 成功返回消息ID
    discussid 讨论组号
    msg 消息内容
    """
    def sendDiscussMsg(AuthCode:int, discussid:int, msg:str) -> int:
        return self.CQDLL.CQ_sendDiscussMsg(c_int(AUTH_CODE), c_longlong(QQID), c_char_p(msg.encode('gbk')))
    """
    撤回消息
    msgid 消息ID
    """
    def deleteMsg(AuthCode:int, msgid:int) -> int:
        return self.CQDLL.CQ_deleteMsg(c_int(AUTH_CODE), c_longlong(msgid))
    """
    发送赞 发送手机赞
    QQID QQ号
    """
    def sendLike(AuthCode:int, QQID:int) -> int:
        return self.CQDLL.CQ_sendLike(c_int(AUTH_CODE), c_int(QQID)) 
    """
    置群员移除
    groupid 目标群
    QQID QQ号
    rejectaddrequest 不再接收此人加群申请，请慎用
    """
    def CQ_setGroupKick(AuthCode:int, groupid:int, QQID:int, rejectaddrequest:bool) -> int:
        return self.CQDLL.CQ_setGroupKick(c_int(AuthCode), c_int(groupid), c_int(QQID), c_bool(rejectaddrequest)) 
    """
    置群员禁言
    groupid 目标群
    QQID QQ号
    duration 禁言的时间，单位为秒。如果要解禁，这里填写0。
    """
    def setGroupBan(AuthCode:int, groupid:int, QQID:int, duration:int) -> int:
         return self.CQDLL.CQ_setGroupBan(c_int(AuthCode), c_int(groupid), c_int(QQID), c_bool(rejectaddrequest)) 
    """
    置群管理员
    groupid 目标群
    QQID QQ号
    setadmin true:设置管理员 false:取消管理员
    """
    def CQ_setGroupAdmin(AuthCode:int, groupid:int, QQID:int, setadmin:bool) ->int:
        return self.CQDLL.CQ_setGroupBan(c_int(AuthCode), c_int(groupid), c_int(QQID), c_bool(rejectaddrequest)) 
    
    """
    置全群禁言
    groupid 目标群
    enableban true:开启 false:关闭
    """
    def setGroupWholeBan(AuthCode:int, groupid:int, enableban:bool) ->int:
        return self.CQDLL.CQ_setGroupWholeBan(c_int(AuthCode), c_int(groupid), c_bool(rejectaddrequest)) 
    """
    置匿名群员禁言
    groupid 目标群
    anomymous 群消息事件收到的 anomymous 参数
    duration 禁言的时间，单位为秒。不支持解禁。
    """
    def setGroupAnonymousBan(AuthCode:int, groupid:int, anomymous:str, duration:int) ->int:
        return self.CQDLL.CQ_setGroupAnonymousBan(c_int(AuthCode), c_int(groupid), c_char_p(anomymous.encode('gbk')), c_int(duration)) 
    """
    置群匿名设置
    groupid 目标群
    enableanomymous true:开启 false:关闭
    """
    def setGroupAnonymous(AuthCode:int, groupid:int, enableanomymous:bool) ->int:
        return self.CQDLL.CQ_setGroupAnonymous(c_int(AuthCode), c_int(groupid), c_bool(enableanomymous)) 
    """
    置群成员名片
    groupid 目标群
    QQID 目标QQ
    newcard 新名片(昵称)
    """
    def setGroupCard(AuthCode:int, groupid:int, QQID:int, newcard:str) ->int:
        return self.CQDLL.CQ_setGroupCard(c_int(AuthCode), c_int(groupid), c_int(QQID), c_char_p(enableanomymous.encode('gbk'))) 
    """
    置群退出 慎用, 此接口需要严格授权
    groupid 目标群
    isdismiss 是否解散 true:解散本群(群主) false:退出本群(管理、群成员)
    """
    def setGroupLeave(AuthCode:int, groupid:int, isdismiss:bool) ->int:
        return self.CQDLL.CQ_setGroupLeave(c_int(AuthCode), c_int(groupid), c_bool(isdismiss)) 
    """
    置群成员专属头衔 需群主权限
    groupid 目标群
    QQID 目标QQ
    newspecialtitle 头衔（如果要删除，这里填空）
    duration 专属头衔有效期，单位为秒。如果永久有效，这里填写-1。
    """
    def setGroupSpecialTitle(AuthCode:int, groupid:int, QQID:int, newspecialtitle:str, duration:int) ->int:
        return self.CQDLL.CQ_setGroupSpecialTitle(c_int(AuthCode), c_int(groupid), c_int(QQID), c_char_p(newspecialtitle.encode('gbk')), c_int(duration)) 
    """
    置讨论组退出
    discussid 目标讨论组号
    """
    def setDiscussLeave(AuthCode:int, discussid:int) ->int:
        return self.CQDLL.CQ_setDiscussLeave(c_int(AuthCode), c_int(discussid))

    """
    置好友添加请求
    responseflag 请求事件收到的 responseflag 参数
    responseoperation REQUEST_ALLOW 或 REQUEST_DENY
    remark 添加后的好友备注
    """
    def setFriendAddRequest(AuthCode:int, responseflag:str, responseoperation:int, remark:str) ->int:
        return self.CQDLL.CQ_setFriendAddRequest(c_int(AuthCode), c_char_p(responseflag.encode('gbk')), c_int(responseoperation), c_char_p(remark.encode('gbk'))) 

    """
    置群添加请求
    responseflag 请求事件收到的 responseflag 参数
    requesttype根据请求事件的子类型区分 REQUEST_GROUPADD 或 REQUEST_GROUPINVITE
    responseoperation  REQUEST_ALLOW 或 REQUEST_DENY
    reason 操作理由，仅 REQUEST_GROUPADD 且 REQUEST_DENY 时可用
    """
    def setGroupAddRequestV2(AuthCode:int, responseflag:str, requesttype:int, responseoperation:int, reason:str) ->int:
        return self.CQDLL.CQ_setGroupAddRequestV2(c_int(AuthCode), c_char_p(responseflag.encode('gbk')), c_int(requesttype), c_int(responseoperation), c_char_p(reason.encode('gbk'))) 
    """
    取群成员信息
    groupid 目标QQ所在群
    QQID 目标QQ号
    nocache 不使用缓存
    """
    def getGroupMemberInfoV2(AuthCode:int, groupid:int, QQID:int, nocache:bool) ->str:
        return self.CQDLL.CQ_getGroupMemberInfoV2(c_int(AuthCode), c_int(groupid), c_int(QQID), c_bool(nocache))
    """
    取陌生人信息
    QQID 目标QQ
    nocache 不使用缓存
    """
    def getStrangerInfo(AuthCode:int, QQID:int, nocache:bool) -> str:
        return self.CQDLL.CQ_getStrangerInfo(c_int(AuthCode), c_int(QQID), c_bool(nocache))
    """
    日志
    priority 优先级，CQLOG 开头的常量
    category 类型
    content 内容
    """
    def addLog(AuthCode:int, priority:int, category:str, content:str) ->int:
        return self.CQDLL.CQ_addLog(c_int(AuthCode), c_int(priority), c_char_p(category.encode('gbk')), c_char_p(content.encode('gbk')))
    """
    取Cookies 慎用, 此接口需要严格授权
    """
    def getCookies(AuthCode:int) -> str:
        return self.CQDLL.CQ_getCookies(c_int(AuthCode))
    """
    取CsrfToken 慎用, 此接口需要严格授权
    """
    def getCsrfToken(AuthCode:int) -> int:
        return self.CQDLL.CQ_getCsrfToken(c_int(AuthCode))
    """
    取登录QQ
    """
    def getLoginQQ(AuthCode:int) -> int:
        return self.CQDLL.CQ_getLoginQQ(c_int(AuthCode))
    """
    取登录QQ昵称
    """
    def getLoginNick(AuthCode:int) -> str:
        return self.CQDLL.CQ_getLoginNick(c_int(AuthCode))
    """
    取应用目录，返回的路径末尾带"\"
    """
    def getAppDirectory(AuthCode:int) -> str:
        return self.CQDLL.CQ_getAppDirectory(c_int(AuthCode))
    """
    置致命错误提示
    errorinfo 错误信息
    """
    def setFatal(AuthCode:int, errorinfo:str) -> int:
        return self.CQDLL.CQ_setFatal(c_int(AuthCode),  c_char_p(errorinfo.encode('gbk')))
    """
    接收语音，接收消息中的语音(record),返回保存在 \data\record\ 目录下的文件名
    file 收到消息中的语音文件名(file)
    outformat 应用所需的语音文件格式，目前支持 mp3 amr wma m4a spx ogg wav flac
    """
    def getRecord(AuthCode:int, file:str, outformat:str) -> str:
        return self.CQDLL.CQ_getRecord(c_int(AuthCode), c_char_p(file.encode('gbk')), c_char_p(outformat.encode('gbk')))
