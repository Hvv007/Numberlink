class SolutionBuilder:
    def __init__(self, solutions, field, output_number):
        self.solutions = solutions
        self.field = field.cells
        self.height = field.height
        self.width = field.width
        self.output_number = output_number if output_number != -1 else len(self.solutions)

    def get_lined_solutions(self):
        solutions_pics = []
        for i in range(min(self.output_number, len(self.solutions))):
            path = self.solutions[i]
            solve_matrix = [[' ' for _ in range(self.width * 2 + 1)] for _ in range(self.height * 2 + 1)]
            self.add_numbers(self.field, solve_matrix)
            while path is not None:
                self.add_lines(path, solve_matrix)
                path = path.parent_path
            solutions_pics.append(solve_matrix)
        return solutions_pics

    def add_lines(self, path, solve_matrix):
        for i in range(len(path.path) - 1):
            if path.path[i].y == path.path[i + 1].y:
                if abs(path.path[i].x - path.path[i + 1].x) == self.width - 1:
                    solve_matrix[path.path[i].y * 2 + 1][0] = '-'
                    solve_matrix[path.path[i].y * 2 + 1][-1] = '-'
                elif path.path[i].x > path.path[i + 1].x:
                    solve_matrix[path.path[i].y * 2 + 1][path.path[i].x * 2] = '-'
                elif path.path[i].x < path.path[i + 1].x:
                    solve_matrix[path.path[i].y * 2 + 1][path.path[i].x * 2 + 2] = '-'
            if path.path[i].x == path.path[i + 1].x:
                if abs(path.path[i].y - path.path[i + 1].y) == self.height - 1:
                    solve_matrix[0][path.path[i].x * 2 + 1] = '|'
                    solve_matrix[-1][path.path[i].x * 2 + 1] = '|'
                elif path.path[i].y > path.path[i + 1].y:
                    solve_matrix[path.path[i].y * 2][path.path[i].x * 2 + 1] = '|'
                elif path.path[i].y < path.path[i + 1].y:
                    solve_matrix[path.path[i].y * 2 + 2][path.path[i].x * 2 + 1] = '|'

    @staticmethod
    def add_numbers(starting_matrix, solve_matrix):
        for i, line in enumerate(starting_matrix):
            for j, cell in enumerate(line):
                solve_matrix[i * 2 + 1][j * 2 + 1] = cell
