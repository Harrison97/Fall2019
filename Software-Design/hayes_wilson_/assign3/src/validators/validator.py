from abc import ABC, abstractmethod

class Validator(ABC):

  @abstractmethod
  def validate(self, ss_num: 'XXX-XX-XXXX') -> (bool, 'reason'):
    """ This class is to be used as a base for validators. """

