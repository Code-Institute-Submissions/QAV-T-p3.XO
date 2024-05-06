import os

# Displying the main board
def board(spots):
    board = (f"| {spots[1]} | {spots[2]} | {spots[3]} |\n"
             f"-------------\n"
             f"| {spots[4]} | {spots[5]} | {spots[6]} |\n"
             f"-------------\n"
             f"| {spots[7]} | {spots[8]} | {spots[9]} |")
    print(board)

    # check player turn function 
def check_turn(turn):
        if turn % 2 == 0:
             return 'O'
        else:
         return 'X' 

def check_for_win(spots):
    # Handle Horizontal Cases
    if (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
        return True
    # Handle Vertical Cases
    elif (spots[1] == spots[4] == spots[7]) \
    or (spots[2] == spots[5] == spots[8]) \
    or (spots[3] == spots[6] == spots[9]):
        return True
    # Diagonal Cases
    elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
        return True
    else:
        return False             

def main():
    while True:
        # Declare all the variables
        spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                 6: '6', 7: '7', 8: '8', 9: '9'}
        playing, complete = True, False
        turn = 0
        prev_turn = -1

        # Game Loop
        while playing:
            os.system('cls' if os.name == 'nt' else 'clear')
            board(spots)
            # If an invalid turn occurred
            if prev_turn == turn:
                print("Invalid spot selected, please pick another.")
            prev_turn = turn
            print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press q to quit")

            # Get the user choice and check its validation
            choice = input()
            if choice == 'q':
              playing = False
            elif str.isdigit(choice) and int(choice) in spots:
                 if not spot[int(choice)] in {"X", "O"}: 
                    turn += 1
                    spots[int(choice)] = check_turn(turn)

            # Check the end of the game
            if check_for_win(spots):
                playing, complete = False, True
                if turn > 8:
                    playing = False        


