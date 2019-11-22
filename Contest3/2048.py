def main():
    graph = [list(map(int, input().split())) for _ in range(4)]

    d = int(input())

    if d == 0:
        # Left
        for j in range(4):
            fixed = set()
            changed = 1
            while changed > 0:
                changed = 0
                for i in range(1, 4):
                    if graph[j][i] == 0:
                        continue
                    if graph[j][i-1] == 0:
                        graph[j][i-1] = graph[j][i]
                        graph[j][i] = 0
                        changed += 1
                        if i in fixed:
                            fixed.remove(i)
                            fixed.add(i-1)
                    elif i not in fixed and (i-1) not in fixed and graph[j][i-1] == graph[j][i]:
                        graph[j][i-1] *= 2
                        graph[j][i] = 0
                        fixed.add(i-1)
                        changed += 1
    elif d == 1:
        # Up
        for i in range(4):
            fixed = set()
            changed = 1
            while changed > 0:
                changed = 0
                for j in range(1, 4):
                    if graph[j][i] == 0:
                        continue
                    if graph[j-1][i] == 0:
                        graph[j-1][i] = graph[j][i]
                        graph[j][i] = 0
                        changed += 1
                        if j in fixed:
                            fixed.remove(j)
                            fixed.add(j-1)
                    elif j not in fixed and (j-1) not in fixed and graph[j-1][i] == graph[j][i]:
                        graph[j-1][i] *= 2
                        graph[j][i] = 0
                        fixed.add(j-1)
                        changed += 1
    elif d == 2:
        # Right
        for j in range(4):
            fixed = set()
            changed = 1
            while changed > 0:
                changed = 0
                for i in range(2, -1, -1):
                    if graph[j][i] == 0:
                        continue
                    if graph[j][i+1] == 0:
                        graph[j][i+1] = graph[j][i]
                        graph[j][i] = 0
                        changed += 1
                        if i in fixed:
                            fixed.remove(i)
                            fixed.add(i+1)
                    elif i not in fixed and (i+1) not in fixed and graph[j][i+1] == graph[j][i]:
                        graph[j][i+1] *= 2
                        graph[j][i] = 0
                        fixed.add(i+1)
                        changed += 1
    else:
        # Down
        for i in range(4):
            fixed = set()
            changed = 1
            while changed > 0:
                changed = 0
                for j in range(2, -1, -1):
                    if graph[j][i] == 0:
                        continue
                    if graph[j+1][i] == 0:
                        graph[j+1][i] = graph[j][i]
                        graph[j][i] = 0
                        changed += 1
                        if j in fixed:
                            fixed.remove(j)
                            fixed.add(j+1)
                    elif j not in fixed and (j+1) not in fixed and graph[j+1][i] == graph[j][i]:
                        graph[j+1][i] *= 2
                        graph[j][i] = 0
                        fixed.add(j+1)
                        changed += 1


    for j in range(4):
        print(*graph[j])
if __name__ == "__main__":
    main()
    