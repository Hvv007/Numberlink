import pytest
from src.Field import Field
from src.Point import Point
from src.Solver import Solver
from src.SolutionBuilder import SolutionBuilder


def test_wrong_input():
    with pytest.raises(Exception) as e_info:
        Field.build_field_from_file('test_files/4.txt')
    assert str(e_info.value) == "Встречаются строки различной ширины"

    with pytest.raises(Exception) as e_info:
        Field.build_field_from_file('test_files/5.txt')
    assert str(e_info.value) == "Каждая цифра отличная от нуля должно встречаться ровно 2 раза"

    with pytest.raises(Exception) as e_info:
        Field.build_field_from_file('test_files/6.txt')
    assert str(e_info.value) == "Пустая строка"


def test_neighbors():
    field = Field.build_field_from_file('test_files/3.txt')
    point = Point(2, 2)
    neighbors = field.get_neighbors(point)
    expected_neighbours = [Point(1, 2),  # левый
                           Point(3, 2),  # правый
                           Point(2, 1),  # верхний
                           Point(2, 0)]  # нижний
    assert neighbors == expected_neighbours


def test_solvable():
    field = Field.build_field_from_file('test_files/2.txt')
    solver = Solver(field)
    solutions = solver.solve_puzzle()
    assert len(solutions) > 0


def test_unsolvable():
    field = Field.build_field_from_file('test_files/8.txt')
    solver = Solver(field)
    solutions = solver.solve_puzzle()
    assert not solutions


def test_solution_builder():
    field = Field.build_field_from_file('test_files/1.txt')
    solver = Solver(field)
    solutions = solver.solve_puzzle()
    solutions_builder = SolutionBuilder(solutions, field, -1)
    solutions_pics = solutions_builder.get_lined_solutions()
    assert len(solutions) == len(solutions_pics)


def test_solution_builder_correctness():
    field = Field.build_field_from_file('test_files/9.txt')
    solver = Solver(field)
    solutions = solver.solve_puzzle()
    assert len(solutions) == 1

    solutions_builder = SolutionBuilder(solutions, field, -1)
    solutions_pics = solutions_builder.get_lined_solutions()
    assert len(solutions) == len(solutions_pics)

    print(solutions_pics[0])
    expected_pic = [[' ', '|', ' ', ' ', ' ', '|', ' '],
                    [' ', '1', ' ', '2', ' ', '0', ' '],
                    [' ', ' ', ' ', '|', ' ', '|', ' '],
                    [' ', '2', '-', '0', ' ', '3', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '1', ' ', '3', '-', '0', ' '],
                    [' ', '|', ' ', ' ', ' ', '|', ' ']]
    assert expected_pic == solutions_pics[0]
