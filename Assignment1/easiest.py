'''
https://open.kattis.com/problems/easiest
'''
def easiest():
    """
    :type digit: int 
    :rtype: int
    """
    import sys
    while(1):
        digit = input() # input from user
        digit = int(digit)
        if digit == 0: return
        final_sum = sum_digits(digit) # sum of wanted digits
        temp_sum =  0
        for p in range (11,100000): # max should be 100 so will never go to 100000
            temp_sum = p * digit
            if sum_digits(temp_sum) == final_sum:
                print(p)
                break

def sum_digits(digit):
    ret_int = 0
    while digit: # sum of digits calc
        ret_int += digit%10
        digit = digit//10
    return ret_int

if __name__ == "__main__":
    easiest()