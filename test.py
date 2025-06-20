import socket



def start_server():

    # Create a socket object

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    # Bind the socket to a specific IP and port

    server_socket.bind(('localhost', 65432))

    print("Server is running and waiting for a connection...")



    # Listen for incoming connections

    server_socket.listen(1)

    conn, addr = server_socket.accept()

    print(f"Connected to {addr}")



    while True:

        # Receive data from the client

        data = conn.recv(1024).decode()

        if not data:

            break  # Exit if the client disconnects



        # Convert the received data into a list of integers

        numbers = list(map(int, data.split(',')))



        # Calculate the sum of the numbers

        result = sum(numbers)



        # Send the result back to the client

        conn.send(str(result).encode())



    # Close the connection

    conn.close()

    server_socket.close()

  

if __name__ == "__main__":

    start_server()