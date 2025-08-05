import socket
import threading

def receive_messages(conn):
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"\nClient: {message}")
        except:
            break

def send_messages(conn):
    while True:
        try:
            message = input("You: ")
            conn.send(message.encode())
        except:
            break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("[+] Server listening on port 12345...")

conn, addr = server_socket.accept()
print(f"[+] Connected to client at {addr}")

# Start threads for sending and receiving
threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()
send_messages(conn)

conn.close()
server_socket.close()
print("[+] Server closed connection.")