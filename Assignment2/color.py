# input
socks_det = list(map(int, input().split()))
socks = list(map(int, input().split()))

socks.sort() # sort array

# initialize counters
counter = 0
min_socks = 0
numb_laundry = 0
from collections import Counter

for s in socks:

    if numb_laundry == 0:

        counter = 1
        numb_laundry += 1
        numb_socks = s
        continue

# need to make another machine
    if counter >= socks_det[1] or abs(s-numb_socks) > socks_det[2]:

        counter = 1
        numb_laundry += 1
        numb_socks = s

    else:
        # add to the counter
        
        counter += 1

print(numb_laundry)