# open, Read and close a file
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Open it using with statement, so that we don't have to worry about closing the file,
# as it will be closed automatically after the block of code is executed
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# Write into a file
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")
#     print(file.read())

#  open file in write mode, actually creates a new file if it doesn't exist, and if it already exists, it will overwrite the existing content
with open("new_file.txt", mode="w") as file:
    contents = file.write("Hello I'm In brand new File")

# append into a file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")