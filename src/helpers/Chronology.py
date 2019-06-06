import re

class Chronology:
  commits = None
  commit_days = {}

  def __init__(self, commits):
    self.commits = commits

  def get_date(self, commit_date):
    date_str = re.findall(r'[^Date:]([A-Za-z]{3})[\s]([0-9]{1,2})[\s](?:[\d]{2}[\:][\d]{2}[\:][\d]{2}[\s])([0-9]{4})', commit_date)
    return date_str

  def get_by_date(self):
    if self.commits == None:
      raise Exception("Commits are None")
    
    for commit in self.commits:
      commit
