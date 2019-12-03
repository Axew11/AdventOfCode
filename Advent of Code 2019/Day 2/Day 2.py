### Day 2: 1202 Program Alarm ###
intcode_data = [int(x) for x in open('Day 2 Data 2019.txt').read().split(',')]
def test(noun, verb):
    intcode = [x for x in intcode_data]
    index = 0
    intcode[1] = noun
    intcode[2] = verb
    while True:
        opcode = intcode[index]
        value_1 = intcode[index + 1]
        value_2 = intcode[index + 2]
        position = intcode[index + 3]
        if opcode == 1:
            intcode[position] = intcode[value_1] + intcode[value_2]
            index += 4
        elif opcode == 2:
            intcode[position] = intcode[value_1] * intcode[value_2]
            index += 4
        else:
            break
    return intcode[0]
print(test(12, 2))
for i in range(100):
    for j in range(100):
        if test(i, j) == 19690720:
            print(i * 100 + j)
            break