from pathlib import Path

# Prompt user to enter a filename
filename = input("Please enter file name (without .txt extension): ")
file_path = Path("logs/" + filename + ".txt")

relevant_keys = {'Key.space': ' ', 'Key.backspace': 'BS'}

# Read file contents into contents
file_stream = open(file_path, "r")
char_list = []

if file_stream.mode == "r":
    contents = file_stream.readlines()
    file_stream.close()

for line in contents:
    key = line[25:-1]
    if len(key) == 3:
        #print(key)
        char_list.append(key[1])
    elif key in relevant_keys:
        char_list.append(relevant_keys[key])
print(char_list)
print(''.join(char_list))
    
#