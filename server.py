# ##################################################################################### #
# ADAPTED FROM 'echo-server.py'
# https://realpython.com/python-sockets/#echo-client-and-server
# ##################################################################################### #

import socket

HOST = "127.0.0.1"  # localhost
PORT = 4343
QUIT = "/q"

# Create the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the HOST and PORT defined above
    s.bind((HOST, PORT))
    # Listen for a connection
    print(f'[Server listening on {HOST}:{PORT}... (Press Ctrl-C to stop)]')
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'[Connected by {addr}]')
        print(f'[Waiting for message... (Reply "/q" to quit)]')
        while True:
            # Wait on the client's message
            message = conn.recv(1024)
            if not message:
                print('[Chat closed.]')
                break
            print('<', message.decode())
            # Send reply to the client
            reply = input('> ')
            if reply == QUIT:
                print('[Closing chat.]')
                break
            conn.sendall(reply.encode())
