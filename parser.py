class Parser:
    def __init__(self, file_name):
        self._lines = []

        with open(file_name, 'r') as infile:
            lines = infile.readlines()
            for line in lines:
                line = line.rstrip()
                self._lines.append([int(num) for num in line.split(' ')])  # split numbers into a list by line

        self._pairs = self._parse_pairs()  # extract tuple list
        if len(lines) == 2:  # initializes the physical memory via text file; otherwise, it's something else.
            self._triples = self._parse_triples()  # extract triple list

    def get_pairs(self):
        return list(self._pairs)

    def get_triples(self):
        return list(self._triples)

    def _parse_pairs(self, lines=None):
        if self._lines_used(lines):
            lines = self._lines

        first_line = lines[0]

        return [(first_line[i], first_line[i+1]) for i in range(0, len(first_line), 2)]

    def _parse_triples(self, lines=None):
        if self._lines_used(lines):
            lines = self._lines

        second_line = lines[1]

        return [(second_line[i], second_line[i+1], second_line[i+2]) for i in range(0, len(second_line), 3)]

    @staticmethod
    def _lines_used(lines):
        if lines is None:
            return True
        return False


if __name__ == '__main__':
    p = Parser("pm.txt")
