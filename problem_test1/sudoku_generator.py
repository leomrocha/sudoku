#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random 
import math


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
        pass

    def _get_next_zero(self, puzzle):
        """
        returns the coordinates of the next '0' element (to solve)
        """
        D = len(puzzle)
        numbers = range(D)
        for i in numbers:
            for j in numbers:
                if puzzle[i][j] == 0:
                    return (i,j)

    def _get_candidates(self, puzzle, pos):
        """
        Calculates the candidates for a certain position in the puzzle
        @param puzzle
        @param pos: coord (x,y) in puzzle
        """
        i,j = pos
        D = len(puzzle)  #matrix dimension
        N = math.sqrt(D)  #quadrants
        taken = set([r for r in puzzle[i]])
        col = [puzzle[k][j] for k in numbers]
        taken.update(col)
        qr = i/N; qc = j/N
        quadrant = [row[qc:qc+N] for row in puzzle[qr:qr+N]]
        for r in quadrant:
            taken.update(r)
        #avoid duplicates
        taken = list(taken)
        candidates = [i for i in numbers if i not in taken]
        
    def _get_all_candidates(self, puzzle):
        """
        Calculates the candidates for a certain position in the puzzle
        @param puzzle
        """
        D = len(puzzle)  #matrix dimension
        N = math.sqrt(D)  #quadrants
        #all numbers in the selectable set (and also, the index of the rows and columns)
        numbers = range(1, D+1)
        #initial candidates, empty
        candidates = [[[] for j in numbers] for k in numbers]
        #for all columns and rows
        t_puzzle = [[r[i] for r in puzzle] for i in numbers]
        for i in numbers:
            #i == row index
            
            for j in numbers:
                # j == col index
                if puzzle[i][j] == 0:
                    #if the number is not yet defined
                    #get all taken
                    taken = set([r for r in puzzle[i]])
                    col = [puzzle[k][j] for k in numbers]
                    taken.update(col)
                    qr = i/N; qc = j/N
                    quadrant = [row[qc:qc+N] for row in puzzle[qr:qr+N]]
                    for r in quadrant:
                        taken.update(r)
                    #avoid duplicates
                    taken = list(taken)
                    candidates[i][j] = [i for i in numbers if i not in taken]
        return candidates
        
    def _generate_solution(self, dimension):
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
    
    def generate(self, dimension=9, difficulty=27, tries=100):
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
