from manage_files import read_config
from helpers.chronologize import chronologize

class Tokenize:
  tokens = None
  commits = None
  token_keys = []

  def __init__(self, commits):
    self.tokens = read_config()['tokens']
    self.commits = commits
    self.token_keys = self.tokens.keys()

  def __resolve_token(self, date, aggregate, date_commits):
    for commit in date_commits:
      message = commit['message']
      for token in self.token_keys:
        __has_token = __has_token(message, token)

  def tokenize(self):
    chronologized_commits = chronologize(self.commits)
    commit_dates = chronologized_commits.keys()
    results = {}

    for date in commit_dates:
      date_commits = chronologized_commits[date]
      if date in results:
        self.__resolve_token(date, results, date_commits)
      else:
        results[date] = {}
        self.__resolve_token(date, results, date_commits)

    return results


  # {'Added': ['Add', 'Added'], 'Changed': ['Change', 'Changed'], 'Deprecated': ['Deprecate', 'Deprecated'], 
  # 'Fixed': ['Fix', 'Fixed'], 'Removed': ['Remove', 'Removed'], 'Security': ['Security']}
