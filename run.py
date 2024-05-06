import os

# Displaying the main board
def draw_board(spots):
    board = (f"| {spots[1]} | {spots[2]} | {spots[3]} |\n"
             f"-------------\n"
             f"| {spots[4]} | {spots[5]} | {spots[6]} |\n"
             f"-------------\n"
             f"| {spots[7]} | {spots[8]} | {spots[9]} |")
    print(board)

#check the turn
def check_turn(turn):
    if turn % 2 == 0:
        return 'X'
    else:
        return 'O'

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
        playing = True
        turn = 0
        prev_turn = -1

        # Game Loop
        while playing:
            # Reset the screen
            os.system('cls' if os.name == 'nt' else 'clear')
            # Draw the current Game Board
            draw_board(spots)
            if prev_turn == turn:
                print("Invalid spot selected, please pick another.")
            prev_turn = turn
            print("Player " + check_turn(turn) + "'s turn: Pick your spot or press q to quit")

            # Get input and make sure it's valid
            choice = input()
            if choice == 'q':
                playing = False
            elif str.isdigit(choice) and int(choice) in spots:
                # Check if the spot is already taken.
                if not spots[int(choice)] in {"X", "O"}:
                    # If not, update board and increment the turn
                    spots[int(choice)] = check_turn(turn)
                    turn += 1
                    

                    if check_for_win(spots):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        draw_board(spots)
                        print(f"Player {spots[int(choice)]} wins!")
                        playing = False
                    elif turn == 9:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        draw_board(spots)
                        print("It's a tie!")
                        playing = False
                else:
                    print("Invalid spot selected, please pick another.")

        restart = input("Do you want to play again? (y/n): ").strip().lower()
        if restart != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
