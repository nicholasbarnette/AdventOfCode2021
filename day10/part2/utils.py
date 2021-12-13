import math


def get_character_value(c):
    if c == ')':
        return 3
    elif c == ']':
        return 57
    elif c == '}':
        return 1197
    elif c == '>':
        return 25137
    else:
        return 0


def parse_syntax(line):
    queue = []
    for c in line:
        if c == '<' or c == '(' or c == '{' or c == '[':
            queue.append(c)
        else:
            opening_char = queue.pop()
            if (c == '>' and opening_char != '<') or (c == ')' and opening_char != '(') or (c == '}' and opening_char != '{') or (c == ']' and opening_char != '['):
                return get_character_value(c)

    return 0


def find_incomplete_lines(lines):
    incompletes = []
    for line in lines:
        if parse_syntax(line) == 0:
            incompletes.append(line.strip())
    return incompletes


def complete_line(line):
    queue = []
    # Find sets that need to be completed
    for c in line:
        if c == '<' or c == '(' or c == '{' or c == '[':
            queue.append(c)
        else:
            queue.pop()

    # Calculate value of completion
    complete_sum = 0
    while len(queue) > 0:
        c = queue.pop()
        complete_sum *= 5
        if c == '(':
            complete_sum += 1
        elif c == '[':
            complete_sum += 2
        elif c == '{':
            complete_sum += 3
        else:
            complete_sum += 4

    return complete_sum


def complete_lines(lines):
    values = []
    for line in lines:
        values.append(complete_line(line))
    values.sort()
    return values[math.floor(len(values)/2)]
