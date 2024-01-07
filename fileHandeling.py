# '''Open the file in writing ('w') mode. If the file does not exist, Python will create it for you. If you open an existing file in writing mode, 
# any content that it had contained previously will be deleted.'''

# f = open("file.txt", "w")
# f.write("Hello World !")
# f.close() #It's important to close the file when you're finished with it.

# #If you're interested in adding to an existing file, without deleting its content, you should use the append ('a') mode instead of write.

# f = open("file.txt", "a")
# f.write("Hello World again")
# f.close()

# '''This with keyword allows you to open a file, do operations on it, and automatically close it after the indented code is executed, in this case, 
# reading from the file. Now, we don’t have to call f.close()! You can only access the file object, f, within this indented block.'''



# with open('file.txt', 'r') as f:
#     while True:
#         file_data = f.readline() #readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline.
#         print(file_data)
#         if not file_data:
#             break

camelot_lines = []
with open("file.txt") as f:
    for line in f:
        print(line.strip())
        camelot_lines.append(line.strip())

#print(camelot_lines)