import time, socket, sys, random

print("Receiver.\n")
print("Initialising...")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
host = input("Server address: ")
port = 1234
time.sleep(1)
s.connect((host, port))
print("Connected.")

while True:
    m = s.recv(1024)
    m = m.decode()
    if m != "End":
        k = s.recv(1024)
        k = k.decode()
        k = int(k)
        i = 0
        a = ""
        b = ""
        f = random.randint(0, 1)
        message = ""
        while i!= k:
            f = random.randint(0, 1)
            if (f==0):
                b = "ACK Lost!"
                message = s.recv(1024)
                message = message.decode()
                s.send(b.encode())
            elif (f==1):
                b = "ACK" + str(i)
                message = s.recv(1024)
                message = message.decode()
                s.send(b.encode())
                a = a + message
                i = i+1
        print("Received message: ", m)
    else:
        print("\nConnection terminated.")
