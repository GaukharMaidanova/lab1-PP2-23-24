import string

def generate_files():
    alphabet = string.ascii_uppercase
    for letter in alphabet:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write(f"This is the content of {filename}")

if __name__ == "__main__":
    generate_files()
    print("Text files created successfully!")
