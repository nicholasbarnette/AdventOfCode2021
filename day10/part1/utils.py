
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
