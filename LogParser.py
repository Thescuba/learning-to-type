from pathlib import Path

# Prompt user to enter a filename
filename = input("Please enter file name (without .txt extension): ")
file_path = Path("logs/" + filename + ".txt")

relevant_keys = {'Key.space': ' ', 'Key.backspace': 'BS', 'Key.enter': '\n', 'Key.shift': 'SHIFT'}

# Read file into contents
file_stream = open(file_path, "r")
char_list = []
filtered_list = []

if file_stream.mode == "r":
    contents = file_stream.readlines()
    file_stream.close()

# Parse contents
char_list = []

for line in contents:
    key = line[25:-1]
    if len(key) == 3:
        char_list.append(key[1])
    elif key in relevant_keys:
        char_list.append(relevant_keys[key])
# print(char_list)
# print(''.join(char_list))
    
#
slow = 0
fast = 0
size = 0
for char in char_list:
    if len(char) == 2:
        fast += 1
        slow = max(0, slow-1)
    if len(char) == 1:
        if slow <size:
            filtered_list[slow] = char
        else:
            filtered_list.append(char)
            size += 1
        slow +=1
        fast +=1

print(''.join(filtered_list))
