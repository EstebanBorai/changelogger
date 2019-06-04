from changelogger import get_commits
from manage_files import checkout

def init():
  # checkout()
  commits = get_commits()
  print(commits)

init()
