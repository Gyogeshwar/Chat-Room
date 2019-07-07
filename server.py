import socket
m=2
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
name=socket.gethostname()
ip='127.0.0.3'
port=8888
server.bind((ip,port))
server.listen(5)
print("socket server lisening on {0}and {1}".format(ip,port))
newsocket1,cliadd=server.accept()
print("get a new connection from {}".format(str(cliadd)))
newsocket2,cliadd1=server.accept()
print("get a new connection from {}".format(str(cliadd1)))
msg="welcome to chatroom"
newsocket1.sendall(msg.encode("utf-8"))
newsocket2.sendall(msg.encode("utf-8"))

while True:
          clientmsg=newsocket1.recv(1024)
          clientmsg1=clientmsg.decode("utf-8")
          print("client1 message={0}".format(clientmsg1))
          newsocket2.sendall(clientmsg1.encode("utf-8"))
          print("send")
          clientmsg=newsocket2.recv(1024)
          clientmsg1=clientmsg.decode("utf-8")
          print("client2 message={0}".format(clientmsg1))
          newsocket1.sendall(clientmsg1.encode("utf-8")) 

server.close()
