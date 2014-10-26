#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random 
import math

from file_helpers import *

class SudokuPuzzleGenerator(object):
    """
    Generates sudoku sets
    """
    def __init__(self):
        """
        """
        pass
    
    def to_file(self, puzzle, fname):
        """
        puzzle to save on the file named fname
        @param puzzle puzzle
        @param fname: output file name
        """
        
        f = open(fname, 'w')
        f.writelines(flines)
        f.close()
        
    
    def _generate_puzzle(self, solved_puzzle, difficulty):
        """
        Takes a sudoku solved and takes out to leave only 'difficulty' 
        number of elements visible, the rest is fill to 0
        @param solved_puzzle: the sudoku puzzle completed
        @param difficulty: number of zeros that will be put
        """
        #TODO
        pass

    def _interchange_numbers(self, num1, num2):
        """
        interchanges two numbers, for example, all 1 to 9 and all 9 to 1
        this generates another valid puzzle
        """
        #TODO
        pass

    def _row_swap(self, puzzle, col1, col2):
        """
        Swap two rows
        can only be in the same quadrant
        """
        #TODO
        pass
        
    def _column_swap(self, puzzle, col1, col2):
        """
        Swap two columns
        can only be in the same quadrant
        """
        #TODO
        pass
        
    def _generate_base_and_solve(self, dimension, n):
        """
        
        """
        pass
        
    def _generate_dumb_solution(self, dimension):
        """
        Generates a solved sudoku puzzle
        This algorithm is really DUMB and can fail, but at least is something
        @param dimension: the number of columns and rows in the puzzle
        """
        D = len(puzzle)  #matrix dimension
        N = math.sqrt(D)  #quadrants
        puzzle = [[0 for j in numbers] for k in numbers]
        #all numbers in the selectable set (and also, the index of the rows and columns)
        numbers = range(1, D+1)
        for i in numbers:
            for j in numbers:
                candidates = self._get_candidates(puzzle, (i,j))
                assert len(candidates)>0
                puzzle[i][j] = random.choice(candidates)
                #this WILL fail many times .... the best way to generate is with a solver
        return puzzle
    
    def generate(self, dimension=9, difficulty=27, tries=10000):
        """
        returns a pair of matrices (puzzle, solution)
        @param dimension: the number of columns and rows in the puzzle
        @param difficulty: number of zeros that will be put
        """
        assert math.sqrt(difficulty) <= dimension
        for i in xrange(tries):
            try
                solution = self._generate_solution()
                puzzle = self._generate_puzzle(solution)
                return puzzle, solution
            except:
                #failed generation
                pass
        return None
       

def main(args):
    """
    generates the sudoku files puzzle_X.txt, puzzle_X_solution.txt
    """
    #TODO
    pass
    
if __name__ == '__main__':
    """
    """
    #TODO
    pass
