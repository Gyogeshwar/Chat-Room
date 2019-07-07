import socket                                              # import the socket library
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)  # create socket connection
ip='127.0.0.3'                                             # define server ip
port=8888                                                  # define port address
server.bind((ip,port))                                     # bind the server and port address
server.listen(5)                                           # connection limit for this defined ip is 5
print("socket server lisening on {0}and {1}".format(ip,port)) # display the message for ip and port
newsocket1,cliadd=server.accept()                             # accept requect form 1st client
print("get a new connection from {}".format(str(cliadd)))     # disply the connection message
newsocket2,cliadd1=server.accept()                            # accept requect form 2nd client
print("get a new connection from {}".format(str(cliadd1)))    # disply the connection message
msg="welcome to chatroom"                                     # define message
newsocket1.sendall(msg.encode("utf-8"))                       # send the message for client 1
newsocket2.sendall(msg.encode("utf-8"))                       # send the message for client 2

while True:                                                   # contineous loop for chat
          clientmsg=newsocket1.recv(1024)
          clientmsg1=clientmsg.decode("utf-8")                # receive the message from client 1 and display
          print("client1 message={0}".format(clientmsg1))
          newsocket2.sendall(clientmsg1.encode("utf-8"))
          print("send")
          clientmsg=newsocket2.recv(1024)
          clientmsg1=clientmsg.decode("utf-8")
          print("client2 message={0}".format(clientmsg1))    # send the message for client2
          newsocket1.sendall(clientmsg1.encode("utf-8")) 

server.close()
