import socket                                               #import socket library

client1=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)  # create socket connection
client1.connect(('127.0.0.3',8888))                         # connect to server ip
servermsg=client1.recv(1024)                                # receive the message from server
servermsg1=servermsg.decode("utf-8")                        # decode the message
print("client2={0}".format(servermsg1))                     # print message on console

while True:                                                 # contineous loo[ for chat
           client1msg=input(str("client1="))                
           client1.sendall(client1msg.encode("utf-8"))     # send the message
           print("message is send")                         
           servermsg=client1.recv(1024)        
           servermsg1=servermsg.decode("utf-8")            # receive the message
           print("client2={0}".format(servermsg1)) 
 

           
client1.close()

