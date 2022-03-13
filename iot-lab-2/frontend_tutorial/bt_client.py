import bluetooth

host = "10.0.0.10" # The address of Raspberry PI Bluetooth adapter on the server.
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))
while 1:
    text = input("Bluetooth communication\nType...\nF to move car forward\nR to move car right\nL to move car left\nB to move car backwards\nS to stop car\nStats to get car statistics\nQ to quit\nEnter your message: ") # Note change to the old (Python 2) raw_input
    if text == "Q":
        break
    sock.send(text)
    data = sock.recv(1024)
    print("from server: ", data)

sock.close()
