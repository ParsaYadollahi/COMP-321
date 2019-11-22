input = list(input().split())

def split(word): 
    return [char for char in word]  

s = ''

if input[0] == 'E':
    count = 0
    current = input[1][:1]
    for c in input[1]:
        if (c == current):
            count+=1
        else:
            s = s + current + str(count)
            current = c
            count = 1
    s = s + current + str(count)
else:
    char = ''
    for c in input[1]:
        if c.isdigit():
            s = s + char*int(c)
            continue
        char = c

print(s)