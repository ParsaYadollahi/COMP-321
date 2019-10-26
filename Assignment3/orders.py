def backtrack(depth, result, combinations, target):
    if sum(result) == target:
        results.append(result)
        return
    else:
        for i in range(depth, len(combinations)):
            if target - sum(result) < combinations[i]:
                break
            else:
                backtrack(i, result + [combinations[i]], combinations, target)


def output_result(result):
    if len(result) == 0:
        print('Impossible')
    elif len(result) > 1:
        print('Ambiguous')
    else:
        for sub_arr in result:
            for i in sub_arr:
                print(combinations.index(i) + 1, end=' ')
            print()





numb_orders = int(input()) # useless
combinations = list(map(int, input().split()))

numb_individuals = int(input()) # useless
targets = list(map(int, input().split()))

combinations.sort()

for i in targets:
    results = []
    backtrack(0, [], combinations, i)
    output_result(results)