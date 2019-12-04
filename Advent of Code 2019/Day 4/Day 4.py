### Day 4: Secure Container ###
answer_1 = 0
answer_2 = 0
range_values = [int(x) for x in open("Day 4 Data 2019.txt").read().split('-')]
for value in range(range_values[0], range_values[1]):
    valid = True
    digits = [int(i) for i in str(value)]
    if digits != sorted(digits):
        continue
    for number in digits:
        if digits.count(number) >= 2 and valid:
            answer_1 += 1
            valid = False
        if digits.count(number) == 2:
            answer_2 += 1
            break
print(answer_1, answer_2)