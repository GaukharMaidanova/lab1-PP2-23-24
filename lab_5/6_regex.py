import re
with open('lab_5\Row1_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = r'[ ,.]'
matches_1 = re.sub(pattern, ":", text)
print(matches_1)
