from .validator import Validator

class Credit(Validator):

  def validate(self, ss_num: 'XXX-XX-XXXX') -> (bool, 'reason'):
    return True if ss_num[0] == '5' else (False, 'Poor Credit.')

