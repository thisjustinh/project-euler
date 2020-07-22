import random as r

def knight_tour(n: int):
  """
  Perform a knight's tour on an n x n board, where n >= 5.
  """
  board = []
  for row in range(n):
    row = []
    for col in range(n):
      row.append("0")
    board.append(row)
  
  knight = (r.randrange(0,n), r.randrange(0, n))
  board[knight[0]][knight[1]] = u"\u265E"
  exclude = [knight]
  str_board(board)

  next_move = warnsdorff(knight, n, exclude)
  print(next_move)

  while next_move is not None:
    board[knight[0]][knight[1]] = "x"
    knight = next_move
    exclude.append(knight)
    board[knight[0]][knight[1]] = u"\u265E"
    next_move = warnsdorff(knight, n, exclude)
    str_board(board)
    print(next_move)

def warnsdorff(position: tuple, n: int, exclude: list) -> tuple:
  """
  Finds the optimal move for the knight using Warnsdorff's rule.
  For each possible move for the knight, calculate the number of moves possible from that position. From there, return the (i, j) position of the move that has the least number of moves from there.
  If no moves are available, return None. 
  position: current (row, col) position of knight
  n: size of the board, where n >= 5
  exclude: list of tuples of positions already moved by knight
  """
  knight_x, knight_y = position
  moves = [(-2,1),(-1,2),(1,2),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
  optimal = [(-1,-1),100]
  for (dx, dy) in moves:
    check_x, check_y = knight_x + dx, knight_y + dy
    if not (check_x, check_y) in exclude and 0 <= check_x < n and 0 <= check_y < n:
      count = 0
      for (dx1, dy1) in moves:
        check_x1, check_y1 = check_x + dx1, check_y + dy1
        if not (check_x1, check_y1) in exclude and 0 <= check_x1 < n and 0 <= check_y1 < n:
          count += 1
      if count < optimal[1]:
        optimal = [(check_x, check_y), count]
  if optimal == [(-1,-1),100]:
    return None
  return optimal[0]

def str_board(board: list):
  """
  Print out the board state into the console and make it look pretty.
  """
  for i in board:
    for j in i:
      print(j, end=' ')
    print('')

knight_tour(8)