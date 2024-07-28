# client.py

import socket
import time
import random
import json

def start_client(host='10.141.27.75', port=8222, client_id=1):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        for _ in range(10):
            # Create a JSON object
            data = {
                "client_id": client_id,
                "random_number": random.randint(1, 1000)
            }
            json_data = json.dumps(data)
            print(f"[Client {client_id}] Sending to server: {json_data}")
            client_socket.send(json_data.encode())

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
