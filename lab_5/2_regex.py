import re
with open('lab_5\Row1_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
pattern_1 = r'а{2}б'
pattern_2 = r'а{3}б'
matches_1 = re.findall(pattern_1, text)
matches_2 = re.findall(pattern_2, text)
print(matches_1)
print(matches_2)