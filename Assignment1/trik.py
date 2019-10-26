'''
https://open.kattis.com/problems/trik
'''
def trik():
    import sys
    pattern = sys.stdin.readlines()
    """
    :type pattern: str 
    :rtype: int
    """

    position = 1
    string = list(pattern[-1].strip())
    for char in string:
        # a evoked
        if char.lower() == 'a': # swap
            if position == 1:
                position = 2
            elif position == 2:
                position = 1
        # b evoked
        elif char.lower() == 'b':# swap
            if position == 2:
                position = 3
            elif position == 3:
                position = 2
        # c evoked
        elif char.lower() == 'c': # swap
            if position == 1:
                position = 3
            elif position == 3:
                position = 1


    print(position)

if __name__ == "__main__":
    trik()
