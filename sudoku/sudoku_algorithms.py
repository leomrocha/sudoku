# -*- coding: utf-8 -*-
"""
Sudoku solver algorithms
"""

import copy
import math
import random


class Sudoku(object):
    """
    Defines common functions for solvers and generators
    """
    def __init__(self):
        """
        """
        #dimension
        self.D = 0
        #quadrant dimension && n# of quadrants
        self.N = 0 
        #row sum == column sum == quadrant sum
        self.S = 0
        
    def _accept(self, puzzle):
        """
        checks that the puzzle is solved, if so, returns True, else returns False
        S is the sum
        D the dimension (number of columns and rows)
        N: number of quadrant rows and columns
        assumes that the puzzle is valid (dimensions and values in the cells)
        """
        #check rows
        for r in puzzle:
            if sum(r) != self.S:
                return False
        #check columns (obtain by transposing the matrix)
        t_puzzle = [[r[i] for r in puzzle] for i in range(self.D)]
        for c in t_puzzle:
            if sum(c) != self.S:
                return False
        #check quadrants
        for i in range(self.N):
            qri = i*self.N
            for j in range(self.N):
                qcj = j*self.N
                quadrant = [row[qri:qri+self.N] for row in puzzle[qcj:qcj+self.N]]
                if sum([sum(row) for row in quadrant]) != self.S:
                    return False
                
        return True
        
    def _reject(self, puzzle):
        """
        Checks wether the puzzle is valid, else is rejected
        """
        #TODO make it more efficient
        #check for non empty rows
        for r in puzzle:
            if 0 not in r and sum(r) != self.S:
                return True
        #check columns (obtain by transposing the matrix)
        t_puzzle = [[r[i] for r in puzzle] for i in range(self.D)]
        #check for non empty columns
        for c in t_puzzle:
            if 0 not in c and sum(c) != self.S:
                return True
        #check non empty quadrants
        for i in range(self.N):
            qri = i*self.N
            for j in range(self.N):
                qcj = j*self.N
                quadrant = [row[qri:qri+self.N] for row in puzzle[qcj:qcj+self.N]]
                qlist = []
                for row in quadrant:
                    qlist.extend(row)
                if 0 not in qlist and sum(qlist) != self.S:
                    return True
                
        return False


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
        return None
        
    def _get_candidates(self, puzzle, pos):
        """
        Calculates the candidates for a certain position in the puzzle
        @param puzzle
        @param pos: coord (x,y) in puzzle
        """
        i,j = pos
        if puzzle[i][j] != 0:
            return []
        D = len(puzzle)  #matrix dimension
        N = int(math.sqrt(D))  #quadrants
        numbers = range(1, D+1)  #possible numbers and indexes
        taken = set([r for r in puzzle[i]])
        col = [puzzle[k][j] for k in range(D)]
        taken.update(col)
        #TODO improve math here (did it at 1 am)
        qr = i/N; qc = j/N  #integer division ->important
        quadrant = [row[qc*N:(qc+1)*N] for row in puzzle[qr*N:(qr+1)*N]]
        for r in quadrant:
            taken.update(r)
        taken.discard(0)
        #avoid duplicates
        taken = list(taken)
        return [i for i in numbers if i not in taken]

    def _get_all_candidates(self, puzzle):
        """
        Calculates the candidates for a certain position in the puzzle
        @param puzzle
        """
        #all numbers in the selectable set
        numbers = range(1, self.D+1)
        #the index of the rows and columns
        indexes = range(self.D)
        #initial candidates, empty
        candidates = [[[] for j in indexes] for k in indexes]
        for i in indexes:
            #i == row index
            for j in indexes:
                # j == col index
                if puzzle[i][j] == 0:
                    #if the position is not yet defined
                    candidates[i][j] = self._get_candidates(puzzle, (i,j))
        return candidates

