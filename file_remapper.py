import os


def _name_helper(file_name: str) -> str:
    return file_name.rstrip()

def file_jumbler(file_name: str) -> None:
    file_name = _name_helper(file_name)
    jumbled_file_name = file_name + "jumbled"
    os.rename(file_name, jumbled_file_name)
    print(F"Jumbled {file_name} into {jumbled_file_name}")

def file_unjumbler(file_name: str) -> None:
    file_name = _name_helper(file_name)
    jumbled_file_name = file_name + "jumbled"
    os.rename(jumbled_file_name, file_name)
    print(F"Unjumbled {jumbled_file_name} into {file_name}")
