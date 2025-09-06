import socket
import threading

# Receive messages from the server
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if message:
                print(message)
        except:
            print("[!] Connection closed by server.")
            sock.close()
            break

# Send messages to the server
def send_messages(sock):
    while True:
        try:
            message = input()
            sock.send(message.encode())
        except:
            print("[!] Disconnected from server.")
            sock.close()
            break

def start_client(host='127.0.0.1', port=5555):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except:
        print(f"[!] Unable to connect to {host}:{port}")
        return

    print("[*] Connected to the server. Start chatting!")

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client,))
    
    receive_thread.start()
    send_thread.start()

if __name__ == "__main__":
    start_client()
