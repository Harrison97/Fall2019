from .validator import Validator

class Employment(Validator):

  def validate(self, ss_num: 'XXX-XX-XXXX') -> (bool, 'reason'):
    return True if ss_num[2] == '5' else (False, 'No Experience.')

