class Chronology:
  commits = None
  commit_days = {}

  def __init__(self, commits):
    self.commits = commits

  def get_by_date(self):
    if self.commits == None:
      raise Exception("Commits are None")
    
    for commit in self.commits:
      commit
