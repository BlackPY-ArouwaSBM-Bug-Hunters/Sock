import socket

ip=socket.gethostbyname(socket.gethostname())
port=1234
adress=(ip,port)
size=1024
format='utf-8'
disconnect='d'

def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.socket.connect(adress)
    print(f'Client connect to server {ip}:{port}')

    connect=True
    while connect:
        msg=input('Enter your input : ')
        client.send(msg.encode(format))

        if msg==disconnect:
            connect=False
        else:
            msg=client.recv(size).decode(format)
            print(f' Server Is : {msg}')
if __name__=="__main__":
    main()




            