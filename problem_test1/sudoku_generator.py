#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random 


class SudokuGenerator(object):
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
        pass
        
    def _generate_solution(self, dimension):
        """
        Generates a solved sudoku puzzle
        @param dimension: the number of columns and rows in the puzzle
        """
        pass
    
    def generate(self, dimension=9, difficulty=27):
        """
        returns a matrix  pair: 
        @param dimension: the number of columns and rows in the puzzle
        @param difficulty: number of zeros that will be put
        """
        assert math.sqrt(difficulty) <= dimension
        solution = self._generate_solution()
        puzzle = self._generate_puzzle(solution)
        return puzzle, solution
       

def main(args):
    pass
    
def main(args):
    """
    generates the sudoku files puzzle_X.txt, puzzle_X_solution.txt
    """
    pass
    
if __name__ == '__main__':
    pass
