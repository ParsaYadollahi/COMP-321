def main():
    healthy = list(input())
    disease = list(input())
        
        
    stack = []
    if healthy == disease:
        print(0)
    elif healthy and disease:
        for i in range(min(len(disease), len(healthy))):
            if healthy[i] != disease[i]: # find the uncommon area
                break

        stack = disease[i:] # append the diseased area and on

        stack_index = len(stack)-1
        healthy_index = len(healthy)-1
        while((stack_index >= 0 and healthy_index >= 0) and \
                    healthy[healthy_index] == stack[stack_index]): # move backwards
            stack.pop()
            healthy_index -= 1
            stack_index -= 1

        print(len(stack))
    else:
        print(len(disease))

if __name__ == "__main__":
    main()