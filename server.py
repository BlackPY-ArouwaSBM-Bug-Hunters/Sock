import socket
import threading

ip=socket.gethostbyname(socket.gethostname())
port=1234
adress=(ip,port)
size=1024
format='utf-8'
disconnect='d'



def hangle_client(client_socket,user):
    print(f'User {user}')

    connect=True
    while connect:
        msg=client_socket.recv(size).decode(format)
        if msg==disconnect:
            connect=False
        print(f' User message {user}')

        msg=f'Received message {msg}'
        client_socket.send(msg.encode(format))
    client_socket.close()
def main():
    print('server is starting...')
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((adress))
    server.listen(5)
    print(f'Server listening mode : {ip}:{port}')

    while True:
        user,addr=server.accept()
        thed=threading.Thread(target=hangle_client,args=(user,addr))
        thed.start()
        print(f'User Count {threading.activeCount()-1}')
if __name__=="__main__":
    main()