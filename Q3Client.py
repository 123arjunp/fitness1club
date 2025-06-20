import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '192.168.X.X'  # Replace with server's local IP
client_socket.connect((server_ip, 65432))

print("Connected to the server. Type 'exit' to end the chat.")
while True:
    message = input("You: ")
    client_socket.sendall(message.encode())
    if message.lower() == 'exit':
        break
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")
    if response.lower() == 'exit':
        break

client_socket.close()
