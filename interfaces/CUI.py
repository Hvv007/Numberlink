class CUI:
    def __init__(self, solutions):
        self.solutions = solutions

    def print_solutions(self):
        if len(self.solutions) == 0:
            print('Решений нет!')

        for i in range(len(self.solutions)):
            print(f'\nРешение {i + 1}')
            for line in self.solutions[i]:
                matrix_line = ''
                for el in line:
                    matrix_line += el
                print(matrix_line)
