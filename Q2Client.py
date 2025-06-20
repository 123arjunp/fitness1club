import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 65432))

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