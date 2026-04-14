# --- Stateful System ---
request_count = 0 # Global variable to store state

def stateful():
    global request_count
    request_count += 1
    return f"Stateful: You have visited {request_count} times."

print("--- Stateful Demo ---")
try:
    n_stateful = int(input("Enter number of requests for stateful: "))
    for _ in range(n_stateful):
        print(stateful())
except ValueError:
    print("Please enter a valid integer.")


# --- Stateless System ---
def stateless():
    visit_count = 1 # Always resets to 1 as it doesn't remember state
    return f"Stateless: You have visited {visit_count} times."

print("\n--- Stateless Demo ---")
try:
    n_stateless = int(input("Enter number of requests for stateless: "))
    for _ in range(n_stateless):
        print(stateless())
except ValueError:
    print("Please enter a valid integer.")