with open("Day 1 Data 2019.txt") as f:
    data = f.readlines()
total_fuel = 0
total_additional = 0
### Day 1 Part 1 ###
for number in data:
    total_fuel += int(int(number) / 3 - 2)
print(total_fuel)
### Day 2 Part 2 ###
total_2 = 0
for number in data:
    fuel = int(number)
    while True:
        fuel = int(int(fuel / 3) - 2)
        if fuel <= 0:
            break
        total_additional += fuel
print(total_additional)
