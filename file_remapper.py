import os

def file_jumbler(file_name: str) -> None:
    jumbled_file_name = file_name + "jumbled"
    os.rename(file_name, jumbled_file_name)
    print(F"Jumbled {file_name} into {jumbled_file_name}")

def file_unjumbler(file_name: str) -> None:
    jumbled_file_name = file_name + "jumbled"
    os.rename(jumbled_file_name, file_name)
    print(F"Unjumbled {jumbled_file_name} into {file_name}")

def _name_helper(file_name: str) -> str:
    return file_name.rstrip()

operation = input("Operation (j/u): ")
input_file = input("Path to file: ")
file = open(input_file)

if operation == 'j':
    for file_name in file:
        file_jumbler(_name_helper(file_name))

if operation == 'u':
    for file_name in file:
        file_unjumbler(_name_helper(file_name))
