
user_input = input('enter file name, including the file extension')


import numpy as np
from numpy import genfromtxt

class Error(Exception):
   pass

class NoSolutionsError(Error):
   """Raised when the equations have no solutions"""
   pass


data = genfromtxt(user_input, delimiter=',')
b = data[:,-1]
A = data[:,0:-1]

try:
    X = np.linalg.solve(A,b)
    if np.isnan(X).all()!=True:
        print(f'solutions to linear equations: {X}')
    else: 
        raise NoSolutionsError

except NoSolutionsError:
    print('there is no solution to the equations provided')

except np.linalg.LinAlgError:
    print("there are no unique solutions to the equations provided")




