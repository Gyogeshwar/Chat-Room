import socket
from tkinter import *

client1msg=0
string=0
i=20
j=20

def send():
    global i
    global j
    i=i+10
    j=i-j
    global e1
    global client1
    string = e1.get() 
    print (string)
    c1.create_text(j,i,text=string)
    client1.sendall(string.encode("utf-8"))


def receive():
              servermsg=client1.recv(1024)
              servermsg1=servermsg.decode("utf-8")


window=Tk()
window.geometry('350x350')
window.title("client1")
client1=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
client1.connect(('127.0.0.3',8888))
print ('connected')
servermsg=client1.recv(1024)
servermsg1=servermsg.decode("utf-8")
print(servermsg1)


while True:
            
            e1=Entry(window)
            e1.pack()
            b1=Button(window, text="send", bg="yellow",fg="red",command=send)    
            b1.pack(side='top')
            c1=Canvas(window,height='300',width='400',bg='white')
            c1.pack()
            receive();
            tkinter.mainloop()
            window.pack()


tkinter.mainloop()  
client1.close()


