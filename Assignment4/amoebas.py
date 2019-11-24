def main():
    rnge, d = map(int, input().split())

    diag = [[True if char == '#' else False for char in input()] for _ in range(rnge)]
    colum = [[None for _ in range(d)] for _ in range(rnge)]
    col = 0

    def flood(row, c, grey):
        if row < 0 or c < 0 or row >= d or c >= rnge:
            return
        if not diag[c][row]:
            return
        if colum[c][row]:
            return
        colum[c][row] = grey
        flood(row+1, c, grey)
        flood(row+1, c-1, grey)
        flood(row+1, c+1, grey)
        flood(row, c-1, grey)
        flood(row, c+1, grey)
        flood(row-1, c, grey)
        flood(row-1, c-1, grey)
        flood(row-1, c+1, grey)

    for i in range(d):
        for j in range(rnge):
            if diag[j][i] and not colum[j][i]:
                col += 1
                flood(i, j, col)


    print(col)

if __name__ == "__main__":
    main()