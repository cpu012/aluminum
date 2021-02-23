from constant import *
import itertools, time

def split_problem(problem):
  tokens = []
  number, paren, variable = '', '', ''
  paren_total = 0
  paren_end, num_end, var_end = False, False, False

  for i, char in enumerate(problem): # identify tokens
    if char in CONF_WHITESPACES:
      pass
    
    # parentheses
    elif char == '(':
      paren += char
      paren_total += 1
    elif char == ')':
      paren_total -= 1
      if paren_total > 0: paren += char
      else: paren_end = True
    elif paren_total > 0: paren += char

    # variables and numbers
    elif char.isdigit():
      number += char
      if i == len(problem) - 1:
        num_end = True
      elif not problem[i + 1].isdigit():
        num_end = True
    elif ord(char) in VALID_VAR_CHARS:
      variable += char
      if i == len(problem) - 1:
        var_end = True
      elif not ord(problem[i + 1]) in VALID_VAR_CHARS:
        var_end = True

    elif char in '=^*/+-':
      tokens += char

    # handle multi character tokens
    if num_end:
      tokens.append(int(number))
      num_end = False
      number = ''
    elif paren_end:
      tokens.append(paren)
      paren_end = False
      paren = ''
    elif var_end:
      tokens.append(variable)
      var_end = False
      variable = ''

  return tokens

def calculate(problem, var):
  is_valid_var = False
  tok_sub = {'^': '**'}
  vtoks_grp = itertools.cycle(('^', '*/', '+-'))

  while len(problem) > 0:
    for i, token in enumerate(problem): # calculate values 
      try:
        if isinstance(token, (str)):
      
          if token == '=': # assign variables
            if bool([ch for ch in problem[i - 1] if ord(ch) in VALID_VAR_CHARS]) \
            and isinstance(problem[i + 1], (int)):
              print('x')
              time.sleep(1)
              var[problem[i - 1]] = problem[i + 1]
              # remove the assignment
              problem.pop(i - 1)
              problem.pop(i - 1)
              problem.pop(i - 1)
          
          elif [ch for ch in token if ord(ch) in VALID_VAR_CHARS] == [token] \
          and not problem[i + 1] == '=': # validize variable
            if var.get(token): problem[i] = var[token] # replace variable with value

          elif token[0] == '(': # tokenize parentheses
            problem[i] = calculate(split_problem(token[1:]), var)[0][0]
   
          elif isinstance(problem[i - 1], (int)) and isinstance(problem[i + 1], (int)) \
          and token in next(vtoks_grp):
            exec('problem[i] = problem[i - 1]' + tok_sub.get(token, token) + 'problem[i + 1]')
            problem.pop(i - 1)
            problem.pop(i)
      except Exception as err:
        print('an error occured\n\t', err)

    if len(problem) <= 1: break
  return problem, var
     









