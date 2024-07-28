# multi_client_launcher.py

import subprocess

def launch_clients(num_clients=5):
    processes = []
    for i in range(num_clients):
        process = subprocess.Popen(['python3', 'client.py'])
        processes.append(process)
        print(f"Launched client {i + 1}")

    for process in processes:
        process.wait()

if __name__ == "__main__":
    launch_clients(num_clients=10)  # Adjust the number of clients as needed
