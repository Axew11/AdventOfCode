with open("input1.txt", 'r') as f:
    array = [int(line) for line in f]
    flag = True
    for x in array[:-1]:
        if flag and (2020 - x) in array:
            print(f"Day 1 Part 1: {x * (2020 - x)}")
            flag = False
        for y in array:
            if (2020 - y - x) in array:
                print(f"Day 1 Part 2: {x * y * (2020 - y - x)}")
                exit(0)
