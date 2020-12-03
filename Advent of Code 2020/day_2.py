 with open("input2.txt", 'r') as f:
     part1_total = 0
     part2_total = 0
     for line in f:
         data = line.split(":")
         char = data[0].split(' ')[1]
         minimum, maximum, password = int(data[0].split('-')[0]), int(data[0].split('-')[1].strip(char)), data[1].       strip(" ").strip("\n")
         if password.count(char) >= minimum and password.count(char) <= maximum:
             part1_total += 1
         if password[minimum - 1] == char or password[maximum - 1] == char:
             if not (password[minimum - 1] == char and password[maximum - 1] == char):
                 part2_total += 1
     print(f"Day 2 Part 1: {part1_total}\nDay 2 Part 2: {part2_total}")
