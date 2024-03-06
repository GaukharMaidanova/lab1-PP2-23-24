def write_list_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"The list has been written to the file '{filename}' successfully.")
    except IOError:
        print(f"Error writing to the file '{filename}'.")

if __name__ == "__main__":
    data = ['apple', 'banana', 'orange', 'grape']
    filename = input("Enter the filename to write the list to: ")
    write_list_to_file(filename, data)
