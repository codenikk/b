import socket 

def send_file(file_path): 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5001))

    # Step 1: Send hello to server 
    client_socket.send("Hello from Client!".encode())

    # Step 1: Receive hello from server 
    server_hello = client_socket.recv(1024).decode() 
    print(f"Server says: {server_hello}")

    # Step 2: Send file name 
    filename = file_path.split('/')[-1]
    client_socket.send(filename.encode())

    # Step 2: Send file data 
    with open(file_path, 'rb') as f:
        while True:
            bytes_read = f.read(1024)
            if not bytes_read:
                break
            client_socket.send(bytes_read)

    print("File sent successfully.")
    client_socket.close()

# Run the client 

send_file("pk.txt")


# Server

import socket

def receive_file():

    # Create TCP socket

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('127.0.0.1', 5001))

    server_socket.listen(1)

    print("Server listening on port 5001...")

    # Accept client connection

    conn, addr = server_socket.accept()

    print(f"Connection from {addr}")

    # Step 1: Receive hello from client

    client_hello = conn.recv(1024).decode()

    print(f"Client says: {client_hello}")

    # Step 1: Send hello to client

    conn.send("Hello from Server!".encode())

    # Step 2: Receive file name

    filename = conn.recv(1024).decode()

    print(f"Receiving file: {filename}")

    # Step 2: Receive file data and save it

    with open("received_" + filename, 'wb') as f:

        while True:

            data = conn.recv(1024)

            if not data:

                break

            f.write(data)

    print("File received successfully.")

    conn.close()

    server_socket.close()

# Run the server

receive_file()
