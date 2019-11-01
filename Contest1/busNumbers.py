useless = input()
buses = list(map(int, input().split()))

buses.sort()
strks = []
ret_string = []

strks.append(buses[0])
for i in range(1,len(buses)):
    if buses[i] - buses[i-1] == 1:
        strks.append(buses[i])
    else:
        if len(strks) > 2:
            ret_string.append('{a}-{b}'.format(a = strks[0], b = strks[-1]))
        else:   
            ret_string = ret_string + strks
        strks = []
        strks.append(buses[i])

if len(strks) > 2:
    ret_string.append('{a}-{b}'.format(a = strks[0], b = strks[-1]))
else:   
    ret_string = ret_string + strks
print(*ret_string)