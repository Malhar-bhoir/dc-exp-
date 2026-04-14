from rpc import RPCServer

# Define functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# Initialize server
server = RPCServer()

# Register functions
server.registerMethod(add)
server.registerMethod(sub)

# Run the server (Run this file first!)
if __name__ == '__main__':
    server.run()