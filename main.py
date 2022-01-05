import argparse
from src.Solver import Solver
from interfaces.CUI import CUI
from interfaces.GUI import GUI
from src.Field import Field
from src.SolutionBuilder import SolutionBuilder


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Numberlink', add_help=False,
                                     usage='main.py [OPTIONS] FILE_NAME')
    parser.add_argument("-h", "--help", help="показывает это сообщение", action="help")
    parser.add_argument("-g", "--gui", help="вывод в gui-интерфейс, а не в консоль", action="store_true")
    parser.add_argument("-n", "--number", help="сколько первых решений вывести", type = int, default=-1)
    parser.add_argument("FILE_NAME", help="название файла")
    args = parser.parse_args()
    gui_flag = args.gui
    filename = args.FILE_NAME
    number = args.number
    field = Field.build_field_from_file(filename)
    solver = Solver(field)
    solutions = solver.solve_puzzle()
    solutions_builder = SolutionBuilder(solutions, field, number)
    solutions_pics = solutions_builder.get_lined_solutions()
    interface = GUI(solutions_pics) if gui_flag else CUI(solutions_pics)
    interface.print_solutions()



