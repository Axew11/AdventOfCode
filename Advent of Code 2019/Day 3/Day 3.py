### Day 3: Crossed Wires ###
with open("Day 3 Data 2019.txt") as f:
    line = f.read().splitlines()
    wire_1 = line[0].split(',')
    wire_2 = line[1].split(',')
def get_coords(wire):
    x = 0
    y = 0
    steps = 0
    wire_coords = {}
    for direction in wire:
        units = int(direction[1:])
        for i in range(units):
            if direction[0] == 'U':
                y += 1
            elif direction[0] == 'D':
                y -= 1
            elif direction[0] == 'L':
                x -= 1
            else:
                x += 1
            steps += 1
            if (x, y) not in wire_coords:
                wire_coords[(x, y)] = steps
    return wire_coords
wire_1_coords = get_coords(wire_1)
wire_2_coords = get_coords(wire_2)
intersections = set(wire_1_coords.keys())&set(wire_2_coords.keys())
minimum_distance = min([abs(x) + abs(y) for (x,y) in intersections])
minimum_steps = min([wire_1_coords[steps] + wire_2_coords[steps] for steps in intersections])
print(minimum_distance)
print(minimum_steps)