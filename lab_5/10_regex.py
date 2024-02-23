import re
with open('lab_5\Row1_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[А-Я])', '_', camel_case).lower()
    return snake_case

pattern = r'[а-я]+(?:[А-Я][а-я]*)+'
snake_text = re.sub(pattern, lambda x: camel_to_snake(x.group()), text)
print(snake_text)