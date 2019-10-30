healthy = list(input())
disease = list(input())
# inputs 
    
stack = []
i = 0
while(i < min(len(healthy), len(disease)) and healthy[i] == disease[i]):
    i+=1 # find where the two list dont match

# add disease and on to stack
stack = disease[i:]
healthy = healthy[i:]


s_index = len(stack)-1
h_index = len(healthy)-1

while(stack and healthy and healthy[h_index] == stack[s_index]): # move backwards
    stack.pop() # remove elements in common at the of stack
    h_index -= 1
    s_index -= 1

print(len(stack))
