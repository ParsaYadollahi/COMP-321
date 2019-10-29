import sys
sys.setrecursionlimit(1000000)
def backtrack(depth, result, combinations, target):

    if sum(result) == target: # if the combinations is equal to the result append it to the list
        results.append(result)
        if len(result) > 2:
            return
    else:
        for i in range(depth, len(combinations)): # iterate through each of the elements in the list

            if target - sum(result) < combinations[i]: # backtrack (remove the last added element)
                break # removes the last added number (no return statement)
            else:
                # add the next element (or the current one) at combinations[i] to the list
                backtrack(i, result + [combinations[i]], combinations, target)

if __name__ == "__main__":
    numb_orders = int(input()) # useless
    comb = list(map(int, input().split())) # the menu

    numb_individuals = int(input()) # useless
    targets = list(map(int, input().split())) # individuals with money

    combinations = sorted(comb) # sort the list

    for target in targets: # loop through each of the individuals that have "money"
        results = []
        backtrack(0, [], combinations, target) # returns a 2d list with all combinations
        
        # display the answers for each individual
        if len(results) == 0: 
            print('Impossible')
        elif len(results) > 1:
            print('Ambiguous')
        else:
            for i in results[0]:
                print(combinations.index(i) + 1, end=' ') # print the index of the element
            print()