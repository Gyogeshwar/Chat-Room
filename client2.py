import socket

client2=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
client2.connect(('127.0.0.3',8888))
servermsg=client2.recv(1024)
servermsg1=servermsg.decode("utf-8")
print("client1={0}".format(servermsg1))

while True:
          servermsg=client2.recv(1024)
          servermsg1=servermsg.decode("utf-8")
          print("client1={0}".format(servermsg1))

          client2msg=input(str("client2="))
          client2.sendall(client2msg.encode("utf-8"))
          print("message is send")

          
client.close()


