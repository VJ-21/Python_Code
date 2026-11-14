#os module will be working as  string but path lib handles as python objects
from pathlib import Path

a = Path() / 'test'/'dummY_test.txt' 

a.rename('dummY_dual.txt')
