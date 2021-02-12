from .validator import Validator

class Citizenship(Validator):

  def validate(self, ss_num: 'XXX-XX-XXXX') -> (bool, 'reason'):
    return True if ss_num[4] == '5' else (False, 'Not a citizen.')

