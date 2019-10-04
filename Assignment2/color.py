'''
https://open.kattis.com/problems/color
'''

def valid_insert(element, container, capacity, max_diff):
    from collections import Counter
    for sub_list in container:# iterate through each sublist in the container
        c = Counter(sub_list)
        # fist element in container
        if not sub_list:
            continue
        
        # insert element if is already in the sublist
        if element in sub_list and len(sub_list) < capacity:
            sub_list.append(element)
            return

        # insert element if distinct and able to insert
        elif len(sorted(c)) <= max_diff and len(sub_list) < capacity:
            sub_list.append(element)
            return

    # if cannot be inserted, create a new 'laundry' and insert
    new_list = []
    new_list.append(element)
    container.append(new_list)
    return


def main():
    container = []
    
    # inputs
    data = map(int, input().split())
    socks = map(int, input().split())

    capacity = data[1]
    max_diff = data[2]

    for i in socks: # loop through each socks
        valid_insert(i, container, capacity, max_diff)
    
    print(len(container)) # answer is amount of sublists

if __name__ == "__main__":
    main() 