import socket
import threading

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 65432))
server_socket.listen(5)  # Support up to 5 clients
print("Server is listening on localhost:65432")

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print(f"Connection closed by {addr}")
            break
        print(f"Client {addr}: {data}")
        response = input("You: ")
        conn.sendall(response.encode())
        if response.lower() == 'exit':
            break
    conn.close()

while True:
    conn, addr = server_socket.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
