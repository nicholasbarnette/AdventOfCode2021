import copy


class Expansion:

    def __init__(self, origin, mappings):
        self.origin = origin
        self.current = origin
        self.mappings = {}
        for m in mappings:
            self.mappings[m[0]] = m[1]

    def simulate(self):
        new_string = []
        i = 0
        s = list(self.current)
        while i + 1 < len(s):
            n1 = s[i]
            n2 = s[i+1]
            key = '%s%s' % (n1, n2)
            if key in self.mappings:
                new_string += n1 + self.mappings[key]
            i += 1

        # Append the last character
        new_string += s[i]
        new_string = ''.join(new_string)

        self.current = new_string
        return new_string

    def find_character_prevalence(self):
        prev = {}
        for c in list(self.current):
            if c not in prev:
                prev[c] = 0
            prev[c] += 1
        return prev

    def __str__(self):
        return self.current
