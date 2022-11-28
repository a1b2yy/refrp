import socket
import method_rsa
import threading
def main():
    recv_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("local bind port")
    local_bind_port = int(input())
    print("local server port")
    local_server_port = int(input())
    print("Please Input the time tcp time out time")
    time_out = int(input())
    recv_sock.bind(("",local_bind_port))
    recv_sock.listen(5)
    addr_list = list()
    socks_list = list()
    while True:
        try:
            new_sock ,addr = recv_sock.accept()
            sub_thread = threading.Thread(target=method_rsa.vpn_server, args=(new_sock ,addr,local_server_port,time_out))
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