import os

def check_path_existence_and_split(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return
    
    print(f"The path '{path}' exists.")

    dirname = os.path.dirname(path)
    filename = os.path.basename(path)

    print(f"Directory portion of the path: {dirname}")
    print(f"Filename portion of the path: {filename}")

if __name__ == "__main__":
    path = input("Enter the path to check: ")
    check_path_existence_and_split(path)
