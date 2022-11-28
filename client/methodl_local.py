import socket
import threading

def vpn_server(socks,addr,ip,port,time_out):
    socks.settimeout(time_out)
    rm_host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    rm_host.connect((ip,port))
    rm_host.settimeout(time_out)

    te1 = threading.Thread(target=t1,args=(rm_host,socks))
    te1.start()
    te2 = threading.Thread(target=t2,args=(rm_host,socks))
    te2.start()


def t1(rm_host,socks):
    while True:
        try:
            data = socks.recv(8192)
            rm_host.send(data)
            if len(data)<1:
                print("fuck you fuck you loop")
                #rm_host.close()
                #socks.close()
                return 0
        except:
            print("ERRORd")
            #rm_host.close()
            #socks.close()
            break
        #print(recv_data)
        #rm_host.close()
        #socks.close()


def t2(rm_host,socks):
    while True:
        try:
            recv_data = rm_host.recv(8048)
            socks.send(recv_data)
            if len(recv_data)<1:
                print("fuck you fuck you loop")
                #rm_host.close()
                #socks.close()
                return 0
        except:
            print("ERRORs")
            #rm_host.close()
            #socks.close()
            return 0
        #print(recv_data)
        #rm_host.close()
        #socks.close()