from lib.Changelog import Changelog

def main():
	"""
		Initializes a CHANGELOG based on `.changeloggerrc`
	"""
	changelog = Changelog()
	changelog.create()
