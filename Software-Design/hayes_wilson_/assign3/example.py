from src import agency as A
from src.validators import *

print('results for 555-55-5555: ', A.evaluate(Credit, Employment, ss_num='555-55-5555'))
print('results for 515-15-5555: ', A.evaluate(Credit, Citizenship, Criminal, Employment, ss_num='515-15-5555'))

