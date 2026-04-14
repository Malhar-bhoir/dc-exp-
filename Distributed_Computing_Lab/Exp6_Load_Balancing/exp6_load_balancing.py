# Threshold 1 and Threshold 2 Load Balancing Algorithm

# List of servers (each server starts with 0 load)
servers = [0, 0, 0, 0]

threshold1 = 5 # First threshold: Normal threshold for busy state
threshold2 = 8 # Second threshold: Critical threshold for overload state

def assign_request_to_server(request):
    for i in range(len(servers)):
        if servers[i] < threshold1:
            # If the server's load is below threshold1, assign the request
            servers[i] += 1
            print(f"Request assigned to Server {i}. Current load: {servers[i]} (Below Threshold1)")
            return
            
        elif servers[i] >= threshold1 and servers[i] < threshold2:
            # If the server's load is between threshold1 and threshold2, it's busy, but can still accept the request
            servers[i] += 1
            print(f"Server {i} is busy but accepting request. Current load: {servers[i]} (Between Threshold1 and Threshold2)")
            return
            
        elif servers[i] >= threshold2:
            # If the server's load exceeds threshold2, it rejects the request
            print(f"Server {i} is overloaded and rejecting request. Current load: {servers[i]} (Above Threshold2)")
            continue
            
    # If all servers exceed threshold2, reject the request
    print("All servers are either at or above critical capacity (Threshold2). Rejecting request.")

if __name__ == "__main__":
    for _ in range(12): # Simulate 12 requests
        assign_request_to_server("request")