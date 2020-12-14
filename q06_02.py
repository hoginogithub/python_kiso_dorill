with open('q06_02.txt', 'r', encoding='utf_8') as f:
    lines = f.readlines()

chocolate_lines = [line.rstrip('\n') for line in lines if 'チョコレート' in line]
#chocolate_lines = [line for line in lines if 'チョコレート' in line]
print(chocolate_lines)