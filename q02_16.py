def dropped_list(src_list, i):
    return [x for k, x in enumerate(src_list) if k != i]

def all_permutations(num_list):
    if num_list == []:
        return [[]]
    result_list = []
    for i, elem in enumerate(num_list):
        result_list += list(map(lambda perm: [elem] + perm, all_permutations(dropped_list(num_list, i))))
    return result_list

print(all_permutations([1, 2, 3]))

# test dropped_list
# test_list = [1,2,3]
# print(dropped_list(test_list, 1))