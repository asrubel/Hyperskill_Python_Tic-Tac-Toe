def cells2mat(cells, rotate=False):
    mat = []
    for i in range(3):
        mat.append([])
        for j in range(3):
            index = (j * 3 + i) if rotate else (i * 3 + j)
            mat[i].append(cells[index])
    return mat


def print_battle_field(mat):
    print(f"""
    ---------
    | {mat[0][0]} {mat[0][1]} {mat[0][2]} |
    | {mat[1][0]} {mat[1][1]} {mat[1][2]} |
    | {mat[2][0]} {mat[2][1]} {mat[2][2]} |
    ---------
    """)


def check_line(line, side):
    return len([el for el in line if el == side]) == 3


def check_state(mat):
    x_marks = len([mat[i][j] for i in range(3) for j in range(3) if mat[i][j] == "X"])
    o_marks = len([mat[i][j] for i in range(3) for j in range(3) if mat[i][j] == "O"])
    return x_marks + o_marks == 9, abs(x_marks - o_marks) <= 1


input_cells = input("Enter cells: ")
battlefield = cells2mat(input_cells)
rotated_battlefield = cells2mat(input_cells, True)
battle_sides = ["X", "O"]
wins = [[], []]

for b in range(len(battle_sides)):
    wins[b] += [check_line(row, battle_sides[b]) for row in battlefield]
    wins[b] += [check_line(row, battle_sides[b]) for row in rotated_battlefield]
    wins[b] += [check_line([battlefield[i][j] for i in range(3) for j in range(3) if i == j], battle_sides[b])]
    wins[b] += [check_line([battlefield[i][j] for i in range(3) for j in range(3) if i + j == 2], battle_sides[b])]

print_battle_field(battlefield)
finished, correct = check_state(battlefield)
x_won = True in wins[0]
o_won = True in wins[1]
if not correct:
    print("Impossible")
elif not finished and not x_won and not o_won:
    print("Game not finished")
elif not x_won and not o_won:
    print("Draw")
elif x_won and o_won:
    print("Impossible")
elif x_won:
    print("X wins")
elif o_won:
    print("O wins")
