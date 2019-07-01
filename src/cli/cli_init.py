import argparse
from . import init_changelog

def init():
	'''Setup CLI Arguments'''
	cli = argparse.ArgumentParser(description='Changelogger manages a CHANGELOG for your repository')

	# reads target version
	cli.add_argument('version', type=str, help='Target Version', nargs='?')

	# reads create changelog option (--init)
	cli.add_argument('-i', '--init', action='store_true', help='Creates a new CHANGELOG')

	args = cli.parse_args()

	if args.init:
		init_changelog.init()
