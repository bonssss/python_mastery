import socket

host = socket.gethostname()  # Get the local machine name

port=4000

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
s.bind((host, port))  # Bind to the port 
s.listen(5)  # Now wait for client connection
print(f"Server started at {host}:{port}")

conn , address= s.accept()  # Establish connection with client`
print(f"Got connection from {address}")
msg = input("-> ")  # Input message to send to the client

while True:
    conn.send(msg.encode())  # Send data to the client
    data = conn.recv(1024).decode()  # Receive data from the client
    if not data: 
        break  # If no data, exit the loop
    print(f"Received from client: {data}")
    msg = input("-> ")  # Input message to send to the client
#     data = conn.recv(1024).decode()  # Receive data from the client
#     if not data: 
#         break  # If no data, exit the loop
#     print(f"Received from client: {data}")
#     conn.send(data.encode())  # Echo back the received data`
# conn.close()  # Close the connection