useless, divisor = list(map(int, input().split()))
input2 = list(map(int, input().split()))

d = {}
for i in range(len(input2)):
    if (input2[i]//divisor) not in d:
        d.setdefault(input2[i]//divisor, 1)
    else:
        d[input2[i]//divisor]+=1

res = 0

for i in d:
    res+=(d[i]*(d[i]-1))//2

print(res)