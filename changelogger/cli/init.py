from lib.gather_config import gather_config
from lib.get_commits import get_commits
from lib.extract_keys import extract_keys
from lib.get_tags import get_tags
from lib.Entry import Entry

def main():
	"""
		Initializes a CHANGELOG based on `changelogger.config.json`
	"""
	commits = None
	config = gather_config()
	tags = get_tags()

	if len(tags) == 0:
		# If there's no tags, create a CHANGELOG with
		# the existing commits
		commits = get_commits()
		all_keys = extract_keys(config['tokens'], commits)
		print(all_keys)
