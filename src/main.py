from helpers.get_commits import get_commits
from helpers.chronologize import chronologize
from helpers.tokenize import tokenize

def init():
  commits = get_commits()
  tokenize(commits)

init()
