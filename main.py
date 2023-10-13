from tkinter import *
from tkinter import filedialog as fd


def command_list():
    print("Hi, this is a Brace Balance.\n",
    "Please, choose the command:\n",
    "c - select and check '.txt', '.c' or '.cpp' file\n",
    "q - close the program\n")


def search_braces(file):
    while True:
        line = file.readline()
        if not line:
            break
        for i in line:
            if i in '({[)}]':
                brace_string.append(i)
    file.close()


def check_braces():
    is_good = True
    symbols = 0
    for i in brace_string:
        if i not in '({[)}]':
            symbols += 1
    if len(brace_string) == symbols:
        print("BRACES NOT FOUND")
    for i in brace_string:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if len(stack) == 0:
                is_good = False
                break
            brace_open = stack.pop()
            if brace_open == '(' and i == ')':
                continue
            if brace_open == '{' and i == '}':
                continue
            if brace_open == '[' and i == ']':
                continue
            is_good = False
            break
    if is_good and len(stack) == 0:
        if brace_string:
            print("BRACES BALANCED")
    else:
        print("BRACES NOT BALANCED")
    brace_string.clear()
    stack.clear()


if __name__ == '__main__':
    brace_string = []
    stack = []
    wanted_files = (
        ("Text Files", "*.txt"),
        ("C Files", "*.c"),
        ("C++ Files", "*.cpp")
    )
    command_list()
    command = input()
    while command != 'q':
        if command == 'c':
            file_name = fd.askopenfilename(filetypes=wanted_files)
            if file_name:
                file = open(f"{file_name}", "r")
                search_braces(file)
                check_braces()
            command = input()
        else:
            print("Error: unknown command")
            command = input("Enter 'c' - for check file or 'q' for exit\n")
    exit(0)