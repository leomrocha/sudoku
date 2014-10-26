#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""


import argparse
from sudoku_algorithms import *
from file_helpers import *

SOLVERS = {
              "backtracking": RecursiveBacktrackingSudokuSolver,
              #"generator": SudokuPuzzleGenerator,
}



def main(args):
    parser = argparse.ArgumentParser(description='Sudoku solver')
    parser.add_argument('-f','--csvfile', help='Input CSV file', required=True)
    parser.add_argument('-o','--outcsvfile', help='Input CSV file', required=True)
    args = parser.parse_args()
    puzzle = parse_csv_from_file(args.csvfile)
    solver = RecursiveBacktrackingSudokuSolver()
    solution = solver.solve(puzzle)
    save_puzzle_to_csv(solution, args.outcsvfile)
    #TODO log that file was printed
    

if __name__ == '__main__':
    #TODO
    main(args)
    pass
