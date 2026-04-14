import threading
import time

class Node:
    def __init__(self, node_id, next_node=None):
        self.node_id = node_id
        self.next_node = next_node
        self.has_token = False

    def set_next_node(self, next_node):
        self.next_node = next_node

    def process(self):
        while True:
            if self.has_token:
                print(f"Node {self.node_id} is using the token.")
                time.sleep(2) # Simulating work
                print(f"Node {self.node_id} passing the token to Node {self.next_node.node_id}.")
                self.has_token = False
                self.next_node.receive_token()
            time.sleep(1)

    def receive_token(self):
        self.has_token = True

if __name__ == "__main__":
    # Initialize nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # Form a ring
    node1.set_next_node(node2)
    node2.set_next_node(node3)
    node3.set_next_node(node4)
    node4.set_next_node(node1)

    # Give token to Node 1 initially
    node1.has_token = True

    # Start threads
    threads = [threading.Thread(target=node.process) for node in [node1, node2, node3, node4]]
    for thread in threads:
        # thread.daemon = True # Optional: Allows program to exit on Ctrl+C smoothly
        thread.start()