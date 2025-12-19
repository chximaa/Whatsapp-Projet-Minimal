import socket
import tkinter as tk
from threading import Thread

# ---- TCP socket ----
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.1.2", 5000))  # Use your laptop IP if needed

# ---- GUI setup ----
window = tk.Tk()
window.title("Mini WhatsApp")
window.geometry("400x400")

# ---- Chat display ----
chat_box = tk.Text(window, height=20, width=50)
chat_box.pack(pady=10)
chat_box.config(state=tk.DISABLED)

# ---- Message input ----
message_entry = tk.Entry(window, width=40)
message_entry.pack(side=tk.LEFT, padx=10, pady=10)

# ---- Send button ----
def send_message():
    msg = message_entry.get()
    if not msg:
        return
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Me: " + msg + "\n")
    chat_box.config(state=tk.DISABLED)
    client_socket.send(msg.encode())
    message_entry.delete(0, tk.END)
    if msg.lower() == "quit":
        client_socket.close()
        window.destroy()

send_btn = tk.Button(window, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT)

# ---- Receive messages in background ----
def receive_messages():
    while True:
        try:
            reply = client_socket.recv(1024).decode()
            if not reply:
                break
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, "Server: " + reply + "\n")
            chat_box.config(state=tk.DISABLED)
        except:
            break

# Run receiving in a separate thread
receive_thread = Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

# ---- Start GUI ----
window.mainloop()
