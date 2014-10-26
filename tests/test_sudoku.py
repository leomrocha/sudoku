#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import unittest
import random
import math
import copy

from sudoku.sudoku_algorithms import *


VALID_PUZZLE = [
                    [0,3,5,2,9,0,8,6,4],
                    [0,8,2,4,1,0,7,0,3],
                    [7,6,4,3,8,0,0,9,0],
                    [2,1,8,7,3,9,0,4,0],
                    [0,0,0,8,0,4,2,3,0],
                    [0,4,3,0,5,2,9,7,0],
                    [4,0,6,5,7,1,0,0,9],
                    [3,5,9,0,2,8,4,1,7],
                    [8,0,0,9,0,0,5,2,6],
                ]
                
INVALID_PUZZLE = [
                    [0,3,5,2,9,0,8,6,9],
                    [0,8,2,4,1,0,7,0,3],
                    [7,6,4,3,8,0,0,9,0],
                    [2,1,8,7,3,9,0,4,0],
                    [0,0,0,8,0,4,2,3,0],
                    [0,4,3,0,5,2,9,7,0],
                    [4,0,6,5,7,1,0,0,9],
                    [3,5,9,0,2,8,4,1,7],
                    [8,0,0,9,0,0,5,2,6],
                ]
                
VALID_SOLUTION = [
                    [1,3,5,2,9,7,8,6,4],
                    [9,8,2,4,1,6,7,5,3],
                    [7,6,4,3,8,5,1,9,2],
                    [2,1,8,7,3,9,6,4,5],
                    [5,9,7,8,6,4,2,3,1],
                    [6,4,3,1,5,2,9,7,8],
                    [4,2,6,5,7,1,3,8,9],
                    [3,5,9,6,2,8,4,1,7],
                    [8,7,1,9,4,3,5,2,6],
                ]



