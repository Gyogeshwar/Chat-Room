import socket


client1=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
client1.connect(('192.168.42.23',8888))
servermsg=client1.recv(1024)
servermsg1=servermsg.decode("utf-8")
print("client2={0}".format(servermsg1))

while True:
           client1msg=input(str("client1="))
           client1.sendall(client1msg.encode("utf-8"))
           print("message is send")
           servermsg=client1.recv(1024)
           servermsg1=servermsg.decode("utf-8")
           print("client2={0}".format(servermsg1))
 

           
client1.close()

