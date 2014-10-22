# -*- coding: utf-8 -*-
"""
"""

import copy


def parse_csv_from_text(csv):
    """
    parse input and add it to an array of arays
    """
    scene = [ [int(i.strip()) for i in j.split(',')] for j in csv.split('\n')]
    #verify dimension consistency
    for c in scene:
        assert len(scene) == len(c)
        for e in c:
            assert e >= 0
            
    #assert if fail
    return scene
    
def parse_csv_from_file(csvfile):
    """
    parse input and add it to an array of arays
    """
    f = open(csvfile)
    parse_csv_from_text(f.read())
    #TODO if fails file will not be closed -> treat it with an exception and finally
    f.close()
    #verify dimension consistency
    
    #assert if fail
    return scene

    
class RecursiveBacktrackingSudokuSolver(object):
    """
    This sudoku solver uses a dumb recursive backtracking 
    This should break memory or recursion limits
    also it's not that efficient
    Anyway, I wanted to do it.
    """
    def __init__(self):
        """
        """
        pass
        
    def _accept(self, scene):
        """
        checks that the scene is solved, if so, returns True, else returns False
        S is the sum
        D the dimension (number of columns and rows)
        N: number of quadrant rows and columns
        assumes that the scene is valid (dimensions and values in the cells)
        """
        #check rows
        for(r in scene):
            if sum(r) != self.S:
                return False
        #check columns (obtain by transposing the matrix)
        t_scene = [[r[i] for r in scene] for i in range(self.D)]
        for(c in t_scene):
            if sum(c) != self.S:
                return False
        #check quadrants
        
        for i in range(self.N):
            qri = i*self.N
            for j in range(self.N):
                qcj = j*self.N
                quadrant = [row[qri:qri+vN] for row in scene[qcj:qcj+self.N]]
                if sum([sum(row) for row in quadrant]) != self.S:
                    return False
                
        return True
        
    def _reject(self, scene):
        """
        """
        #check for non empty rows
        for(r in scene):
            if 0 not in r and sum(r) != self.S:
                return True
        #check columns (obtain by transposing the matrix)
        t_scene = [[r[i] for r in scene] for i in range(self.D)]
        #check for non empty columns
        for(c in t_scene):
            if 0 not in c and sum(c) != self.S:
                return True
        #check non empty quadrants
        for i in range(self.N):
            qri = i*self.N
            for j in range(self.N):
                qcj = j*self.N
                quadrant = [row[qri:qri+self.N] for row in scene[qcj:qcj+self.N]]
                qlist = []
                for row in quadrant:
                    qlist.extend(row)
                if 0 not in qlist and sum(qlist) != self.S:
                    return True
                
        return False

    def _generate_next(self, scene, number):
        """
        looks for the first zero and change it to the given number
        """
        new_scene = copy.deepcopy(scene)
        for row in new_scene:
            if 0 in row:
                row[row.index(0)] = number
        return new_scene
    
    def solve(self, scene):
        """
        Solves the sudoku
        @param scene: an already parsed scene.
        """
        #get sudoku scene dimensions
        self.D = len(scene)
        #sum to check
        self.S = sum(range(self.D))
        #number of quadrant rows and columns
        self.N = sqrt(self.D)
        
        return self._recursive_solve(scene)
        
    def _recursive_solve(self, scene):
        """
        recursive solve
        @param scene: an already parsed scene.
        """
        if reject(scene):
            return None
        if _accept(scene):
            return scene
        #This is the dumbest way to do it
        for i in range(1, self.D+1):
            scene = self._generate_next(scene, i)
            ret = self._recursive_solver(scene)
            if ret:
                return ret
        
