from pathlib import Path

# Prompts user to enter a filename
filename = input("Please enter file name (without .txt extension): ")

# Create file directory
file_path = Path("logs/" + filename + ".txt")
print(file_path)