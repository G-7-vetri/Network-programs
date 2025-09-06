import socket
import threading

# List to keep track of connected clients
clients = []

# Broadcast message to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

# Handle individual client connection
def handle_client(client_socket, address):
    print(f"[+] New connection from {address}")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"[{address}] {message.decode()}")
            broadcast(message, client_socket)
        except:
            break
    print(f"[-] Disconnected {address}")
    clients.remove(client_socket)
    client_socket.close()

# Start the server
def start_server(host='127.0.0.1', port=5555):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[*] Server started on {host}:{port}")
    
    while True:
        client_socket, address = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    start_server()
