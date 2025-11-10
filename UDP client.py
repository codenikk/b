import socket
import os

def start_client():
    server_ip = input("Enter server IP address(127.0.0.1): ")
    filename = input("Enter the file name to send: ")

    # Step 1: Create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (server_ip, 5001)

    # Step 2: Send file name first
    client_socket.sendto(filename.encode(), server_address)

    # Step 3: Read file in binary mode and send in chunks
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            while True:
                bytes_read = f.read(4096)
                if not bytes_read:
                    break
                client_socket.sendto(bytes_read, server_address)
        # Send end of file marker
        client_socket.sendto(b'EOF', server_address)
        print("File sent successfully.")
    else:
        print("File not found!")

    # Step 4: Receive confirmation from server
    msg, _ = client_socket.recvfrom(1024)
    print("Server response:", msg.decode())

    client_socket.close()


if __name__ == "__main__":
    start_client()

