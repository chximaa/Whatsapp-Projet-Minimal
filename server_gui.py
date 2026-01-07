import socket
import tkinter as tk
from threading import Thread

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5000))  # Listen on all interfaces
server_socket.listen(1)
print("Waiting for client connection...")

client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)

window = tk.Tk()
window.title("WhatsApp Minimal Server")
window.geometry("400x400")

chat_box = tk.Text(window, height=20, width=50)
chat_box.pack(pady=10)
chat_box.config(state=tk.DISABLED)

message_entry = tk.Entry(window, width=40)
message_entry.pack(side=tk.LEFT, padx=10, pady=10)

def send_message(event=None):
    msg = message_entry.get()
    if not msg:
        return
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Server: " + msg + "\n")
    chat_box.config(state=tk.DISABLED)
    client_socket.send(msg.encode())
    message_entry.delete(0, tk.END)
    if msg.lower() == "quit":
        client_socket.close()
        server_socket.close()
        window.destroy()

send_btn = tk.Button(window, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT)
message_entry.bind("<Return>", lambda e: send_message())

def receive_messages():
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, "Client: " + msg + "\n")
            chat_box.config(state=tk.DISABLED)
        except:
            break

receive_thread = Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

window.mainloop()
