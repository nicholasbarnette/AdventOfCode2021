def find_bit_prevalence(lines, n):
    prevalence = [0, 0]

    # Iterate through the lines and populate the prevalence array
    for line in lines:
        line = line.strip()
        if n <= len(line):
            try:
                prevalence[int(line[n], base=2)] += 1
            except Exception as e:
                print(e)

    return prevalence


def find_o2gen_rating(lines, n=0):

    # If there is only one line left return that line as the rating
    if len(lines) == 1:
        return lines[0]

    # Find the prevalence of the current bit
    prevalence_matrix = []
    prevalence_matrix = find_bit_prevalence(lines, n)
    most_common_bit = '0' if prevalence_matrix[0] > prevalence_matrix[1] else '1'

    # Iterate a remove all unnecessary values
    pertinent_lines = []
    for line in lines:
        if line[n] == most_common_bit:
            pertinent_lines.append(line)

    # Continue to the next bit
    return find_o2gen_rating(pertinent_lines, n+1)


def find_co2scrubber_rating(lines, n=0):
    # If there is only one line left return that line as the rating
    if len(lines) == 1:
        return lines[0]

    # Find the prevalence of the current bit
    prevalence_matrix = []
    prevalence_matrix = find_bit_prevalence(lines, n)
    least_common_bit = '0' if prevalence_matrix[0] <= prevalence_matrix[1] else '1'

    # Iterate a remove all unnecessary values
    pertinent_lines = []
    for line in lines:
        if line[n] == least_common_bit:
            pertinent_lines.append(line)

    # Continue to the next bit
    return find_co2scrubber_rating(pertinent_lines, n+1)


def calculate_life_support_rating(lines):
    o2gen_rating = find_o2gen_rating(lines, 0)
    co2scrubber_rating = find_co2scrubber_rating(lines, 0)
    return [int(o2gen_rating, base=2), int(co2scrubber_rating, base=2)]
