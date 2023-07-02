# ##################################################################################### #
# Allen Blanton
# CS 372 Fall 2022
# Project 4: Client-Server Chat
#
# ADAPTED FROM 'echo-server.py'
# https://realpython.com/python-sockets/#echo-client-and-server
# ##################################################################################### #

import socket
import tictactoe

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
        new_game = tictactoe.TicTacToe()
        board = new_game.get_board()
        print(f"[Connected by {addr}]")
        print(f"[Welcome to Tic-Tac-Toe.]\n{board}\n")

        while True:
            # Wait on the client's move
            print("[Waiting for the client...]")
            conn.sendall(board.encode())
            choice = conn.recv(1024).decode()
            if not choice:
                print('[Connection closed.]')
                break
            move_successful = False
            while not move_successful:
                move_successful = new_game.make_move(choice)
                if not move_successful:
                    # prompt again for a valid move
                    conn.sendall('TRY AGAIN'.encode())
                    choice = conn.recv(1024).decode()

            # Check the state
            print(f"\n{new_game.get_board()}\n")
            state = new_game.get_state()
            if state != 'CONTINUE':
                conn.sendall(state.encode())
                print(f"[{state}]")
                print('[Closing connection.]')
                break

            # Make a move
            print(f"[Player O, what's your move? (Send '/q' to quit)]")
            choice = input('> ')
            if choice == QUIT:
                print('[Closing connection.]')
                break
            move_successful = False
            while not move_successful:
                move_successful = new_game.make_move(choice)
                if not move_successful:
                    print("[Please choose an available number.]")
                    choice = input('> ')

            # Check the state
            board = new_game.get_board()
            state = new_game.get_state()
            if state != 'CONTINUE':
                conn.sendall(f"{board}\n\n[{state}]".encode())
                print(f"\n[{state}]")
                print('[Closing connection]')
                break
