class Solver:
    def __init__(self, field):
        self.field = field
        self.parent_paths = [None]
        self.solved_numbers = set()

    def solve_puzzle(self):
        for number in self.field.numbers:
            if number in self.solved_numbers:
                continue
            temp_parent_paths = []
            for parent_path in self.parent_paths:
                temp_parent_paths += self.find_path(self.field.numbers[number][0], self.field.numbers[number][1],
                                                    parent_path, [])
            self.parent_paths = temp_parent_paths
            self.solved_numbers.add(number)
        return self.find_correct_paths(self.parent_paths)

    def find_path(self, current, target, parent_path, path):
        path.append(current)
        if current == target:
            children_paths = SolvePath(parent_path, self.field[target], path)
            if parent_path is not None:
                parent_path.add_children_path(children_paths)
            return [children_paths]

        paths = []
        for neighbor in self.field.get_neighbors(current):
            if target != neighbor and (self.field[neighbor] != '0'
                                       or (parent_path is not None and parent_path.is_point_in_path(neighbor))
                                       or neighbor in path):
                continue
            for current_path in self.find_path(neighbor, target, parent_path, list(path)):
                paths.append(current_path)
        return paths

    def find_correct_paths(self, paths):
        correct_paths = []
        for path in paths:
            if self.is_correct_path(path):
                correct_paths.append(path)
        return correct_paths

    def is_correct_path(self, path):
        count = 0
        while path is not None:
            count += len(path.path)
            path = path.parent_path
        return count == self.field.width * self.field.height


class SolvePath:
    def __init__(self, parent_path, number, path):
        self.parent_path = parent_path
        self.number = number
        self.path = path
        self.children_paths = []

    def add_children_path(self, path):
        self.children_paths.append(path)

    def is_point_in_path(self, point):
        if point in self.path:
            return True
        if self.parent_path is not None and self.parent_path.is_point_in_path(point):
            return True
        return False
