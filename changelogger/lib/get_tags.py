import subprocess
import sys
import re

def get_tags():
	"""
		Returns an array of strings with the results
		of the `git tag` command
	"""
	response = subprocess.check_output(
		['git', 'tag'], stderr=subprocess.STDOUT
	).decode(sys.stdout.encoding)

	tags = str(response).split('\n')
	
	if len(tags) > 0 and tags[0] != '':
		return tags
	return []
