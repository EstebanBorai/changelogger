from manage_files import read_config
from helpers.chronologize import chronologize

class Tokenize:
  tokens = None
  commits = None

  def __init__(self, commits):
    self.tokens = read_config()['tokens']
    self.commits = commits

  def __resolve_token(self, date_commits):
    aggregate = {}

    for commit in date_commits:
      message = commit['message']
      for token_set in self.tokens.items():
        for tkn in token_set[1]:
          if tkn.lower() in message.lower():
            if tkn in aggregate:
              aggregate[tkn].append(commit)
            else:
              token_list = list()
              aggregate[tkn] = token_list
              aggregate[tkn].append(commit)
    
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
