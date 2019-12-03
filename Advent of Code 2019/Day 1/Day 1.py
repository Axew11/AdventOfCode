### Day 1: The Tyranny of the Rocket Equation ###
with open("Day 1 Data 2019.txt") as f:
    data = f.readlines()
total_fuel = 0
total_additional = 0
for number in data:
    fuel = int(number)
    total_fuel += int(fuel / 3 - 2)
    while True:
        fuel = int(fuel / 3 - 2)
        if fuel <= 0:
            break
        total_additional += fuel
print(total_fuel)
print(total_additional)
