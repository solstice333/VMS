class Parser:
    def __init__(self, file_name):
        self._lines = []

        with open(file_name, 'r') as infile:
            for line in infile:
                if line[-1] == '\n': #remove new lines
                    line = line[:-1]
                self._lines.append( [int(num) for num in line.split(' ')] ) #split numbers into a list by line

        self._tuples = self._parse_tuples() #extract tuple list
        self._triples = self._parse_triples() #extract triple list

        print(self._tuples)
        print(self._triples)

    def _parse_tuples(self, lines = None):
        if (self._lines_used(lines)):
            lines = self._lines

        first_line = lines[0]

        s_list = [first_line[element] for element in range(0, len(first_line), 2)]
        f_list = [first_line[element] for element in range(1, len(first_line), 2)]

        return list(zip(s_list, f_list))

    def _parse_triples(self, lines = None):
        if (self._lines_used(lines)):
            lines = self._lines

        second_line = lines[1]

        p_list = [second_line[element] for element in range(0, len(second_line), 3)]
        s_list = [second_line[element] for element in range(1, len(second_line), 3)]
        f_list = [second_line[element] for element in range(2, len(second_line), 3)]

        return list(zip(p_list, s_list, f_list))

    def _lines_used(self, lines):
        if lines is None:
            return True
        return False

if __name__ == '__main__':
    Parser("input.txt")