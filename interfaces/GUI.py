from tkinter import Tk, Frame, Canvas, ttk
from tkinter.constants import *


class GUI:
    def __init__(self, solutions):
        self.solutions = solutions
        self.width = 0
        self.height = 0
        if solutions:
            self.puzzle_row_count = len(solutions[0]) // 2
            self.puzzle_column_count = len(solutions[0][0]) // 2
            self.width = self.puzzle_column_count * 50
            self.height = (self.puzzle_row_count + 3) * 50
        self.step = 50
        self.horizontal_line_offset = 25
        self.vertical_line_offset = 75

    def print_solutions(self):
        root = Tk()
        root.title('Numberlink')
        root.geometry(f"{max(self.width, 500)}x{max(self.height, 400)}")

        main_frame = Frame(root)
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=YES)
        vertical_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=vertical_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame = Frame(my_canvas)
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        main_frame.pack(fill=BOTH, expand=YES)

        if len(self.solutions):
            self.paint_solutions(my_canvas)
        else:
            my_canvas.create_text(230, 180, text='Решений нет!', font='Helvetica 20 bold')
        root.mainloop()

    def paint_solutions(self, my_canvas):
        for i, solution in enumerate(self.solutions):
            my_canvas.create_text(self.step + self.width // 2, i * self.height + self.step,
                                  text=f'Решение {i + 1}', font='Helvetica 20 bold')
            for m in range(1, self.puzzle_column_count + 2):
                my_canvas.create_line(self.step * m, i * self.height + 2 * self.step,
                                      self.step * m, i * self.height + 2 * self.step + self.height - 150)
            for m in range(1, self.puzzle_row_count + 2):
                my_canvas.create_line(self.step, i * self.height + self.step * m + self.step,
                                      self.step + self.width, i * self.height + self.step * m + self.step)
            for j, line in enumerate(self.solutions[i]):
                for k, cell in enumerate(line):
                    self.handle_cell(my_canvas, i, k, j, cell)

    def handle_cell(self, canvas, solution_number, matrix_x, matrix_y, cell):
        item = cell
        if item == ' ' or item == '0':
            return
        elif item == '-':
            canvas.create_line(self.horizontal_line_offset + 25 * matrix_x,
                               solution_number * self.height + self.vertical_line_offset + 25 * matrix_y + 25,
                               self.horizontal_line_offset + 25 * (matrix_x + 2),
                               solution_number * self.height + self.vertical_line_offset + 25 * matrix_y + 25)
        elif item == '|':
            canvas.create_line(self.horizontal_line_offset + 25 * matrix_x + 25,
                               solution_number * self.height + self.vertical_line_offset + 25 * matrix_y,
                               self.horizontal_line_offset + 25 * matrix_x + 25,
                               solution_number * self.height + self.vertical_line_offset + 25 * (matrix_y + 2))
        else:
            canvas.create_text(self.step//2 * (matrix_x + 1) + self.horizontal_line_offset,
                               solution_number * self.height + self.step//2 * (matrix_y+1) + self.vertical_line_offset,
                               text=item, font='Helvetica 20 bold')
