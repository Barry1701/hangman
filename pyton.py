# file_input = open("read.txt", "r")
# data = file_input.readlines()


# file_input = open("read.txt", "a")
# data = file_input.write("python is amazing.")
# print(data)
file_input = open("read.txt", 'r')
print(file_input.read())

file_input.close()