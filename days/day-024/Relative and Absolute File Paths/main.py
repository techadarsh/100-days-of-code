# Absolute Path /directory-1/directory-2/file.txt
# Relative Path ./directory-1/directory-2/file.txt

# Absolute Path
with open("/Users/adarsharma/Desktop/my_file.txt", mode="w") as file:
    contents = file.write("Hello World")

# Relative path
with open("../../../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)