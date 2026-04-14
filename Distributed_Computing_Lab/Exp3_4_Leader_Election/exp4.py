from datetime import datetime, timedelta

class Node:
    def __init__(self, name, time_offset_seconds):
        self.name = name
        # Simulate different computer clocks by adding an offset to the real time
        self.clock = datetime.now() + timedelta(seconds=time_offset_seconds)

    def get_time(self):
        return self.clock

    def adjust_time(self, offset):
        self.clock += timedelta(seconds=offset)
        print(f"[{self.name}] Adjusted clock by {offset:>5.2f} seconds. \tNew time: {self.clock.strftime('%H:%M:%S')}")

def berkeley_algorithm(coordinator, nodes):
    print(f"--- Starting Berkeley Clock Synchronization Algorithm ---\n")
    
    # 1. Fetch current time from all nodes
    print("Step 1: Initial Times before Synchronization")
    times = [node.get_time() for node in nodes]
    for node in nodes:
        print(f"[{node.name}] Time: {node.get_time().strftime('%H:%M:%S')}")

    # 2. Coordinator calculates time differences relative to its own time
    coord_time = coordinator.get_time()
    differences = [(t - coord_time).total_seconds() for t in times]
    
    # 3. Calculate the average difference
    avg_diff = sum(differences) / len(nodes)
    print(f"\nStep 2: Coordinator calculates the average time difference: {avg_diff:.2f} seconds\n")

    # 4. Coordinator tells each node how much to adjust its clock
    print("Step 3: Adjusting clocks...")
    for i, node in enumerate(nodes):
        # The adjustment is: (Average Difference) - (Node's original difference from coordinator)
        adjustment = avg_diff - differences[i]
        node.adjust_time(adjustment)

    # 5. Final check
    print("\nStep 4: Final Synchronized Times")
    for node in nodes:
        print(f"[{node.name}] Time: {node.get_time().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    # Initialize a coordinator and some clients with inaccurate clocks
    # (Offsets are in seconds. E.g., Client 1 is 15 seconds ahead, Client 2 is 10 seconds behind)
    server = Node("Coordinator", 0)
    client1 = Node("Client 1 ", 15)  
    client2 = Node("Client 2 ", -10) 
    
    network_nodes = [server, client1, client2]
    
    # Run the simulation
    berkeley_algorithm(server, network_nodes)