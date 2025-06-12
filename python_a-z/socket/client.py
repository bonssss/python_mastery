import socket

host = socket.gethostname()
port= 4000

c_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
c_socket.connect((host, port))  # Connect to the server
print(f"Connected to server at {host}:{port}")

msg = input("-> ")

while msg.lower().strip() != 'bye':
    c_socket.sendall(msg.encode())  # Send data to the server
    data = c_socket.recv(1024).decode()  # Receive data from the server
    print(f"Received from server: {data}")
    msg = input("-> ")
c_socket.close()  # Close the socket connection
print("Connection closed.")