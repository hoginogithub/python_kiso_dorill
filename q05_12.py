import re

def count_dogs(text):
    # inu_pattern = r'(?<!狂犬|猛犬|野良犬)犬'
    # inu_pattern = r'(?<!.狂|.猛|野良)犬'
    inu_pattern = r'(?<!狂|猛)犬'
    # inu_pattern = r'犬'
    return len(re.findall(inu_pattern, text))

txt1 = '狂犬'
print(count_dogs(txt1))

txt2 = '犬'
print(count_dogs(txt2))

txt3 = '吾輩は犬である'
print(count_dogs(txt3))

txt4 = '吾輩は狂犬である'
print(count_dogs(txt4))