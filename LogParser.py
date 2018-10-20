from pathlib import Path

# Prompt user to enter a filename
filename = input("Please enter file name (without .txt extension): ")
file_path = Path("logs/" + filename + ".txt")

relevant_keys = {'Key.space': ' ', 'Key.backspace': 'BS', 'Key.enter': '\n'}

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
    
# Filter sentences
wrong_letters = dict()
# err_list = []
slow = 0
size = 0
prev_char = ''
for char in char_list:
    if char == 'BS' or char == '\n':
        slow = max(0, slow-1)
        # err_list.append(filtered_list[slow])
    if len(char) == 1:
        if slow < size:
            filtered_list[slow] = char
            if prev_char == 'BS':
                if char in wrong_letters:
                    wrong_letters[char] = wrong_letters[char] + 1
                else:
                    wrong_letters[char] = 1
            # GETS THE LETTER THAT YOU TYPED IN WRONG E.G. helkoBSBSlo -> {'k' : 1}
            # if size - slow == 1:
            #     letter = err_list[0]
            #     if letter in wrong_letters:
            #         wrong_letters[letter] = wrong_letters[letter] + 1
            #     else:
            #         wrong_letters[letter] = 1
            #     err_list.clear()
        else:
            filtered_list.append(char)
            size += 1
        slow +=1
    prev_char = char

print(wrong_letters)
raw_sentences = ''.join(char_list)
filtered_sentences = ''.join(filtered_list)