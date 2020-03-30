def print_battlefield(mat):
    print(f"""
    ---------
    | {mat[0][0]} {mat[0][1]} {mat[0][2]} |
    | {mat[1][0]} {mat[1][1]} {mat[1][2]} |
    | {mat[2][0]} {mat[2][1]} {mat[2][2]} |
    ---------
    """)


def occupy(field, col, row, mark):
    if field[abs(row - 3)][col - 1] in ['X', 'O']:
        return field, True
    else:
        field[abs(row - 3)][col - 1] = mark
        return field, False


def check_line(line, player):
    return all([el == player for el in line])


def check_state(mat, player):
    lines = [check_line(row, player) for row in mat]
    lines += [check_line([mat[i][j] for i in range(3)], player) for j in range(3)]
    lines += [check_line([mat[i][j] for i in range(3) for j in range(3) if i == j], player)]
    lines += [check_line([mat[i][j] for i in range(3) for j in range(3) if i + j == 2], player)]
    return any(lines)


def check_digits(in_str):
    if in_str not in "0123456789":
        return False
    return True


current_player = 'X'
moves = 0
battlefield = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print_battlefield(battlefield)

while True:
    in_col, in_row = input("Enter the coordinates: ").split()

    if not check_digits(in_col) or not check_digits(in_row):
        print("You should enter numbers!")
        continue
    else:
        in_col = int(in_col)
        in_row = int(in_row)

    if in_col not in range(1, 4) or in_row not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        continue
    else:
        battlefield, occupied = occupy(battlefield, in_col, in_row, current_player)
        if occupied:
            print("This cell is occupied! Choose another one!")
            continue
        else:
            moves += 1
            print_battlefield(battlefield)
            if check_state(battlefield, current_player):
                print(f"{current_player} wins")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
            if moves == 9:
                print("Draw")
                break
