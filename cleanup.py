"""
Version 1.0
Purpose: To organise files within a specific folder
Author: Jack O'Shea
Date: 27/11/2020

"""

"""import os

scan_location = ""
os.chdir(scan_location)
list_of_files = os.listdir()
print(list_of_files)
for filename in list_of_files:
    if filename.endswith(".png"):
        os.rename(f"{scan_location}/{filename}", f"{scan_location}/png/{filename}")
    elif filename.endswith(".pdf"):
        os.rename(f"{scan_location}/{filename}", f"{scan_location}/pdf/{filename}")"""



"""
Version 2.0
Purpose: To organise files within a folder.
Author: Jack O'Shea
Date:27/11/2020

"""
def cleanup(scan_location):
    """This function is used to seperate files in a specific folder into folders based on file types,
    file must be given as a string."""

    
    #Necessary library needed for functions.
    import os
    os.chdir(scan_location)

    #Lists out names of files for debugging purposes.
    list_of_files = os.listdir()
    print(list_of_files)

    #For loop for each file within the specified path
    for filename in list_of_files:
        file, file_extensionraw = os.path.splitext(filename)
        file_extension = file_extensionraw[1:]
        print(file_extension)

        try:
            if os.path.isdir(file_extension):
                print(f"Moving file: {file}")
                os.rename(f"{scan_location}/{filename}", f"{scan_location}/{file_extension}/{filename}")
            elif os.path.isdir(file_extension) == False:
                print(f"Making Directory: {file_extension}")
                os.mkdir(f"{scan_location}/{file_extension}")

                print(f"Moving file: {file}")
                os.rename(f"{scan_location}/{filename}", f"{scan_location}/{file_extension}/{filename}")
        except:
            print("//Skipping Directory or config")

    print("Done")

