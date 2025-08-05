import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(f"\nServer: {message}")
        except:
            break

def send_messages(sock):
    while True:
        try:
            message = input("You: ")
            sock.send(message.encode())
        except:
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
print("[+] Connected to server.")

# Start threads for sending and receiving
threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
send_messages(client_socket)

client_socket.close()
print("[+] Disconnected from server.")