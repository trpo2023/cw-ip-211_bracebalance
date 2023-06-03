file = open("c_program.c", "r")

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
        print("BRACES BALANCED")
    else:
        print("BRACES NOT BALANCED")

if __name__ == '__main__':
    search_braces()
    check_braces(is_good)
