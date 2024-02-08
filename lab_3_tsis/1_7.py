def word_frequency(text):
    words = text.split()
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

input_text = input()
print(word_frequency(input_text))
