
"""
***********************************************************************************
****                       Author: Alon Gritsovsky                             ****
**** Description: This fuzzing program mutates different packets to IOT device ****
***********************************************************************************
"""
import pyradamsa
import socket
import serial
import os
import glob


i = 0
number_of_packets = 12
iteration_number = 1
rad = pyradamsa.Radamsa()

server_IP = input("Enter IP address of the server: ") # IP OF LOCAL SERVER: "192.168.2.1"
server_PORT = int(input("Enter Source Port Number: ")) # PORT: 31337



# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((server_IP, server_PORT))
# become a server socket
serversocket.listen(5)
# wait for a connection from the client
client, address = serversocket.accept()


print(f"A client is connected to the server on port {server_PORT}.")


folder_path = "/root/Documents/fuzzer/fuzzer_packet"
packets = []

for file_path in glob.glob(os.path.join(folder_path, "*.txt")):
    with open(file_path, "r") as f:
        packet = bytearray.fromhex(f.read())
    packets.append(packet)


while True:
    raw_packet = packets[i]
    print("Packet before mutation:")
    print(raw_packet)
    mutated_packet = rad.fuzz(raw_packet)
    print("Packet after mutation:")
    print(mutated_packet)
    client.sendall(mutated_packet)
    print(f"Packet number ---> {iteration_number} was sent")
    iteration_number += 1
    i += 1
    if i % number_of_packets == 0:
        i = 0



# Close the socket connection
client.close()


