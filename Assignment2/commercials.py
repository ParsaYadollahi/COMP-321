
# inputs
first = list(map(int, input().split()))
second = list(map(int, input().split()))

if first[0] == 0:
    print(0)

tot_max = second[0]
max_so_far = 0

for i in second:
    # add elements to list
    max_so_far += i-first[1]

    # if smaller, refresh
    if (max_so_far <= 0):
        max_so_far = 0
    # if bigger, increment
    if (max_so_far >= tot_max):
        tot_max = max_so_far

print(tot_max)