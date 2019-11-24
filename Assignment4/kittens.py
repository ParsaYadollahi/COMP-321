def main():
    dic = {}

    kitten = int(input())

    while True:
        inp = list(map(int, input().split()))
        if len(inp) == 1:
            break
        for i in inp[1:]:
            dic[i] = inp[0]

    while True:
        print(kitten, end=" ")
        if kitten in dic:
            kitten = dic[kitten]
        else:
            print()
            break

if __name__ == "__main__":
    main()