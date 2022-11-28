import socket
import base64
import rsa

def vpn_server(socks,addr,server_loacl_port,time_out):

    with open('private_ser.pem', "rb") as publickfile:
        p = publickfile.read()
        server_private_key = rsa.PrivateKey.load_pkcs1(p)

    with open('public.pem', "rb") as privatefile:
        p = privatefile.read()
        local_public_key = rsa.PublicKey.load_pkcs1(p)

    #socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socks.settimeout(time_out)
    rm_host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    rm_host.connect(("127.0.0.1",server_loacl_port))
    rm_host.settimeout(time_out)

    while True:
        try:
            data = socks.recv(8192)
            #rsa_data = rsa.decrypt(data,server_private_key) #改写
            length = len(data)
            val_list = []
            for i in range(0, length, 256):
                tpl = data[i:i + 256]
                val = rsa.decrypt(tpl, server_private_key)
                val_list.append(val)
            rsa_data = b''.join(val_list)
            #print("send data",rsa_data)
            rm_host.send(rsa_data)#解密
            if len(data)<1:
                rm_host.close()
                socks.close()
                return 0
        except:
            print("ERROR")
            break

        try:
            recv_data = rm_host.recv(22048)
            length = len(recv_data)
            val_list = []
            for i in range(0, length, 245):
                tpl = recv_data[i:i + 245]
                val = rsa.encrypt(tpl, local_public_key)
                val_list.append(val)
            rsa_recv_data = b''.join(val_list)
            print(rsa_recv_data)
            socks.send(rsa_recv_data)
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