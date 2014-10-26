#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

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
    if not os.path.isfile(csvfile):
        return None
    try:
        f = open(csvfile)
        ftext = f.read()
        f.close()
        puzzle = parse_csv_from_text(ftext)
        return puzzle
    except:
        #TODO log error
        pass
    return None


def save_puzzle_to_csv(puzzle, csvfile):
    """
    saves a puzzle to a csv file
    """
    try:
        f = open(csvfile, 'w')
        flines = []
        for r in puzzle:
            flines.append(','.join([str(i) for i in r])+'\n')
        f.writelines(flines)
        f.close()
    except:
        #TODO log error
        pass
