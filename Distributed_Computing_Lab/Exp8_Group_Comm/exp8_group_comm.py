import threading
import queue
import time

# Simulating the message queue for communication
message_queue = queue.Queue()

# Define client groups for multicast
multicast_group = {"client1", "client3"} # Example group

# Function for server to send messages
def server():
    time.sleep(1) # Simulating delay for setup
    print("\n Server Started...\n")
    
    # Unicast message to client1
    message_queue.put(("client1", "Unicast: Hello, Client1!"))
    
    # Multicast message to group
    for client in multicast_group:
        message_queue.put((client, "Multicast: Hello, Group Clients!"))
        
    # Broadcast message to all clients
    for client in ["client1", "client2", "client3"]:
        message_queue.put((client, "Broadcast: Hello, All Clients!"))
        
    print("\n Messages Sent by Server!\n")

def client(name):
    print(f"{name} started and waiting for messages...")
    while True:
        try:
            recipient, message = message_queue.get(timeout=5) # Wait for messages
            if recipient == name or recipient == "all":
                print(f"{name} received: {message}")
        except queue.Empty:
            break

if __name__ == "__main__":
    # Start server and clients using threads
    server_thread = threading.Thread(target=server)
    client1_thread = threading.Thread(target=client, args=("client1",))
    client2_thread = threading.Thread(target=client, args=("client2",))
    client3_thread = threading.Thread(target=client, args=("client3",))

    # Start all threads
    server_thread.start()
    client1_thread.start()
    client2_thread.start()
    client3_thread.start()

    # Wait for all to finish
    server_thread.join()
    client1_thread.join()
    client2_thread.join()
    client3_thread.join()

    print("\n Grouped Communication Simulation Complete!")