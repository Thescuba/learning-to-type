from pathlib import Path

# Prompt user to enter a filename
filename = input("Please enter file name (without .txt extension): ")
file_path = Path("logs/" + filename + ".txt")

relevant_keys = {'Key.space': ' ', 'Key.backspace': 'BS', 'Key.enter': '\n'}

# Read file into contents
file_stream = open(file_path, "r")
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
print(''.join(char_list))
    
#