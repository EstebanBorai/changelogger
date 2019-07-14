import re
from datetime import datetime

def chronologize(commits):
	"""
		Accumulate commits by date and
		returns them in a dictionary where the
		key is the date and the value is the list
		of commits.
	"""
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

def __remove_date_from(commit):
	try:
		del commit['date']
		return commit
	except KeyError:
		pass
