def main():
    first = map(int, input().split())
    second = map(int, input().split())

    second.append(0)
    second.append(first[0])
    ret_list = []

    # criteria: Brute force it.... So we go with O(n^2)   
    for i in second:
        for j in second:
            # compare each element in list to the other
            width = abs(i-j)
            # add if it not already in the list
            if width not in ret_list:
                ret_list.append(width)
    
    ret_list.sort()
    ret_list.pop(0) # remove 0 since can't be valid area
    s_ret_list = [str(i) for i in ret_list] # print list without commas/brackets
    print(' '.join(s_ret_list))

if __name__ == "__main__":
    main()
    # code is so brute forced it hurts - never again
            