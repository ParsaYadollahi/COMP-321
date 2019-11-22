p, q, s = map(int, input().split())

list_p = []
list_q = []
a = p
while a <= s:
    list_p.append(a)
    a += p
a = q
while a <= s:
    list_q.append(a)
    a += q
ans = (set(list_p) & set(list_q))
if len(ans):
    print('yes')
else:
    print('no')