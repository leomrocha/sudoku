# Sudoku solver set

This small project contains a SUDOKU solver, the tests, generator and documentation.

##Usage
    
###Solving a sudoku puzzle

    ./sudoku_solver -f sudoku_files/example.csv -o out.csv
    #or
    python sudoku_solver -f sudoku_files/example.csv -o out.csv
    
###Generating puzzles

    ./sudoku_solver -f -o out.csv -s 9 -d 40

Will output two files:

 * puzzle_out.csv
 * solution_out.csv

Where puzzle_out.csv contains the puzzle where dimensions are 9x9 and 40 elements set to 0 and solution_out.csv contains the solution to the puzzle


###Getting stats

_Note:_ This is a functionality under development

    ./sudoku_stats -p out_puzzles_path/
    
In the path the files corresponding to the: run, dimension, difficulty for puzzle, solution and solved are saved.

Also two files will be in the current path:

 * generator_stats.csv
 * solver_stats.csv

That contain the statistics [run, dimension, difficulty,time (seconds) ] for the generator and solver.


The idea is to later plot behaviour for different algorithms
    
##Installation

    git clone https://github.com/leomrocha/sudoku.git
    cd sudoku
    ##
    #if you want to use virtualenv
    virtualenv venv
    source /ven/bin/activate
    #END virtualenv
    ##
    #Testing
    python setup.py test
    ##
    python setup.py install
    
    
#Discussion

##Goals of this little project

Getting into the Insight Data Engineering program.

Build a complete program that can be used and understood by other people and can be used also as a Python example project.

Build simple algorithms and if I have some more time, build more complex solvers (I'd like to try with genetic algorithms)


##Scope for first submission (27/10/2014)

Time limited: should be done in no more than half a day on Saturday and half a day on Sunday (no more than one working day)

##Language choice:
 * Python: My choice
 * Java: too verbose, will take more time
 * C: will take longer
 * C++: will take longer. Will be possible to implement a compile time solver (with templates)? 
 * Ruby: I don't know it yet, will take some getting used to it, no time.
 * Clojure: I don't know it yet, will take some getting used to it, no time.
 * Scala: I don't know it yet but I'd like to try it. It will take some getting used to it, no time.

Would be interesting to make it in Javascript (Coffescript or Typescript) for it work directly on the web. But it's not on the previous list.

###Why Python

It's a nice language, I've worked with already some time and I feel at ease. It's fast to develop something and is not to verbose.

###Dependency limitation

Although scipy libraries are really good and fast for manipulating matrices, the goal is to be able to make it work without any non basic dependency.
The idea is to make it run under python 2.7 and 3.

##Sudoku Problem Description

[Sudoku](http://en.wikipedia.org/wiki/Sudoku) on Wikipedia

###Vocabulary
 * Dimension (D) the number of rows and columns of the matrix represented Sudoku puzzle
 * Puzzle:  A DxD matrix representing a Sudoku puzzle formatted with 0s in the places to solve. D is perfect square
 * Row: A row in the matrix
 * Colum: A column in the matrix
 * Quadrant: a sqrt(D)xsqrt(D) sub matrix in specific positions ()
 * Sum: the sum of any valid solved Quadrant, Row or Column


##Development

From the technical point of view:

0. Write down algorithms (paper)
1. Recursive Solver + Tests
2. Constraints + Tests
3. Sudoku Generator + Tests
4. Statistics (in progress)


The selected algorithm is Backtracking with some constraints, this is fast enough for most puzzles and the time it takes to develop is reasonable and enters in the time I have to make it.

Writing the backtracing algorithm is not too time consuming and let's me time to complete the tests and writing down some other ideas and the generator.

Decision on the algorithms to use is not based on pure efficiency but on the ease to build and test them on time.

###Notes
As I like to think on challenges before searching for the solutions:

1st: how do I usually solve Sudoku puzzles? -> finding candidates and backtracking

The easiest approach would be: implement backtracking and then start adding constraints (candidates for row/column/quadrant)

Afterward I read and analyzed several papers and online documentation

I find interesting many of the approaches, for instance:

 * [Sudoku puzzles generating (sic)](http://zhangroup.aporc.org/images/files/Paper_3485.pdf)
 *[Continuous time solver](http://arxiv.org/pdf/1208.0370v1)
 *[The science behind sudoku](http://www.cs.virginia.edu/~robins/The_Science_Behind_SudoKu.pdf )
 *[Sudoku as a Constraint problem](http://4c.ucc.ie/~hsimonis/sudoku.pdf )
 *[A small discussion about sudoku solving algorithms](http://en.wikipedia.org/wiki/Sudoku_solving_algorithms)


##Conclussions


Was nice to write down a Sudoku solver in a few hours including tests, I feel that the task is completed although there are many things that I'd like to try. And there is a lot of work yet to make an application that can be used as a benchmarking tool

I started working on making this work under Brython (brython.info). All the libraries load correclty, but had no time to actually make a nice working GUI

I found out that manipulating DOM with python under brython can be a pain, and also I didn't like the '<=' operator for adding children.

##Future

 * Add more solving algorithms, 
 * Improve the creation of puzzles
   - difficulty in human terms
 * Improve the statistics module
   
   

