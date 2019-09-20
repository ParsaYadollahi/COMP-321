'''
https://open.kattis.com/problems/trik
'''
class Solution(object):
    def trik(self, pattern):
        """
        :type pattern: str 
        :rtype: int
        """

        position = 1
        for char in pattern:
            # a evoked
            if char.lower() == 'a':
                if position == 1:
                    position = 2
                elif position == 2:
                    position = 1
            # b evoked
            elif char.lower() == 'b':
                if position == 2:
                    position = 3
                elif position == 3:
                    position = 2
            # c evoked
            else:
                if position == 1:
                    position = 3
                elif position == 3:
                    position = 1


        return position

if __name__ == "__main__":
    sol = Solution()
    test_case_1 = 'AB' # return 3
    test_case_2 = 'CBABCACCC' # return 1
    test_case_3 = 'C' # return 3
    test_case_4 = 'ABCCBA' # return 1

    print(sol.trik(test_case_1))
    print(sol.trik(test_case_2))
    print(sol.trik(test_case_3))
    print(sol.trik(test_case_4))

