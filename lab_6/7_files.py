def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"One of the files '{source_file}' or '{destination_file}' does not exist.")
    except IOError:
        print(f"Error copying contents from '{source_file}' to '{destination_file}'.")

if __name__ == "__main__":
    source_file = input("Enter the source filename: ")
    destination_file = input("Enter the destination filename: ")
    copy_file(source_file, destination_file)
