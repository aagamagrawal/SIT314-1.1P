# client.py

import socket
import time
import random

def start_client(host='10.141.27.75', port=8222, client_id=1):  # Use server's IP address here
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        for _ in range(10):
            # Generate a random number to send
            data = str(random.randint(1, 100))
            print(f"[Client {client_id}] Sending to server: {data}")
            client_socket.send(data.encode())

            # Randomize the interval between 0.1 to 1.0 seconds
            time.sleep(random.uniform(0.1, 1.0))

        # Send disconnect message
        msg = "disconnect"
        print(f"[Client {client_id}] Sending disconnect message to server.")
        client_socket.send(msg.encode())

    finally:
        # Close the socket
        client_socket.close()
        print(f"[Client {client_id}] Connection closed.")

if __name__ == "__main__":
    start_client(client_id=random.randint(1, 1000))
