import socket

PORT = 8083
IP = "10.108.33.9"
MAX_OPEN_REQUESTS = 5

# RMB is the China currency: Renminbi is the currency, Yuan is the unit



def process_client(clientsocket):
    #adress[0]=direcciión IP del cliente
    add=address[0]
    add=add.replace(".","")
    #add=int(add)
    import random
    numero=random.randint(0,9)
    suma=int(add[0:2])+int(add[2:5])+int(add[5:7])+int(add[7])
    resto= suma%10
    if resto==numero:
        send_message ="\nTe ha tocado. El numero era: "+ str(numero)
    else:
        send_message="\nNo te ha tocado, tu numero era: "+ str(resto) + "\nEl número premiado es: " + str(numero)
    # utf8 supports all lanaguages chars
    #send_message +=
    # Serializing the data to be transmitted
    send_bytes = str.encode(send_message)
    # We must write bytes, not a string
    clientsocket.send(send_bytes)
    print(clientsocket.recv(2048).decode("utf-8"))
    clientsocket.close()


# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()

        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
