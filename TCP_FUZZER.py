import socket
import random

TCP_IP = '172.25.14.53' # IP address of the server
TCP_PORT = 80 # Port number to use

# Create a TCP socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
s.bind((TCP_IP, TCP_PORT))

# Listen for incoming connections
s.listen(1)

print('Waiting for client connection...')

# Accept a client connection
conn, addr = s.accept()
print('Client connected:', addr)

# Send random packets to the client
while True:
    # Generate a random packet of data
    packet = bytes([random.randint(0, 255) for _ in range(10)])
    print('Sending packet:', packet)
    # Send the packet to the client
    conn.send(packet)
    # Time before sending the next packet
    time.sleep(1)



