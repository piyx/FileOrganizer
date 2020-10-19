import os
import shutil
import ext

FileName = "old.py"
ExtensionModule = "ext.py"

paths = {
    "Downloads": "Downloads/",
    "Desktop": "Desktop/",
    "Documents": "Documents/",
    "C Drive": "C:/",
    "D Drive": "D:/"
}


def organizeFiles():
    print("\n\nFolders...\n")
    for key in paths.keys():
        print(key)

    print("\n1-->Choose Path from above\n2-->Set custom path\n")
    choice = int(input("Enter choice:"))
    if choice == 1:
        path = paths[input("\nEnter the folder to be organized:")]

    elif choice == 2:
        path = input("Enter custom path:") + '/'
        print("\n")
    else:
        print("Invalid Choice!")
        return 0

    if (path == "C:/"):
        print("Cannot make changes to system folder")
        return 0
    list_files = os.listdir(path)
    list_extension_names = set(
        [os.path.splitext(file)[1].strip(".") for file in list_files])
    # os.path.splitext returns a tuple with file name and extension split
    #Eg: Filename = Hello.txt
    # -----> os.path.splitext(file) returns ("Hello", ".txt")

    # Create New Folders
    for extension in list_extension_names:
        folder_name = ext.foldername(extension)
        if(folder_name == None):  # Folder_name = None --> Its a folder
            continue  # No need to make new folder
        if not os.path.exists(path + folder_name):
            os.makedirs(path + folder_name)

    # Move Files To Respective Folder
    for file in list_files:
        if(file == FileName or file == ExtensionModule):
            continue
        file_extension = os.path.splitext(file)[1].strip(".")
        folder_name = ext.foldername(file_extension)
        if(folder_name == None):
            continue
        if not os.path.exists(path + folder_name + "/" + file):
            shutil.move(path + file, path + folder_name + "/" + file)
            print("Moved {} to {}".format(file, path + folder_name))
    return 0


def main():
    print("\n\n1:Organize Files\n2:Backup To Drive\n3:Rename Unordered Files")
    choice = int(input("\nEnter choice:"))

    if(choice == 1):
        organizeFiles()
    elif(choice == 2):
        print("Backup feature not available yet")
    elif(choice == 3):
        print("Feature to be added soon")
    else:
        print("\nInvalid Choice")


if __name__ == "__main__":
    main()
