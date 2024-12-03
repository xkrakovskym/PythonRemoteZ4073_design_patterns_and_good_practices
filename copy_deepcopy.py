import copy

original_list = [1, 2, 4, 5, [4, 5, 0]]

shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

original_list[4][1] = 10

print(original_list)
print(shallow_copy)
print(deep_copy)

