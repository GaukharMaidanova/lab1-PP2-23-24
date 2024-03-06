def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"The number of lines in the file '{filename}' is: {line_count}")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except IOError:
        print(f"Error reading file '{filename}'.")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    count_lines(filename)
