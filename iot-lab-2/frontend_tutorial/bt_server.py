import bluetooth

hostMACAddress = "10.0.0.10" # The address of Raspberry PI Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 0
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
print("listening on port ", port)
try:
    client, clientInfo = s.accept()
    while 1:   
        print("server recv from: ", clientInfo)
        data = client.recv(size)
        if data:
            print(data)
            if data == "F":
                # move car forward
            elif data == "R":
                # move car right
            elif data == "L":
                # move car left
            elif data == "B":
                # move car backwards
            elif data == "S":
                # stop car
            elif data == "Stats":
                # get car stats
                client.send(data) # Echo back to client
except: 
    print("Closing socket")
    client.close()
    s.close()
