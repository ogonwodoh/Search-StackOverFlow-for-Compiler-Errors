# Search-StackOverFlow-for-Compiler-Errors
Uses python, REST APIs, and a little bit of Linux shell logic to search StackOverFlow for compiling errors

Quick Start:
1) run your program in the command line environment with the command: <compiling_instructions> 2>&1 | search.py
2) your program will automatically open 3 urls from StackOverFlow that contain information on how to fix your compiling errors

NOTE: This program only works with certain compilers that compile java, c, and python. Feel free to change or add to the logic that detects the 'tag' attributes so that the program can correctly detect the programming language you have used.
You can also change how many search urls to open and the order they appear in.

Enjoy and let me know of any errors or improvements!
