# Sudoku solver set

This small project contains a SUDOKU solver, the tests, generator and documentation.

This document contains some information about design decisions and use

###Usage
    
    ./sudoku_solver.py -f sudoku_files/example.csv -o out.csv
    
or

    python sudoku_solver.py -f sudoku_files/example.csv -o out.csv
    
##Installation

    git clone 
    virtualenv venv
    source /ven/bi/activate
    
    
###Web based site
    
    
##Goals of this little project

Entering the Insight Data Engineering program.

Build a complete program that can be used and understood by other people and can be used also as a Python example project.

Build from simple algorithms and while time is available, build more complex solvers

##Scope for first submission (27/10/2014)

Time limited: should be done in no more than half a day on Saturday and half a day on Sunday (no more than one working day)

####Language choice:
 * Python: My choice
 * Java: too verbose, will take more time
 * C: will take longer
 * C++: will take longer, will be nice to see if it's possible to implement a compile time solver (with templates :p)
 * Ruby: I don't know it yet, 
 * Clojure: I don't know it yet
 * Scala: I don't know it yet but I'd like to try it

I would like to make it in Javascript (Coffescript or Typescript) to make it work directly on the web. But it's not on the previous list

####Why Python:
It's a nice language, I've worked with already some time and I feel at ease.
Also it's easy and quite to mount a Python server for making it work in web.

####Dependency limitation
Although scipy libraries are really good and fast for manipulating matrices, the goal is to be able to make it work without any non basic dependency
the idea is to make it run under python 2.7 and 3 and make it work under Brython (brython.info) for a demo (I'd like to play a bit with brython and see the results)

##Sudoku Problem Description


###Vocabulary

Puzzle: 
Row:
Colum:
Quadrant:
Dimension:
Sum:


##Planning

###Considerations
As I like to think on challenges before searching for the solutions:
1st: how do I solve Sudoku puzzles? -> this indicates finding candidates and backtracking

A easier approach would be: implement backtracking and then start adding constraints (candidates for row/column/quadrant)


Problem: **SUDOKU** solver

Sudoku characteristics:
    []() Wikipedia page
    

Algorithms:
    backtracking
    constraint problem
    


###Development


###Web (Brython)

##Technical Details

##Backtracking

##Constraints

##Conclussions

##Future

Add more algorithms, 
I would like to have one algorithm of each type and an analysis of time and memory complexity of each

 * Constraints from paper: <!--TODO-->
 * Genetic Algorithms
 * Neural Networks
 
##Sources:

http://zhangroup.aporc.org/images/files/Paper_3485.pdf Sudoku puzzles generating [sic]
http://arxiv.org/pdf/1208.0370v1 Continuous time solver
http://www.cs.virginia.edu/~robins/The_Science_Behind_SudoKu.pdf The science behind sudoku
http://4c.ucc.ie/~hsimonis/sudoku.pdf Sudoku as a Constraint problem
http://en.wikipedia.org/wiki/Sudoku_solving_algorithms
http://en.wikipedia.org/wiki/Sudoku
