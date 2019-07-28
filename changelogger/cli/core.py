import argparse
from cli.init import main as init_changelogger

def init():
	"""
		Initializes a CLI instance for Changelogger
	"""
	cli = argparse.ArgumentParser(description='Changelogger manages a CHANGELOG for your repository')

	# create changelog option (--init)
	cli.add_argument('-i', '--init', action='store_true', help='Setup Changelogger and creates a CHANGELOG')

	args = cli.parse_args()

	if args.init:
		init_changelogger()
