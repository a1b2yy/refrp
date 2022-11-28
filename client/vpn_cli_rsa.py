import socket
import methodl_local_rsa
import threading
def main():
    recv_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("local bind port")
    bind_port = int(input())
    addrss = bind_port
    recv_sock.bind(("",addrss))
    recv_sock.listen(5)
    print("remote host ip")
    ip = input()
    print("remote port")
    port = int(input())
    print("Please Input the time tcp time out time")
    time_out = int(input())
    addr_list = list()
    socks_list = list()
    while True:
        try:
            new_sock ,addr = recv_sock.accept()
            sub_thread = threading.Thread(target=methodl_local_rsa.vpn_server, args=(new_sock ,addr,ip,port,time_out))
            sub_thread.start()
            addr_list.append(addr)
            socks_list.append(new_sock)
        except:
            print("Error")
if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("QUIT")