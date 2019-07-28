from lib.gather_config import gather_config
from lib.get_commits import get_commits
from lib.extract_keys import extract_keys

def main():
	"""
		Initializes a CHANGELOG based on `changelogger.config.json`
	"""
	config = gather_config()
	commits = get_commits()
	print(extract_keys(config['tokens'], commits))
