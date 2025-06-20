import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 65432))
server_socket.listen(1)  # Listen for 1 client
print("Server is listening on localhost:65432")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'exit':
        print("Connection closed.")
        break
    print(f"Client: {data}")
    response = input("You: ")
    conn.sendall(response.encode())
    if response.lower() == 'exit':
        break

conn.close()
server_socket.close()


