

# Example seven segment display
#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

def determine_output(line):
    [input_values, output_values] = line.split(' | ')
    input_values = input_values.split(' ')
    output_values = output_values.split(' ')
    # Sanatize values
    for idx, v in enumerate(input_values):
        input_values[idx] = v.strip()
    for idx, v in enumerate(output_values):
        output_values[idx] = v.strip()

    # Create a mapping between proper segment (key) and list of potential values
    number_map = [None] * 10

    # Find the unique numbers
    unknown_5 = []
    unknown_6 = []
    for v in input_values:
        if len(v) == 2:
            # 1
            number_map[1] = v
        elif len(v) == 4:
            # 4
            number_map[4] = v
        elif len(v) == 3:
            # 7
            number_map[7] = v
        elif len(v) == 7:
            # 8
            number_map[8] = v
        elif len(v) == 5:
            # 2/3/5
            unknown_5.append(v)
        elif len(v) == 6:
            # 0/6/9
            unknown_6.append(v)

    # Find the 2/3/5
    # Three is a seven with two differences
    # Two is a four with four differences
    # Five is a four with three differences
    for v in unknown_5:
        s = set(list(number_map[7]))
        s.update(list(v))
        if len(s) - 3 == 2:
            number_map[3] = v
        else:
            s = set(list(number_map[4]))
            s.update(list(v))
            if len(s) - 4 == 3:
                number_map[2] = v
            else:
                number_map[5] = v

    # Find the 0/6/9
    # Nine is a three with one difference
    # Zero is a seven with three differences
    # Six is a seven with five differences
    for v in unknown_6:
        s = set(list(number_map[3]))
        s.update(list(v))
        if len(s) - 5 == 1:
            number_map[9] = v
        else:
            s = set(list(number_map[7]))
            s.update(list(v))
            if len(s) - 3 == 3:
                number_map[0] = v
            else:
                number_map[6] = v

    # Calculate the output
    segments = ""
    for vo in output_values:
        for idx, vi in enumerate(number_map):
            s = set(list(vo))
            init_len = len(s)
            s.update(list(vi))
            if init_len == len(s) and len(vi) == len(vo):
                segments += str(idx)

    return segments
