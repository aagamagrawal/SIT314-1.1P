# server.py

import socket
import sys
import threading

def handle_client(conn, address):
    print(f"Connected to client at {address}")
    while True:
        try:
            # Receive data from the client
            data = conn.recv(2048)
            if not data:
                break
            message = data.decode()
            print(f"Message received from {address}: {message}")

            # Send acknowledgment back to the client
            conn.sendall("ack".encode())

            # Handle disconnect message
            if message == "disconnect":
                print(f"Client at {address} disconnected.")
                break
        except ConnectionResetError:
            print(f"Connection with {address} was lost.")
            break

    # Close the connection
    conn.close()
    print(f"Connection closed for client at {address}")

def start_server(host='10.141.27.75', port=8222):  # Use your IP address here
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server listening for clients...")

    try:
        while True:
            # Accept a client connection
            conn, address = server_socket.accept()
            # Handle the client connection in a new thread
            client_thread = threading.Thread(target=handle_client, args=(conn, address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
