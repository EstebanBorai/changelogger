import subprocess
import sys
import re

def get_commits():
	"""
		Returns an array of dictionaries with the results
		of the `git log` command
	"""
	commits = __git_log()
	return __normalize(commits)

def __git_log():
	response = subprocess.check_output(
		['git', 'log', '--date=short'], stderr=subprocess.STDOUT
	).decode(sys.stdout.encoding)

	return str(response).split('\n')

def __get_commit_message(line):
	if line.startswith('    '):
		return re.compile('^    ').sub('', line)
	return False

def __normalize(log_output):
	current = {}
	commits = []

	commit_id = lambda l : l.split('commit ')[1]

	for line in log_output:
		is_commit_message = __get_commit_message(line)

		if is_commit_message != False:
			current['message'] = is_commit_message
		else:
			if line.startswith('commit'):
				if len(list(current.keys())) is 0:
					current['commit'] = commit_id(line)
				else:
					commits.append(current)
					current = {}
					current['commit'] = commit_id(line)
			else:
				try:
					key, value = line.split(':', 1)
					current[key.lower()] = value.strip()
				except ValueError:
					if line is '':
						pass

	# appends the first commit in the log
	commits.append(current)
	return commits
