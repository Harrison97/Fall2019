from .validator import Validator

class Criminal(Validator):

  def validate(self, ss_num: 'XXX-XX-XXXX') -> (bool, 'reason'):
    return True if ss_num[1] == '5' else (False, 'Break in.')

