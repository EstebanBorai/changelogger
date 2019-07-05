from lib.get_commits import get_commits
from lib.chronologize import chronologize
from lib.Extract import Extract
from lib.get_changelog import get_changelog

def init_prompt(args):
	print(args)

	if args[1] == '--version':
		if args[2] == None:
			print('Missing version number to append')
		else:
			print(f'Appends version {args[2]}')

  # print('Create CHANGELOG or Update CHANGELOG?')
  # print('1. Create')
  # print('2. Update')

  # answer = input()

  # if answer == '1':
  #   commits = get_commits()
  #   t = Tokenize(commits)
  #   print(t.tokenize())
  # else:
  #   if answer == '2':
  #     get_changelog()
  #   else:
  #     print(f'Wrong answer {answer}')
