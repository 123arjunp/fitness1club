import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 65432))
    print("Connected to the server.")

    # Send a list of numbers to the server
    numbers = [10, 20, 30, 40, 50]  # Example list of integers
    message = ','.join(map(str, numbers))  # Convert the list to a comma-separated string
    client_socket.send(message.encode())
    print(f"Sent numbers: {numbers}")

    # Receive the response (sum) from the server
    response = client_socket.recv(1024).decode()
    print(f"Received sum from server: {response}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
