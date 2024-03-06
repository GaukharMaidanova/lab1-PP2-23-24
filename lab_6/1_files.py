import os

def list_directories_and_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

def list_all_directories_and_files(path):
    for root, dirs, files in os.walk(path):
        print(f"Current directory: {root}")
        print("Directories:")
        for directory in dirs:
            print(os.path.join(root, directory))
        
        print("\nFiles:")
        for file in files:
            print(os.path.join(root, file))
        
        print()

if __name__ == "__main__":
    path = input("Enter the path: ")
    if os.path.exists(path):
        print("\nListing directories and files:")
        list_directories_and_files(path)
        
        print("\nListing all directories and files:")
        list_all_directories_and_files(path)
    else:
        print("The specified path does not exist.")
