import socket
import threading

# Server configuration
host = '127.0.0.1'  # localhost
port = 5000         # Must match server's port

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((host, port))
print(f"[CLIENT] Connected to server at {host}:{port}")

# Function to receive messages
def receive():
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if data:
                print(f"[Server]: {data}")
            else:
                break
        except:
            break

# Function to send messages
def send():
    while True:
        message = input()
        client_socket.send(message.encode())

# Create threads
receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

receive_thread.start()
send_thread.start()
