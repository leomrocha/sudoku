# -*- coding: utf-8 -*-
"""
"""

import copy
import math

import traceback

def parse_csv_from_text(csv):
    """
    parse input and add it to an array of arays
    """
    puzzle = [ [int(i.strip()) for i in j.split(',')] for j in csv.split()]
    #verify dimension consistency
    for c in puzzle:
        assert len(puzzle) == len(c)
        for e in c:
            assert e >= 0
    return puzzle
    
def parse_csv_from_file(csvfile):
    """
    parse input and add it to an array of arays
    """
    f = open(csvfile)
    puzzle = parse_csv_from_text(f.read())
    #TODO if fails file will not be closed -> treat it with an exception and finally
    f.close()
    #verify dimension consistency
    #assert if fail
    return puzzle

    
class RecursiveBacktrackingSudokuSolver(object):
    """
    This sudoku solver uses a recursive backtracking algorithm
    It can (and has by default) constraints on the elements that will try. 
    This improves efficiency 
    It can be used also as a pure dumb backtracking, that is slower and more memory intensive
    """
    def __init__(self):
        """
        """
        pass
        
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
                
        print("Accepted solution: ")
        for r in puzzle:
            print(r)
        return True
        
    def _reject(self, puzzle):
        """
        """
        #print "rejecting puzzle"
        #for r in puzzle:
        #    print r 
        #check for non empty rows
        for r in puzzle:
            if 0 not in r and sum(r) != self.S:
                #print "rejecting row ", 0 not in r, r
                return True
        #check columns (obtain by transposing the matrix)
        t_puzzle = [[r[i] for r in puzzle] for i in range(self.D)]
        #check for non empty columns
        for c in t_puzzle:
            if 0 not in c and sum(c) != self.S:
                #print "rejecting col ", 0 not in c, c
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
                    #print "rejecting qlist ", 0 not in qlist, qlist
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
        D = len(puzzle)  #matrix dimension
        N = int(math.sqrt(D))  #quadrants
        numbers = range(1, D+1)  #possible numbers and indexes
        taken = set([r for r in puzzle[i]])
        col = [puzzle[k][j] for k in range(D)]
        taken.update(col)
        #TODO improve math here (did it at 1 am)
        qr = i/N; qc = j/N
        quadrant = [row[qc*N:qc*N+N] for row in puzzle[qr*N:qr*N+N]]
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
        D = len(puzzle)  #matrix dimension
        N = int(math.sqrt(D))  #quadrants
        #all numbers in the selectable set
        #the index of the rows and columns)
        numbers = range(1, D+1)
        indexes = range(D)
        #initial candidates, empty
        candidates = [[[] for j in indexes] for k in indexes]
        #for all columns and rows
        t_puzzle = [[r[i] for r in puzzle] for i in indexes]
        for i in indexes:
            #i == row index
            for j in indexes:
                # j == col index
                if puzzle[i][j] == 0:
                    #if the number is not yet defined
                    #get all taken
                    candidates[i][j] = self._get_candidates(puzzle, (i,j))
        return candidates
        
    def _generate_next(self, puzzle, number):
        """
        looks for the first zero and change it to the given number
        """
        #print("generating next: ", number)
        new_puzzle = copy.deepcopy(puzzle)
        for row in new_puzzle:
            if 0 in row:
                row[row.index(0)] = number
                break
        return new_puzzle
    
    def solve(self, puzzle):
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
        
        return self._recursive_solve(puzzle)
        
    def _recursive_solve(self, puzzle, depth=0, use_constraints=True):
        """
        recursive solve
        @param puzzle: an already parsed puzzle.
        @param depth: depth counter
        @param use_constraints: if should use pure recursion or constrains for the calculation
        pure recursion is less efficient
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
        
if __name__ == "__main__":
    """
    execute example
    """
    pass
    
