import socket
import threading

def vpn_server(socks,addr,server_loacl_port,time_out):
    socks.settimeout(time_out)
    rm_host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    rm_host.connect(("127.0.0.1",server_loacl_port))
    rm_host.settimeout(time_out)
    '''
    维护两个子线程
    一个用来接受数据
    另外一个用来发送数据
    两个进程之间互不干扰
    '''
    te1 = threading.Thread(target=t1,args=(rm_host,socks))
    te1.start()
    te2 = threading.Thread(target=t2,args=(rm_host,socks))
    te2.start()

def t1(rm_host,socks):
    while True:
        try:
            data = socks.recv(8192)
            #rsa_data = rsa.decrypt(data,server_private_key) #改写
            #print("send data",data)
            rm_host.send(data)#解密
            if len(data)<1:
                rm_host.close()
                socks.close()
                return 0
        except:
            print("ERROR")
            break
    #print(recv_data)
    rm_host.close()
    socks.close()


def t2(rm_host,socks):
    while True:
        try:
            recv_data = rm_host.recv(2048)
            socks.send(recv_data)
            if len(recv_data)<1:
                rm_host.close()
                socks.close()
                return 0
        except:
            print("ERROR")
            break

    #print(recv_data)
    rm_host.close()
    socks.close()