class RecursiveBacktrackingSudokuSolver(Sudoku):
    """
    This sudoku solver uses a recursive backtracking algorithm
    It can (and has by default) constraints on the elements that will try. 
    This improves efficiency 
    It can be used also as a pure dumb backtracking, that is slower and more memory intensive
    """
    def __init__(self):
        """
        """
        #dimension
        self.D = 0
        #quadrant dimension && n# of quadrants
        self.N = 0 
        #row sum == column sum == quadrant sum
        self.S = 0
        
    def _generate_next(self, puzzle, number):
        """
        Generates the next puzzle
        looks for the first zero and changes it to the given number
        """
        #deep copy needed (or will modify base puzzle and will be impossible to roll back)
        new_puzzle = copy.deepcopy(puzzle)
        for row in new_puzzle:
            if 0 in row:
                row[row.index(0)] = number
                break
        return new_puzzle
    
    def solve(self, puzzle, use_constraints=True):
        """
        Solves the sudoku
        @param puzzle: an already parsed puzzle.
        """
        #get sudoku puzzle dimensions
        self.D = len(puzzle)
        #sum to check
        self.S = sum(range(1, self.D+1))
        #number of quadrant rows and columns
        self.N = int(math.sqrt(self.D))
        
        return self._recursive_solve(puzzle, use_constraints)
        
    def _recursive_solve(self, puzzle, depth=0, use_constraints=True):
        """
        recursive solve
        @param puzzle: an already parsed puzzle.
        @param depth: depth counter
        @param use_constraints: if should use pure recursion or constrains 
                            for the calculation pure recursion is less efficient
        """
        #evaluation
        if self._reject(puzzle):
            return None
        if self._accept(puzzle):
            return puzzle
        #constraints
        if use_constraints:
            pos = self._get_next_zero(puzzle)
            candidates = self._get_candidates(puzzle, pos)
        else:
            candidates = range(1, self.D+1)            
        #try all constraints
        for i in candidates:
            new_puzzle = self._generate_next(puzzle, i)
            ret = self._recursive_solve(new_puzzle, depth+1)
            if ret is not None:
                return ret


################################################################################
class SudokuPuzzleGenerator(RecursiveBacktrackingSudokuSolver):
    """
    Generates sudoku puzzles
    Can use backtracking solver for finishing the generation
    """
    def __init__(self):
        """
        """
        pass
    
    def _generate_puzzle(self, solved_puzzle, difficulty):
        """
        Takes a sudoku solved and takes out to leave only 'difficulty' 
        number of elements visible, the rest is fill to 0
        @param solved_puzzle: the sudoku puzzle completed
        @param difficulty: number of zeros that will be put
        """
        D = len(solved_puzzle)
        puzzle = copy.deepcopy(solved_puzzle)
        #keep record of columns and rows that where selected
        rows_register = range(D)
        cols_register = [range(D) for i in rows_register]
        
        for i in range(difficulty):
            r = random.choice(rows_register)
            c = random.choice(cols_register[r])
            #set blank to that point
            puzzle[r][c] = 0
            #erase register from the colums
            cols_register[r].remove(c)
            #check if row empty
            if len(cols_register[r]) == 0:
                rows_register.remove(r)
        return puzzle

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
        
    def _generate_base_and_solve(self, dimension):
        """
        Generates a valid row, column and quadrant and then tries to solve for it
        """
        pos = random.randint(1,dimension), random.randint(1,dimension)
        puzzle = self._generate_valid_position(dimension, pos)
        solution = self.solve(puzzle)
        return solution
        
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
    
    def generate(self, dimension=9, difficulty=27, tries=10):
        """
        returns a pair of matrices (puzzle, solution)
        @param dimension: the number of columns and rows in the puzzle
        @param difficulty: number of zeros that will be put
        """
        assert math.sqrt(difficulty) <= dimension
        for i in xrange(tries):
            try:
                solution = self._generate_base_and_solve(dimension)
                puzzle = self._generate_puzzle(solution, difficulty)
                return puzzle, solution
            except Exception as e:
                #TODO log failed generation
                print(e)
                print("try %d failed, trying again " % i)
        return None
