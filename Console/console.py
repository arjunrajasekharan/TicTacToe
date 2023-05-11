
import os

board = {
  1: ' 1',
  2: ' 2',
  3: ' 3',
  4: ' 4',
  5: ' 5',
  6: ' 6',
  7: ' 7',
  8: ' 8',
  9: ' 9'
}


def printBoard(board):
  n = 16
  print()
  print('-' * n)
  print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
  print('-' * n)
  print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
  print('-' * n)
  print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
  print('-' * n)
  print()


printBoard(board)


def checkBoard(board):
  # check who won

  if board[1] == board[2] == board[3]:
    print(board[1] + ' Won')
    toreturn = True
  elif board[4] == board[5] == board[6]:
    print(board[4] + ' Won')
    toreturn = True
  elif board[7] == board[8] == board[9]:
    print(board[7] + ' Won')
    toreturn = True

  elif board[1] == board[4] == board[7]:
    print(board[1] + ' Won')
    toreturn = True
  elif board[2] == board[5] == board[8]:
    print(board[2] + ' Won')
    toreturn = True
  elif board[3] == board[6] == board[9]:
    print(board[3] + ' Won')
    toreturn = True

  elif board[1] == board[5] == board[9]:
    print(board[1] + ' Won')
    toreturn = True
  elif board[3] == board[5] == board[7]:
    print(board[3] + ' Won')
    toreturn = True

  else:
    toreturn = False
  return toreturn


ox = next = 1
mykey = []
print('Enter any number from 1 to 9')


while next:
  ox %= 2
  value = ['😄', '❌']
  mess = f"{value[ox]}'s turn : "
  key = int(input(mess))

  if key not in mykey:
    if key not in range(1,10):
      os.system('cls')

      printBoard(board)
      print('Enter number within 1 and 9')
      continue

    mykey.append(key)
    board[key] = value[ox]
    ox += 1

    os.system('cls')
    printBoard(board)
    if checkBoard(board):
      break
  else:
    print('You tried to Over-Write, Try again...\n')
    next = 0
  next += 1

  if set(mykey) == set(range(1, 10)):
    print('Match Draw...')
    break


input('\nPress `Enter` to Exit.')
