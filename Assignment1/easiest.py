'''
https://open.kattis.com/problems/easiest
'''
class Solution(object):
    def easiest(self, digit):
        """
        :type digit: int 
        :rtype: int
        """
        if digit == 0: return
        final_sum = self.sum_digits(digit)
        temp_sum =  0
        p = 11
        while True:
            temp_sum = p * digit
            if self.sum_digits(temp_sum) == final_sum:
                return p
            p += 1

    def sum_digits(self, digit):
        ret_int = 0
        while digit:
            ret_int += digit%10
            digit = digit//10
        return ret_int

if __name__ == "__main__":
    sol = Solution()

    tc1 = 3029
    tc2 = 4
    tc3 = 5
    tc4 = 42
    tc5 = 0

    print(sol.easiest(tc1))
    print(sol.easiest(tc2))
    print(sol.easiest(tc3))
    print(sol.easiest(tc4))
    print(sol.easiest(tc5))
