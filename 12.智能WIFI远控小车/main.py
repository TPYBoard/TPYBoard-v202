import socket                 #导入socket通信库
import machine
from machine import Pin

g4 = Pin(4,Pin.OUT)
g5 = Pin(5,Pin.OUT)
g12 = Pin(12,Pin.OUT)
g13 = Pin(13,Pin.OUT)

def Go():
    g4.value(1)
    g5.value(0)
    g12.value(1)
    g13.value(0)
def Back():
    g4.value(0)
    g5.value(1)
    g12.value(0)
    g13.value(1)

def Left():
    g4.value(1)
    g5.value(0)
    g12.value(0)
    g13.value(0)
def Right():
    g4.value(0)
    g5.value(0)
    g12.value(1)
    g13.value(0)
def Stop():
    g4.value(0)
    g5.value(0)
    g12.value(0)
    g13.value(0)
#-----------------------HTTP Server-----------------------#
#ap模式下，默认ip地址为192.168.4.1
addr = ('192.168.4.1',80) #定义socket绑定的地址，ip地址为本地，端口为80
s = socket.socket()     #创建一个socket对象
s.bind(addr)            #绑定地址
s.listen(5)             #设置允许连接的客户端数量
print('listening on:', addr)
while True:
    cl, addr = s.accept() #接受客户端的连接请求，cl为此链接创建的一个新的scoket对象，addr客户端地址
    print('client connected from:', addr)
    cl_file = cl.makefile('rwb', 0) #返回与socket对象关联的文件对象。rwb:支持二进制模式的读写操作 0:默认值，不支持缓存
    req = b''
    while True:
        line = cl_file.readline() #读取发送过来的数据，直到\r\n换行结束
        if not line or line == b'\r\n':
            break
        req += line
    print("Request:")
    req=req.decode('utf-8').split('\r\n')
    #http header 解析
    req_data=req[0].lstrip().rstrip().replace(' ','').lower()
    print(req_data)
    if req_data.find('favicon.ico')>-1:
        cl.close()
        continue
    else:
        req_data=req_data.replace('get/?','').replace('http/1.1','')
        index = req_data.find('key=')
        value = req_data[index+4:index+6].lstrip().rstrip()
        print('key:',value)
        if value == 'go':
            Go()
        elif value == 'ba':
            Back()
        elif value == 'le':
            Left()
        elif value == 'ri':
            Right()
        else:
            Stop()
    with open("control.html", 'r') as f:
        for line in f:
            cl.send(line)
    #cl.send(response)   #返回html网页的数据
    cl.close()          #关闭socket