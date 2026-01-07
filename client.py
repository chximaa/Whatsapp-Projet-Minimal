import socket

# 1️⃣ Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2️⃣ Connect to server
client_socket.connect(("127.0.0.1", 5000))
print("Connected to server.")

# 3️⃣ Communication loop
while True:
    message = input("Client: ")
    client_socket.send(message.encode())

    if message.lower() == "quit" or message.lower() == "exit":
        print("Disconnected from server.")
        break

    reply = client_socket.recv(1024).decode()
    print("Server:", reply)

# 4️⃣ Close socket
client_socket.close()
