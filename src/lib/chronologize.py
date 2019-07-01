import re
from datetime import datetime

def __remove_date_from(commit):
  try:
    del commit['date']
    return commit
  except KeyError:
    pass

def chronologize(commits):
  commits_by_date = {}
  for commit in commits:
    date_str = commit['date']

    if date_str in commits_by_date:
      commits_by_date[date_str].append(__remove_date_from(commit))
    else:
      commit_list = list()
      commit_list.append(__remove_date_from(commit))
      commits_by_date[date_str] = commit_list
  return commits_by_date
