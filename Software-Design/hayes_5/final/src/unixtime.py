def fetch_unixtime(fetch_content, parse_content):

  try:
    content = fetch_content()
  except Exception as err:
    return err

  return 'Unix time is ' + parse_content(content)

