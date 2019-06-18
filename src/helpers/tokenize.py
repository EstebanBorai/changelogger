from helpers.manage_files import read_config
from helpers.chronologize import chronologize

class Tokenize:
  tokens = None
  token_list = None
  commits = None

  def __init__(self, commits):
    self.tokens = read_config()['tokens']
    self.commits = commits

    all_tokens = []

    for _, token_items in self.tokens.items():
      for tkn in token_items:
        all_tokens.append(tkn.lower())
    
    self.token_list = all_tokens

  def __get_token_parent(self, token):
    token_p = None
    for token_parent in self.tokens.keys():    
      if token.capitalize() in self.tokens[token_parent]:
        token_p = token_parent
    
    return token_p

  def __resolve_token(self, date_commits):
    aggregate = {
      'Misc': []
    }
    
    for commit in date_commits:
      try:
        token = next(t.lower() for t in commit['message'].lower().split() if t.lower() in self.token_list)
        token_parent = self.__get_token_parent(token)
        if token_parent in aggregate:
          aggregate[token_parent].append(commit)
        else:
          token_list = list()
          aggregate[token_parent] = token_list
          aggregate[token_parent].append(commit)
      except StopIteration:
        aggregate['Misc'].append(commit)
        pass

    if len(aggregate['Misc']) is 0:
      del aggregate['Misc']

    return aggregate

  def tokenize(self):
    chronologized_commits = chronologize(self.commits)
    commit_dates = chronologized_commits.keys()
    results = {}

    for date in commit_dates:
      date_commits = chronologized_commits[date]
      results[date] = self.__resolve_token(date_commits)

    return results
