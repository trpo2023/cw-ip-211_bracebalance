from tkinter import *
from tkinter import filedialog as fd

root = Tk()
root.title("Brace Balance")
root.geometry("500x300")
root.resizable(False, False)
root.configure(background="black")

def run():
    draw_widgets()
    root.mainloop()

def draw_widgets():
    label_header = Label(root, text="Brace Balance", font="Ubuntu 20",
                         bg="black", fg="white")
    label_header.place(x=20, y=20)
    label_check = Label(root, text="Check:", font="Ubuntu 20",
                        bg="black", fg="white")
    label_check.place(x=280, y=20)

    button_load = Button(root, width=20, height=2, text="Check File", relief=FLAT,
                    bg="white", command=check_file)
    button_load.place(x=20, y=80)
    button_exit = Button(root, width=20, height=2, text="Exit", relief=FLAT,
                    bg="white", command=close_program)
    button_exit.place(x=20, y=140)

def close_program():
    exit(0)
def check_file():
    label_result = Label(root, font="Ubuntu 20", bg="black", fg="white")
    label_result.place(x=280, y=80)
    wanted_files = (
        ("Text Files", "*.txt"),
        ("C Files", "*.c")
    )
    file_name = fd.askopenfilename(filetypes=wanted_files)
    if file_name:
        file = open(f"{file_name}", "r")

    brace_string = []
    stack = []
    is_good = True
    def search_braces():
        while True:
            line = file.readline()
            if not line:
                break
            for i in line:
                if i in '({[)}]':
                    brace_string.append(i)
        file.close()

    def check_braces(is_good):
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
            label_result.configure(text="BRACES BALANCED")
        else:
            label_result.configure(text="BRACES NOT BALANCED")

    search_braces()
    check_braces(is_good)

if __name__ == '__main__':
    run()
