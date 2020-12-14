chocolate_lines = []
with open('q06_02.txt', 'r', encoding='utf_8') as f:
    tmp_line = f.readline().strip('\n')
    while tmp_line:
        # chocolate_lines += [line for line in tmp_line if 'チョコレート' in line]
        # chocolate_lines += [tmp_line for tmp_line in tmp_line if 'チョコレート' in tmp_line]
        if 'チョコレート' in tmp_line:
            chocolate_lines += [tmp_line]
        tmp_line = f.readline().strip('\n')

print(chocolate_lines)
