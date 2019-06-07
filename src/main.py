from helpers.get_commits import get_commits
from helpers.chronology import get_by_date

def init():
  commits = get_commits()
  print(get_by_date(commits))

init()
