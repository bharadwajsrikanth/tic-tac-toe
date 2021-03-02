theBoard = {7: ' ', 8: ' ', 9: ' ',
			4: ' ', 5: ' ', 6: ' ',
			1: ' ', 2: ' ', 3: ' '
			}

board_keys = []

for key in theBoard:
	board_keys.append(key)

def printBoard(board):
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])

def announceWinner(turn):
	print("Game over.")
	print(turn + " is the winner.")


def game():

	turn = 'X'
	count = 0

	for i in range(10):
		printBoard(theBoard)
		print( "Hey, " + turn + ". Your turn to play")

		move = int(input())

		if theBoard[move] == ' ':
			theBoard[move] = turn
			count += 1
		else:
			print("Invalid choice, try again")
			continue

		if count >= 5:
			if theBoard[7] == theBoard[8] == theBoard[9] != ' ':
				announceWinner(turn)
				break
			elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':
				announceWinner(turn)
				break
			elif theBoard[1] == theBoard[2] == theBoard[3] != ' ':
				announceWinner(turn)
				break
			elif theBoard[7] == theBoard[4] == theBoard[1] != ' ':
				announceWinner(turn)
				break
			elif theBoard[8] == theBoard[5] == theBoard[2] != ' ':
				announceWinner(turn)
				break
			elif theBoard[9] == theBoard[6] == theBoard[3] != ' ':
				announceWinner(turn)
				break
			elif theBoard[7] == theBoard[5] == theBoard[3] != ' ':
				announceWinner(turn)
				break
			elif theBoard[1] == theBoard[5] == theBoard[9] != ' ':
				announceWinner(turn)
				break

		if count == 9:
			print("Game over.")
			print("Its a tie.")
			return

		if turn == 'X':
			turn = '0'
		else:
			turn = 'X'


if __name__ == "__main__":
		game()


