from helpers.get_commits import get_commits
from helpers.chronologize import chronologize
from helpers.tokenize import Tokenize

def init():
  commits = get_commits()
  t = Tokenize(commits)
  print(t.tokenize())

init()
