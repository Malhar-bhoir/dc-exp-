from rpc import RPCClient

# Initialize client and connect to server
# Make sure server.py is running before executing this
client = RPCClient('localhost', 8080)
client.connect()

print("Addition (5+6):", client.add(5, 6)) # Should print 11
print("Subtraction (5-6):", client.sub(5, 6)) # Should print -1

client.disconnect()