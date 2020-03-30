def cells2mat(cells):
    mat = []
    for i in range(3):
        mat.append([])
        for j in range(3):
            index = i * 3 + j
            mat[i].append(cells[index])
    return mat


def print_battlefield(mat):
    print(f"""
    ---------
    | {mat[0][0]} {mat[0][1]} {mat[0][2]} |
    | {mat[1][0]} {mat[1][1]} {mat[1][2]} |
    | {mat[2][0]} {mat[2][1]} {mat[2][2]} |
    ---------
    """)


def occupy(field, col, row, mark):
    if field[abs(row - 3)][col - 1] in ['X','O']:
        return field, True
    else:
        field[abs(row - 3)][col - 1] = mark
        return field, False


def check_digits(in_str):
    if in_str not in "0123456789":
        return False
    return True


input_cells = input("Enter cells:")
battlefield = cells2mat(input_cells)
print_battlefield(battlefield)

while True:
    in_col, in_row = input("Enter the coordinates:").split()

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
        battlefield, occupied = occupy(battlefield, in_col, in_row, 'X')
        if occupied:
            print("This cell is occupied! Choose another one!")
            continue
        else:
            print_battlefield(battlefield)
            break
