import re
with open('lab_5\Row1_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

def snake_to_camel(snake_case):
    words = re.split('_+', snake_case)
    camel_case = ''.join(word.capitalize() for word in words)
    return camel_case

pattern = r'\b[а-яА-Я]+_[а-яА-Я]+\b'
camel_text = re.sub(pattern, lambda x: snake_to_camel(x.group()), text)
print(camel_text)