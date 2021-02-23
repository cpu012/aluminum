from constant import *
from evaluate import *
import sys, os

# startup
variables = CONF_STARTUP_VARIABLES.copy()

# get user input
while True:
    problem = input(CONF_PROMPT)
    if problem.lower() == 'exit':
        break
    elif problem.lower() == 'clr':
        os.system('cls' if sys.platform == 'win32' else 'clear')
    else:
        print(split_problem(problem))
        print(calculate(split_problem(problem), variables))
