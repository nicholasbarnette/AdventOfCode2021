def calculate_power_consumption(lines):
    # Formatted as an array where the position in the outter array is the bit
    # The spaces in the inner array represents the binary options [0,1]
    power = []

    # Iterate through the lines and populate the power array
    for line in lines:
        line = line.strip()
        for idx, bit in enumerate(line):
            if len(power) <= idx:
                power.append([0, 0])
            try:
                power[idx][int(bit, base=2)] += 1
            except Exception as e:
                print(e)

    # Determine gamma and epsilon
    gamma = ""
    epsilon = ""
    for b in power:
        if b[0] > b[1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return [gamma, epsilon]
