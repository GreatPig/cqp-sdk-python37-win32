## 作者: alphafase
### gayhub：https://github.com/AlphaFase/cqp-sdk-python37-win32.git

# 下载的童鞋，麻烦右上角，fork或者star, 有问题请提交

> 插件跟随软件启动，禁用插件并不会停止python，启用插件只是reload python，热更新  
> 那个dll名字，自己把下划线去掉

更新:  
> com.example.democ.dll 版本
V2 (GIL):
>      在V1的基础上修复了酷Q退出 释放资源，启用插件和禁用插件释放临时解释器
V1 (GIL):  
>      带GIL锁，线程安全，但是部分包，可能会死锁，目前已知：import pywin32 和 os.chdir 会导致死锁

### 1. com.example.democ.dll 和 com.example.democ.json 和com.example.democ 目录  
>    改成你自己的appid文件名，复制到酷Q的app目录  
 


### 2. 安装python37，复制到酷Q的app目录，如果位置正确，python.exe文件路径应该是这样的    
>    ~酷Q目录/app/python37/python.exe     


### 3. 酷Q的CQA.exe的旁边放一个python37.dll  


### 4. main.py名字不可以改，不能挪位置， cqsdk.py倒是无所谓可有可无，完全可以写在main.py里面    
  

 最后说明，python的32位的，却啥库就pip安装，不阉割。但是某些库是无法加载的，目录所知pywin32无法使用  
>  python版本号： 
>  Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32   

> 日期：2018-7-19 的可以用，其他就不知道了  
> python下载地址： https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe  