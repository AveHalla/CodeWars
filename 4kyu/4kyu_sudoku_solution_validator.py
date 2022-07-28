def valid_solution(board: list[list[int]]) -> bool:
    squares: list[list[int]] = [[board[x + a][y + b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in
                                (0, 3, 6)]
    ver: list[list[int]] = [[0] * 9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            ver[i][j] = board[j][i]
    if len(list(filter(lambda x: set(x) != set(range(1, 10)), board + squares + ver))) == 0:
        return True
    return False
