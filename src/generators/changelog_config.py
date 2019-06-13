def default_config():
  config = {}
  tokens = config['tokens'] = {}

  def append_keyword(token, keywords):
    tokens[token] = keywords

  append_keyword('Added', ['Add', 'Added'])
  append_keyword('Changed', ['Change', 'Changed'])
  append_keyword('Deprecated',  ['Deprecate', 'Deprecated'])
  append_keyword('Enhance', ['Enhance', 'Enhanced'])
  append_keyword('Fixed', ['Fix', 'Fixed'])
  append_keyword('Removed', ['Remove', 'Removed'])
  append_keyword('Security', ['Security', 'Secured'])

  return config
