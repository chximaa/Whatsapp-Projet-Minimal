# Mini WhatsApp Python

This project is a simplified version of WhatsApp, implemented in Python using TCP sockets<br>
and a graphical user interface (GUI) built with Tkinter. It allows a client and server to<br>
exchange messages in real-time over a local network.

## Features

- **TCP Socket Communication**: Reliable message exchange between client and server.
- **Server GUI**: View incoming messages and reply from a Tkinter window.
- **Client GUI**: Send messages through a WhatsApp-like interface.
- **Message Timestamps**: Each message is displayed with the time it was sent.
- **Quit Functionality**: Typing "QUIT" closes the connection gracefully.
- **Customizable GUI**: Colors, fonts, and window size can be modified.

## Files

- `server_gui.py` – Server application with GUI.
- `client_gui.py` – Client application with GUI.
- (Optional) `.gitignore` – To ignore cache and compiled files.

## How to Run

1.Run the server first:
bash
```python server_gui.py```

2.Run the client:
```python client_gui.py```

3.Chat between client and server in the GUI windows.

4.Type QUIT to close the connection.


