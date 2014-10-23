#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""


import argparse
from sudoku_algorithms import *

SOLVERS = {
              "backtracking": RecursiveBacktrackingSudokuSolver,
              #"generator": SudokuPuzzleGenerator,
}





def main(args):
    parser = argparse.ArgumentParser(description='Sudoku solver')
    parser.add_argument('-f','--csvfile', help='Input CSV file', required=True)
    args = parser.parse_args()
    puzzle = parse_csv_from_file(args.csvfile)
    

if __name__ == '__main__':
    pass
