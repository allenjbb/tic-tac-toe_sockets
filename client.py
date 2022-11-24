# ##################################################################################### #
# ADAPTED FROM 'echo-client.py'
# https://realpython.com/python-sockets/#echo-client-and-server
# ##################################################################################### #

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 4343  # The port used by the server
QUIT = "/q"

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server at the HOST and PORT defined above
    s.connect((HOST, PORT))
    print(f'[Connected to {HOST}:{PORT}]')
    print('[Write your message... (Send "/q" to quit)]')
    while True:
        # Send message to the server
        message = input('> ')
        if message == QUIT:
            print('[Closing chat.]')
            break
        s.sendall(message.encode())
        # Wait on the server's reply
        reply = s.recv(1024)
        if not reply:
            print('[Chat closed.]')
            break
        print('<', reply.decode())
