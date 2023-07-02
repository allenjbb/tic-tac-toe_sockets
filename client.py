# ##################################################################################### #
# Allen Blanton
# CS 372 Fall 2022
# Project 4: Client-Server Chat
#
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
    board = s.recv(1024).decode()
    print(f"[Welcome to Tic-Tac-Toe.]\n{board}\n\n[Player X, what's your move? (Send '/q' to quit)]")
    while True:
        # Make a move
        choice = input('> ')
        if choice == QUIT:
            print('[Closing connection.]')
            break
        s.sendall(choice.encode())
        # Wait on the server's response
        print("[Waiting for the server...]")
        board = s.recv(1024).decode()
        if not board:
            print('[Connection closed.]')
            break
        elif board == 'TRY AGAIN':
            print('[Please choose an available number.]')
            continue
        elif board[-1] != '-':
            print(f"\n{board}")
            print('[Connection closed.]')
            break
        print(f"\n{board}\n\n[Player X, what's your move? (Send '/q' to quit)]")
