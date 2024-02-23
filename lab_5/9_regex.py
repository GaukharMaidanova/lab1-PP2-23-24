import re
with open('lab_5\Row1_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = r'(?<!^)(?=[A-Z])'

spaced_text = re.sub(pattern, ' ', text)

print(spaced_text)
