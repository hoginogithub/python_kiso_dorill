def parse_rec(text, current_depth):
    index = 0
    result_text = []
    current_text = ''
    print(f'len={len(text)}')
    while index < len(text):
        print(f'index={index} check={text[index]} current_depth={current_depth}')
        if text[index] == '(':
            each_index, each_result = parse_rec(text[index + 1:], current_depth + 1)
            if each_index is None:
                return None, result_text
            index += each_index + 2
            result_text += each_result
        elif text[index] == ')':
            if current_depth == 0:
                return None, result_text
            print('break')
            break
        else:
            current_text += text[index]
            index += 1
            print(f'current_text={current_text}')
    else:
        print(f'解析終了 current_depth={current_depth}')
        if current_depth > 0:
            return None, result_text
    
    if len(current_text) > 0:
        result_text += [f'{c}: {current_depth}' for c in current_text]
    
    return index, result_text

def parse(text):
    (read_pos, results) = parse_rec(text, 0)
    print(', '.join(results))
    if read_pos is None:
        print('Unbalanced')
    #else:
    #    print(', '.join(results))

text = input('テキストを入力してください(修了時はquit)')
while text != 'quit':
    print('テキスト解析')
    parse(text)
    text = input('テキストを入力してください(修了時はquit)')
print('PG終了')