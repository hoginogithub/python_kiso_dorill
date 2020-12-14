def sum_rec(int_list, start):
    if start >= len(int_list):
        return 0
    return int_list[start] + sum_rec(int_list, start + 1)

def to_binary_rec(num):
    if num == 0:
        return ''
    return to_binary_rec(num // 2) + str(num % 2)

print(sum_rec([1, 2, 3, 4], 0))
print(to_binary_rec(7))