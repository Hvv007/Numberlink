class CUI:
    def __init__(self, solutions):
        self.solutions = solutions

    def print_solutions(self):
        if len(self.solutions) == 0:
            print('No solutions')

        for i in range(len(self.solutions)):
            print(f'Solution #{i + 1}')
            for line in self.solutions[i]:
                matrix_line = ''
                for el in line:
                    matrix_line += el[0]
                print(matrix_line)