class TestSudoku(unittest.TestCase):
    """
    RecursiveBacktrackingSudokuSolver test suite.
    Main focus on testing the helping and evaluation functions
    """ 
    def setUp(self):
        self.solver = Sudoku()
 
    def tearDown(self):
        pass
        
    def test__accept(self):
        """
        """
        D = len(VALID_PUZZLE)
        self.solver.D = D
        #sum to check
        self.solver.S = sum(range(1, D+1))
        #number of quadrant rows and columns
        self.solver.N = int(math.sqrt(D))
        self.assertFalse(self.solver._accept(VALID_PUZZLE))
        self.assertTrue(self.solver._accept(VALID_SOLUTION))
        #TODO search for weird cases
        
        
    def test_not_accept(self):
        """
        tests valid puzzles that are not yet completed, should always not accept
        """
        #for some dimensions (from 4x4 -> 25x25)
        for d in range(2, 5):
            D = d**2
            self.solver.D = D
            #sum to check
            self.solver.S = sum(range(1, D+1))
            #number of quadrant rows and columns
            self.solver.N = int(math.sqrt(D))
            #for zero puzzle
            zero_puzzle = self._create_zero_puzzle(D)
            self.assertFalse(self.solver._accept(zero_puzzle))
            #for no zero in puzzle (is most likely invalid, anyways it is useful for testing)
            no_zero_puzzle = [[random.randint(1,D) for j in range(D)] for i in range(D)]
            candidates  = range(1, D+1)
            for r in range(D):
                for c in range(D):
                    #generate a valid column, row and quadrant for the given position
                    vpos_puzzle = self._generate_valid_position(D, (r,c))
                    #
                    self.assertFalse(self.solver._accept(vpos_puzzle))
 
    def test__reject(self):
        """
        """
        #TODO
        pass
        
    def test_not_reject(self):
        """
        """
        for d in range(2, 5):
            D = d**2
            self.solver.D = D
            #sum to check
            self.solver.S = sum(range(1, D+1))
            #number of quadrant rows and columns
            self.solver.N = int(math.sqrt(D))
            #for zero puzzle
            zero_puzzle = self._create_zero_puzzle(D)
            self.assertFalse(self.solver._reject(zero_puzzle))
            #for no zero in puzzle (is most likely invalid, anyways it is useful for testing)
            no_zero_puzzle = [[random.randint(1,D) for j in range(D)] for i in range(D)]
            candidates  = range(1, D+1)
            for r in range(D):
                for c in range(D):
                    #generate a valid column, row and quadrant for the given position
                    vpos_puzzle = self._generate_valid_position(D, (r,c))
                    #
                    self.assertFalse(self.solver._reject(vpos_puzzle))
        
    def test__get_next_zero(self):
        """
        Checks that the function returns the next zero to evaluate (by row, column)
        Evaluation is left to right up to down
        """
        #for some dimensions (from 4x4 -> 25x25)
        for d in range(2, 5):
            D = d**2
            #all rows
            for r in range(D):
                #columns
                for c in range(D):
                    #non empty (and maybe non valid) puzzle 
                    puzzle = [[random.randint(1,D) for j in range(D)] for i in range(D)]
                    #r,c = 0
                    puzzle[r][c] = 0
                    #get sudoku puzzle dimensions
                    self.solver.D = len(puzzle)
                    #sum to check
                    self.solver.S = sum(range(1, self.solver.D+1))
                    #number of quadrant rows and columns
                    self.solver.N = int(math.sqrt(self.solver.D))
                    self.assertEquals( (r,c), self.solver._get_next_zero(puzzle))
        
    def test__get_candidates(self):
        """
        Evaluates that the candidates obtained for each coordinate pair are correct.
        """
        #for some dimensions (from 4x4 -> 25x25), bigger has not much sense and will take too long
        #d is number of quadrants
        for d in range(2, 5):
            D = d**2  #dimension
            self.solver.D = D
            self.solver.S = sum(range(1, D+1))  #sum to check
            self.solver.N = int(math.sqrt(D))  #number of quadrants, rows and columns
            #for zero puzzle
            zero_puzzle = self._create_zero_puzzle(D)
            #for no zero in puzzle (is most likely invalid, anyways it is useful for testing)
            no_zero_puzzle = [[random.randint(1,D) for j in range(D)] for i in range(D)]
            candidates  = range(1, D+1)
            for r in range(D):
                for c in range(D):
                    #evaluate empty
                    self.assertEquals(candidates, self.solver._get_candidates(zero_puzzle, (r,c)))
                    #evaluate full
                    self.assertEquals(0, len(self.solver._get_candidates(no_zero_puzzle, (r,c))))
                    #generate a valid column, row and quadrant for the given position
                    vpos_puzzle = self._generate_valid_position(D, (r,c))
                    #for this generated valid position and for 1 to D start cleaning and find candidates
                    #covers the spectrum of possibilities for the whole puzzle position set (not the whole integer space)
                    for i in range(D):
                        missing, epos_puzzle = self._empty_numbers_for_pos(copy.deepcopy(vpos_puzzle), i, (r,c))
                        pos_candidates = self.solver._get_candidates(epos_puzzle, (r,c))
                        self.assertEquals(set(missing), set(pos_candidates))
                        
    def test__get_all_candidates(self):
        """
        """
        for d in range(2, 5):
            D = d**2
            self.solver.D = D
            #sum to check
            self.solver.S = sum(range(1, D+1))
            #number of quadrant rows and columns
            self.solver.N = int(math.sqrt(D))
            #for zero puzzle
            zero_puzzle = self._create_zero_puzzle(D)
            candidates  = set(range(1, D+1))
            missing = self.solver._get_all_candidates(zero_puzzle)
            for r in range(D):
                for c in range(D):
                    self.assertEquals(set(missing[r][c]), candidates)
        #see other cases although they should be covered by the test__get_candidates
        
    ############################################################################
    #helper methods
    ############################################################################
    def _create_zero_puzzle(self, D):
        """
        Creates a DxD  matrix of zeros
        """
        puzzle = [[0 for j in range(D)] for i in range(D)]
        return puzzle
    
    def _generate_valid_position(self, D, pos):
        """
        The generated puzzle might not be valid, the goal is to be able to test a position only
        @param: D dimension of the puzzle
        @param: pos = (i,j) position in the matrix that should contain a valid row column and quadrant
        @return: a maybe invalid puzzle where the given position is valid
        """
        puzzle = self._create_zero_puzzle(D)
        x,y = pos
        N = int(math.sqrt(D))
        qr,qc = x/N, y/N
        #fill quadrant
        qcandidates = range(1,D+1)
        random.shuffle(qcandidates)
        #quadrant = [row[qc*N:(qc+1)*N] for row in puzzle[qr*N:(qr+1)*N]]
        for r in range(qr*N, (qr+1)*N):
            for c in range(qc*N, (qc+1)*N):
                puzzle[r][c] = qcandidates.pop()
        #fill row
        candidates = range(1,D+1)
        random.shuffle(candidates)
        rcandidates = [i for i in candidates if i not in puzzle[x]]
        for i in range(D):
            if puzzle[x][i] == 0:
                puzzle[x][i] = rcandidates.pop()
        #fill column
        t_puzzle = [[r[i] for r in puzzle] for i in range(D)]
        random.shuffle(candidates)
        ccandidates = [i for i in candidates if i not in t_puzzle[y]]
        for i in range(D):
            if puzzle[i][y] == 0:
                puzzle[i][y] = ccandidates.pop()
        return puzzle
 
    def _empty_numbers_for_pos(self, puzzle, n, pos):
        """
        takes out n numbers from the column, row and quadrant, the resulting puzzle
        contains a 0 in the position and 
        @param puzzle: given puzzle to empty (given position must be already solved)
        @param n: number of elements to empty from the row, column and quadrant
        @param pos: (x,y) position in the puzzle where will be a zero
        @return missing,puzzle where missing is the list of numbers missing in that point
        """
        x,y = pos
        D = len(puzzle)
        missing = set([random.randint(1,D) for i in range(n-1) if n>0])
        missing.add(puzzle[x][y])
        missing = list(missing)
        #empties from the whole puzzle the selected numbers, this is easy and 
        #has the desired result in the given position
        for r in puzzle:
            for m in missing:
                if m in r:
                    r[r.index(m)] = 0
        return missing, puzzle
 
    def _empty_random_positions(self, puzzle, n, max_tries=1000):
        """
        empties 'n' positions from the given puzzle
        @param puzzle: puzle to use
        @param n: number of elements to put in 0
        @param max_tries: maximum number of loops that will try
        
        """
        #TODO implement a better algorithm that can not choose a position that is already in 0
        D = len(puzzle)
        counter = 0;
        emptied = 0;
        for i in range(max_tries):
            x,y = random.randint(0,D-1), random.randint(0,D-1)
            if puzzle[x][y] != 0:
                counter+=1
                puzzle[x][y] = 0
            if counter >= n:
                break
        return puzzle


