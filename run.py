import os

# Displying the main board
def board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

    # check player turn function 
    def check_turn(turn):
            if turn % 2 == 0:
              return 'O'
            else:
              return 'X' 


    # Get input and make sure it's valid
    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spot[int(choice)] in {"X", "O"}: 
            turn += 1
            spots[int(choice)] = check_turn(turn) 


#def main():
