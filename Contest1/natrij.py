timeA = list(map(int, input().split(":")))
timeB = list(map(int, input().split(":")))

t1 = timeA[0]*3600 + timeA[1]*60 + timeA[2]
t2 = timeB[0]*3600 + timeB[1]*60 + timeB[2]

diff_time = [0,0,0]

if t1 > t2:
    t2 = 24*3600 + t2

diff_seconds = abs(t1-t2)
if diff_seconds > 24*3600-1 or diff_seconds <= 0:
    print('24:00:00')
else:
    while (diff_seconds > 0):
        if (diff_seconds // 3600 > 0):
            diff_time[0] = (diff_seconds//3600)
            diff_seconds = diff_seconds%3600

        elif (diff_seconds // 60 > 0):
            diff_time[1] = (diff_seconds//60)
            diff_seconds = diff_seconds%60
        
        else:
            diff_time[2] = (diff_seconds)
            break

    if diff_time[0] < 10:
        diff_time[0] = '0' + str(diff_time[0])

    if diff_time[1] < 10:
        diff_time[1] = '0' + str(diff_time[1])

    if diff_time[2] < 10:
        diff_time[2] = '0' + str(diff_time[2])

    for i in range(len(diff_time)):
        diff_time[i] = str(diff_time[i])


    diff_time = ':'.join(diff_time)

    print(diff_time)