class TestRecursiveBacktrackingSudokuSolver(TestSudoku):
    """
    RecursiveBacktrackingSudokuSolver test suite.
    Main focus on testing the helping and evaluation functions
    """ 
    def setUp(self):
        self.solver = RecursiveBacktrackingSudokuSolver()
 
    def tearDown(self):
        pass
        
    def test_solve(self):
        """
        """
        #test a valid solution
        solution = self.solver.solve(VALID_PUZZLE)
        self.assertEquals(9, self.solver.D)
        self.assertEquals(3, self.solver.N)
        self.assertEquals(45, self.solver.S)
        self.assertIsNotNone(solution)
        self.assertEquals(VALID_SOLUTION, solution)
        #test an invalid solution
        in_solution = self.solver.solve(INVALID_PUZZLE)
        self.assertEquals(9, self.solver.D)
        self.assertEquals(3, self.solver.N)
        self.assertEquals(45, self.solver.S)
        self.assertIsNone(in_solution)
        #TODO should test with a DB of cases
        
        
###In progress
class TestSudokuPuzzleGenerator(TestSudoku):
    """
    """
    def setUp(self):
        self.solver = SudokuPuzzleGenerator()
 
    def tearDown(self):
        pass
    
    def test__generate_puzzle(self):
        """
        """
        #TODO
        pass

    def test__swap_numbers(self):
        """
        """
        #TODO
        pass

    def test__row_swap(self):
        """
        """
        #TODO
        pass
        
    def test__column_swap(self):
        """
        """
        #TODO
        pass
        
    def test__generate_valid_position(self):
        """
        """
        #TODO
        pass
        
    def test__generate_base_and_solve(self):
        """
        
        """
        #TODO
        pass
        
    def test__generate_dumb_solution(self):
        """
        """
        #TODO
        pass
    
    def test_generate(self):
        """
        """
        #TODO
        pass

if __name__ == '__main__':
    unittest.main()
