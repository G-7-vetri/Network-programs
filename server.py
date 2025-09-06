import socket
import threading

# Server configuration
host = '127.0.0.1'  # localhost
port = 5000         # Non-privileged ports are > 1023

# Create a socket (SOCK_STREAM means TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print(f"[SERVER] Listening on {host}:{port}...")

# Accept connection
conn, addr = server_socket.accept()
print(f"[SERVER] Connected by {addr}")

# Function to receive messages
def receive():
    while True:
        try:
            data = conn.recv(1024).decode()
            if data:
                print(f"[Client]: {data}")
            else:
                break
        except:
            break

# Function to send messages
def send():
    while True:
        message = input()
        conn.send(message.encode())

# Create threads for sending and receiving
receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

receive_thread.start()
send_thread.start()
