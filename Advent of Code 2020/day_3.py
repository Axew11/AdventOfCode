with open("input3.txt", 'r') as f:
     map_array = [list(line.strip("\n")) for line in f]
     pointers = [1, 3, 5, 7, 2]
     trees = [0, 0, 0, 0, 0]
     for array in map_array[1:]:
         if array[pointers[0]] == '#':
             trees[0] += 1
         pointers[0] = (pointers[0] + 1) % len(map_array[0])
         if array[pointers[1]] == '#':
             trees[1] += 1
         pointers[1] = (pointers[1] + 3) % len(map_array[0])
         if array[pointers[2]] == '#':
             trees[2] += 1
         pointers[2] = (pointers[2] + 5) % len(map_array[0])
         if array[pointers[3]] == '#':
             trees[3] += 1
         pointers[3] = (pointers[3] + 7) % len(map_array[0])
     i = 1
     while pointers[4] < len(map_array):
         array = map_array[pointers[4]]
         if array[i] == '#':
             trees[4] += 1
         pointers[4] += 2
         i += 1
         if i >= len(array):
             i = 0
         if pointers[4] > len(map_array):
             print(f"Day 3 Part 1: {trees[1]}\nDay 3 Part 2: {trees[0] * trees[1] * trees[2] * trees[3] * trees[4]}")
             break
