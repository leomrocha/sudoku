#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["things/*"]

setup(
    name = "sudoku",
    version = "1.0",
    description = "Sudoku puzzle generator and solver",
    long_description = """
                        Sudoku puzzle generator and solver.
                        
                       """,
    author = "Leonardo Rocha",
    author_email = "",
    url = "http://leomrocha.github.io/sudoku",
    packages = ['sudoku', 'tests'],
    # package_data = {'' : '*.txt' },
    #'runner' is in the root.
    scripts = ["sudoku_solver"],
    classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Internet",
      ],
    keywords='sudoku',
    license='MIT',
    test_suite = 'tests'
) 
