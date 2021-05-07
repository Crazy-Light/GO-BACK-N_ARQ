import time, socket, sys

def decimaltobin(n):
    return n.replace("0b", "")

def binarycode(s):
    byte_array = bytearray(s, "utf8")
    byte_list = []
    for byte in byte_array:
        binary_rep = bin(byte)
        byte_list.append(decimaltobin(binary_rep))
    a = ""
    for i in byte_list:
        a = a + i
    return a

print("Sender.\n")
print("Initialising...\n")
time.sleep(1)
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
s.listen(1)
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

while True:
    message = input("Message ('End' to exit): ")
    conn.send(message.encode())
    if message == "End":
        message = "Connection terminated."
        conn.send(message.encode())
        print(message, "\n")
        break
    else:
        message = binarycode(message)
        f = str(len(message))
        print(f)
        conn.send(f.encode())
        i = 0
        j = 0
        j = int(input("Window size: "))
        b = ""
        j = j-1
        f = int(f)
        k = j
        while i != f:
            while (i != (f-j)):
                conn.send(message[i].encode())
                b = conn.recv(1024)
                b = b.decode()
                print(b)
                if (b != "ACK Lost!"):
                    time.sleep(1)
                    print("Acknowledgement received. Sliding window is in the range " + str(i + 1) + " to " + str(k + 1) + ". Sending the next packet.")
                    i = i+1
                    k = k+1
                    time.sleep(1)
                else:
                    time.sleep(1)
                    print("Acknowledgement lost. Sliding window remains in the range " + (str(i+1)) + " to " + str(k+1) + ". Resending the packet.")
                    time.sleep(1)
            while (i != f):
                conn.send(message[i].encode())
                b = conn.recv(1024)
                b = b.decode()
                print(b)
                if (b != "ACK Lost!"):
                    time.sleep(1)
                    print("Acknowledgement received. Sliding window is in the range " + str(i+1) + " to " + str(k) + ". Sending the next packet.")
                    i = i+1
                    time.sleep(1)
                else:
                    time.sleep(1)
                    print("Acknowledgement lost. Sliding window remains in the range " + str(i+1) + " to " + str(k) + ". Resending the packet.")
                    time.sleep(1)