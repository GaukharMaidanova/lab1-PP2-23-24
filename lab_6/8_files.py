import os

def delete_file(path):
    try:
        os.remove(path)
        print(f"The file '{path}' has been deleted successfully.")
    except FileNotFoundError:
        print(f"The file '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to delete file '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path of the file to delete: ")
    delete_file(file_path)
