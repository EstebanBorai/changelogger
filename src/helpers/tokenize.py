from manage_files import read_config
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
        all_tokens.append(tkn)
    
    self.token_list = all_tokens

  def __get_token_parent(self, token):
    for token_parent in self.tokens.keys():    
      if token in self.tokens[token_parent]:
        return token_parent

  def __resolve_token(self, date_commits):
    aggregate = {
      'Misc': []
    }
    
    for commit in date_commits:
      for token in self.token_list:
        if token.lower() in commit['message'].lower().split():
          token_parent = self.__get_token_parent(token)
          if token_parent in aggregate:
            aggregate[token_parent].append(commit)
          else:
            token_list = list()
            aggregate[token_parent] = token_list
            aggregate[token_parent].append(commit)
        else:
          aggregate['Misc'].append(commit)

    return aggregate

  def tokenize(self):
    chronologized_commits = chronologize(self.commits)
    commit_dates = chronologized_commits.keys()
    results = {}

    for date in commit_dates:
      date_commits = chronologized_commits[date]
      results[date] = self.__resolve_token(date_commits)

    return results

  # {'Added': ['Add', 'Added'], 'Changed': ['Change', 'Changed'], 'Deprecated': ['Deprecate', 'Deprecated'], 
  # 'Fixed': ['Fix', 'Fixed'], 'Removed': ['Remove', 'Removed'], 'Security': ['Security']}
