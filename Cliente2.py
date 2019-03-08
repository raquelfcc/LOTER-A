


import socket

IP = "10.108.33.9"
PORT = 8083

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.connect((IP, PORT))
except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

print(s.recv(2048).decode("utf-8"))
nuestra_IP=(s.getsockname())[0]
send_message = "\nEl cliente "+str(nuestra_IP)+" ha participado\n"
    # utf8 supports all lanaguages chars
    # Serializing the data to be transmitted
send_bytes = str.encode(send_message)
s.send(send_bytes)
s.close()
