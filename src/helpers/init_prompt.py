from helpers.get_commits import get_commits
from helpers.chronologize import chronologize
from helpers.tokenize import Tokenize
from helpers.get_changelog import get_changelog

def init_prompt():
  print('Create CHANGELOG or Update CHANGELOG?')
  print('1. Create')
  print('2. Update')

  answer = input()

  if answer == '1':
    commits = get_commits()
    t = Tokenize(commits)
    print(t.tokenize())
  else:
    if answer == '2':
      get_changelog()
    else:
      print(f'Wrong answer {answer}')
