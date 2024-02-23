import re
with open('lab_5\Row1_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = r'[А-Я]+[а-я]+'
matches = re.findall(pattern, text)
print(matches)