def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = reversed(words)
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input_sentence = input("Enter a sentence: ")

print("Reversed sentence:", reverse_sentence(input_sentence))
