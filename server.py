import socket

# 1️⃣ Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2️⃣ Bind IP and port
server_socket.bind(("127.0.0.1", 5000))

# 3️⃣ Listen for connections
server_socket.listen(1)
print("Server is waiting for a connection...")

# 4️⃣ Accept connection
client_socket, client_address = server_socket.accept()
print("Client connected from:", client_address)

# 5️⃣ Communication loop
while True:
    message = client_socket.recv(1024).decode()
    
    if message.lower() == "quit" or message.lower() == "exit":
        print("Client disconnected.")
        break

    print("Client:", message)
    
    reply = input("Server: ")
    client_socket.send(reply.encode())

# 6️⃣ Close sockets
client_socket.close()
server_socket.close()
print("Server closed.")
