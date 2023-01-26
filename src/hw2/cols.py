from logging import NullHandler
from src.num import Num
from src.sym import Sym
import re

class Cols:
    '''Declares a column class that holds a column of data'''

    def __init__(self, t, col, cols):
        ''' 
        inits Cols with name of col
        :param names: (str) first row containing names of the columns
        :type names: (str) names of the columns
        :type all: (list[col]) every column including skipped columns are included here
        :type x: (list[col]) every independent unskipped column
        :type y: (list[col]) every dependent unskipped column
        :type klass: (col) single dependent col
        
        '''
        self.names = t
        self.all = []
        self.x = []
        self.y = []
        self.klass = None
        for n, s in enumerate(t):
            col = Num(n, s) if s[0].isupper() else Sym(n, s)
            self.all.append(col)
            if s[-1] != 'X':
                if s[-1] == '!':
                    self.klass = col
                if s.find('+') != -1 or s.find('-') != -1:
                    self.y.append(col)
                else:
                    self.x.append(col)

