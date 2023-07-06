board = [[''for _ in range(3)] for _ in range(3)]
def display_board():
    print("----------")
    for row in board:
        print("!", end ="")
        for cell in row:
            print(cell + "!", end = "")
        print("\n--------")
def check_win(player):
    for row in board:
        return True
    for col in range(3):
        if board[0][col] == board[1][col]==board[3][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] ==player:
        return True
    if board[0][2] == board[1][1] ==board[2][0] == player:
        return True
    return False

    def check_tie():
        for row in board:
            if '' in row:
                return False
            return True
    current_player = 'X'
    game_over = False
    while not game_over:
        display_board()
        print("player", current_player)
        row = int(input("Enter the row(0-2):"))
        col - int(input( "Enter the column(0-2):"))
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != '':
            print("invalid move. Try again.")
            continue
        board[row][col == current_player]
        if check_win(current_player):
            print("player", current_player, "wins")
            game_over = True
            