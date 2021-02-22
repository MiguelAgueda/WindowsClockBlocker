import file_remapper as file_tools
import scheduler
import os

cwd = os.getcwd()
input_file_path = cwd + "\\file_list.txt"
state_file_path = cwd + "\\state.txt"

program_files = open(input_file_path)
state_file = open(state_file_path, 'r')

def files_not_jumbled():
    # Read in the file
    state = state_file.read()
    if state == 'j':
        return False
    elif state == 'u':
        return True


play_time = scheduler.time_to_play()
print(F"Time to play? {play_time}")

if not play_time and files_not_jumbled():  # Jumble file names.
    for file_name in program_files:
        file_tools.file_jumbler(file_name)
        with open(state_file_path, 'w') as file:
            file.write('j')

elif play_time and not files_not_jumbled():
    for file_name in program_files:
        file_tools.file_unjumbler(file_name)
        with open(state_file_path, 'w') as file:
            file.write('u')
