import socket
import base64
import rsa
import threading

def vpn_server(socks,addr,ip,port,time_out):
    #socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    with open('public_ser.pem', "rb") as publickfile:
        p = publickfile.read()
        server_public_key = rsa.PublicKey.load_pkcs1(p)

    with open('private.pem', "rb") as privatefile:
        p = privatefile.read()
        local_private_key = rsa.PrivateKey.load_pkcs1(p)

    socks.settimeout(time_out)
    rm_host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    rm_host.connect((ip,port))
    rm_host.settimeout(time_out)
    te1 = threading.Thread(target=t1,args=(rm_host,socks,server_public_key))
    te1.start()
    te2 = threading.Thread(target=t2,args=(rm_host,socks,local_private_key))
    te2.start()


def t1(rm_host,socks,server_public_key):
    while True:
        try:
            data = socks.recv(8192)
            #rsa_data = rsa.encrypt(data, server_public_key)
            length = len(data)
            val_list = []
            for i in range(0, length, 245):
                tpl = data[i:i + 245]
                val = rsa.encrypt(tpl, server_public_key)
                val_list.append(val)
            rsa_data = b''.join(val_list)
            #print("send data",b_data)   #加密
            rm_host.send(rsa_data)
        except:
            print("ERROR")
            break
    rm_host.close()
    socks.close()

def t2(rm_host,socks,local_private_key):
    while True:
        try:
            recv_data = rm_host.recv(58048)
            #print("recive data",recv_data) 
            length = len(recv_data)
            val_list = []
            for i in range(0, length, 256):
                tpl = recv_data[i:i + 256]
                val = rsa.decrypt(tpl, local_private_key)
                val_list.append(val)
            rsa_recv_data = b''.join(val_list)
            #print("recive data",rsa_recv_data)
            socks.send(rsa_recv_data)#解密
        except:
            print("ERROR")
            break
        #print(recv_data)
    rm_host.close()
    socks.close()