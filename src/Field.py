from src.Point import Point


class Field:
    def __init__(self, field):
        self.numbers = {}
        self.cells = field
        self.height = len(field)
        self.width = len(field[0])

        for y in range(len(field)):
            for x in range(len(field[y])):
                if field[y][x] != '0':
                    if self.numbers.get(field[y][x]) is None:
                        self.numbers[field[y][x]] = [Point(x, y)]
                    else:
                        self.numbers[field[y][x]].append(Point(x, y))

    def __getitem__(self, point):
        return self.cells[point.y][point.x]

    def get_neighbors(self, point):
        neighbors = [Point((point.x - 1) % self.width, point.y % self.height),
                     Point((point.x + 1) % self.width, point.y % self.height),
                     Point(point.x % self.width, (point.y - 1) % self.height),
                     Point(point.x % self.width, (point.y + 1) % self.height)]
        return neighbors

    def is_correct_field(self):
        for number in self.numbers.keys():
            if len(self.numbers[number]) != 2:
                raise ValueError("Каждая цифра отличная от нуля должно встречаться ровно 2 раза")
        if len(self.cells) == 0 or any([True for cell in self.cells if not cell]):
            raise ValueError("Пустая строка")

        first_line_width = len(self.cells[0])
        for line in self.cells:
            if len(line) != first_line_width:
                raise ValueError("Встречаются строки различной ширины")
        return True

    @classmethod
    def build_field_from_file(cls, file_path):
        cells = []
        with open(file_path) as file:
            lines = file.read().split('\n')

            for x in range(len(lines)):
                field_line = []
                items = lines[x].split()
                for y in range(len(items)):
                    field_line.append(items[y])
                cells.append(field_line)

        field = cls(cells)
        if field.is_correct_field():
            return field
