import socket                 # importing socket library.  

client2=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)    # creation of ip address for 2nd client.
client2.connect(('127.0.0.3',8888))                           # connection request for server bt client2. 
servermsg=client2.recv(1024)                                  # enable reception for client2 with 1024 string length.
servermsg1=servermsg.decode("utf-8")                          # decode the message using utf-8 algorithm.
print("client1={0}".format(servermsg1))                       # print the message on console.

while True:                                                   # contineous loop for reception and sending the message.
          servermsg=client2.recv(1024)                     
          servermsg1=servermsg.decode("utf-8")                #receive,decode and display the message.
          print("client1={0}".format(servermsg1))

          client2msg=input(str("client2="))
          client2.sendall(client2msg.encode("utf-8"))         #take the message from console encode and send it. 
          print("message is send")

          
client.close()


