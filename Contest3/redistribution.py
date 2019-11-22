def main():
    nb_rooms = int(input())

    numb_exams_per_room = [int(x) for x in input().split()]

    sorted_room_numb = sorted(range(0, nb_rooms), key = lambda x: -numb_exams_per_room[x])

    if numb_exams_per_room[sorted_room_numb[0]] > sum([numb_exams_per_room[i] for i in sorted_room_numb[1:]]):
        print('impossible')
    else:
        print(' '.join([str(i+1) for i in sorted_room_numb]))

if __name__ == "__main__":
    main()