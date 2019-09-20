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

                elif input_one == 2:
                    if len(imp_list) == 0:
                        ret_list.append('impossible')
                        continue
                    # impossible
                    if input_two not in imp_list: # impossible
                        ret_list.append('impossible')
                        continue
                    if queue[0] != input_two: # Queue
                        isqueue = False
                    else:
                        queue.pop(0)

                    if stack[-1] != input_two: # stack
                        isstack = False
                    else:
                        stack.pop()
                            
                    if input_two != max(priority_queue): # priority
                        ispriority_queue = False
                    else:
                        priority_queue.remove(max(priority_queue))
                    
                    if iterations == 0:
                        if ispriority_queue and isqueue:
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
    '''))
