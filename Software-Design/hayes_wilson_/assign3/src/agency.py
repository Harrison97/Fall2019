def evaluate(*args: 'Validator', ss_num: 'XXX-XX-XXXX' = '') -> {'valid': bool, 'reasons': []}:
  response = {'valid': True}
  for criteria in args:
    valid = criteria().validate(ss_num)
    if type(valid) is not bool and valid[0] is False:
      response['valid'] = False
      if 'reasons' in response:
        response['reasons'].append(valid[1])
      else:
        response['reasons'] = [valid[1]]

  return response

