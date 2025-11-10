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