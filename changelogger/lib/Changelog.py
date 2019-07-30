import os

from lib.Entry import Entry
from lib.get_tags import get_tags
from lib.get_commits import get_commits
from lib.extract_keys import extract_keys
from lib.gather_config import gather_config

class Changelog():
	"""
		Represents a CHANGELOG file which is a collection of
		`Entries` sorted by version
	"""

	def __init__(self):
		self.entries = []
		self.commits = []
		self.config = gather_config()
	
	def __changelog_header(self):
		"""
			Returns the CHANGELOG header
		"""
		return """# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).\n\n"""

	def __normalized_commits(self):
		commits = get_commits()
		all_keys = extract_keys(self.config['tokens'], commits)
		self.commits = all_keys

	def __gather_versions(self):
		tags = get_tags()

		if len(tags) is 0:
			print('Theres no versions for the current repository.')
			print('All commits will be treated as "Unreleased"')
			self.__normalized_commits()
			for changes_date in self.commits:
				entry = Entry(None, changes_date)
				for change_type in self.commits[changes_date]:
					for change_dict in self.commits[changes_date][change_type]:
						entry.append_change(change_type, change_dict['message'])

				self.entries.append(entry)
		else:
			print('Creating version scheme')
			print('NOT IMPLEMENTED YET')

	def __write_file(self, file_str):
		"""
			Creates CHANGELOG file in the current working directory (cwd)
		"""
		cwd = os.getcwd()
		changelog_file_dir = f'{cwd}/CHANGELOG'
		try:
			with open(changelog_file_dir, 'r') as changelog:
				changelog.write(file_str)
		except IOError:
			print(f'{changelog_file_dir} not found.')
			print(f'Creating a new "CHANGELOG" at {changelog_file_dir}')
			with open(changelog_file_dir, 'w') as new_changelog:
				new_changelog.write(file_str)

	def create(self):
		file_str = ''
		file_str += self.__changelog_header()

		self.__gather_versions()
		for entry in self.entries:
			file_str += str(entry)
			file_str += '\n'

		self.__write_file(file_str)
