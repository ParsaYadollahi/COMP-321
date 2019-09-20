import re
class Solution(object):
    def guessthedatastructure(self, input):
        """
        :type imput: str 
        :rtype: list
        """

        p1 = re.compile(r'^(?P<single_input>\d+)$')
        p2 = re.compile(r'^(?P<input_1>\d+)\s+(?P<input_2>\d+)$')
        ret_list = []
        queue = []
        stack = []
        priority_queue = []   

        for line in input.splitlines():
            line = line.strip()
            
            m = p1.match(line)
            if m:
                iterations = int(m.groupdict()['single_input'])
                stack = []
                queue = []
                priority_queue = []
                imp_list = []
                ispriority_queue = isstack = isqueue = True
                isimpossible = False
            
            m = p2.match(line)
            if m:
                iterations -= 1
                input_one = int(m.groupdict()['input_1'])
                input_two = int(m.groupdict()['input_2'])

                if input_one == 1: # append
                    queue.append(input_two)
                    stack.append(input_two)
                    priority_queue.append(input_two)
                    imp_list.append(input_two)

                    # impossible
                elif input_one == 2:
                    # case: trying to remove elements when didnt add any
                    if len(imp_list) == 0:
                        isimpossible = True
                    # case: trying to remove an element not in the list
                    elif input_two not in imp_list:
                        isimpossible = True
                    else:
                        if queue[0] == input_two: # Queue
                            queue.pop(0)
                        else:
                            isqueue = False

                        if stack[-1] == input_two: # stack
                            stack.pop()
                        else:
                            isstack = False
                            
                        if input_two == max(priority_queue): # priority
                            priority_queue.remove(max(priority_queue))
                        else:
                            ispriority_queue = False
                if iterations == 0:
                    if isimpossible:
                        ret_list.append('impossible')
                    elif ispriority_queue and isqueue:
                        ret_list.append('not sure')
                    elif ispriority_queue and isstack:
                        ret_list.append('not sure')
                    elif isstack:
                        ret_list.append('stack')
                    elif isqueue:
                        ret_list.append('queue')
                    elif ispriority_queue:
                        ret_list.append('priority queue')
                
        return ret_list

if __name__ == "__main__":
    sol = Solution()

    print(sol.guessthedatastructure('''
6
1 1
1 2
1 3
2 1
2 2
2 3
6
1 1
1 2
1 3
2 3
2 2
2 1
2
1 1
2 2
4
1 2
1 1
2 1
2 2
7
1 2
1 5
1 1
1 3
2 5
1 4
2 4
1
2 1
4
1 1
1 1
2 1
2 1

 5
1 10
2 10
2 20
2 30
1 40


    '''))
