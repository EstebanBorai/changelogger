import datetime

class Entry:
	"""
		Entry represents each of the CHANGELOG
		entries. An entry indexes every change made to
		the project with date and category.
	"""
	def __init__(self, version, date):
		if version is None:
			self.version = 'Unreleased'
		else:
			self.version = version

		self.date = date
		self.changes = dict()

	def __changelog_header(self):
		"""
			Returns the header of the entry.
			Sample:
			[v1.0.1] - 2019-07-26
		"""
		return f'## [{self.version} - {self.date}]'

	def append_change(self, change_t, change_line):
		"""
			Appends a change to the current entry

			Keyword arguments:
			change_t -- Type of change to append. Eg: "Added"
			change_line -- The change to append
		"""
		if change_t in self.changes:
			self.changes[change_t].append(change_line)
		else:
			self.changes[change_t] = list()
			self.changes[change_t].append(change_line)

	def __str__(self):
		"""
			Creates the entry and returns it as a string.
		"""
		entry_str = ''
		entry_str += f'{self.__changelog_header()}\n'
		changes_types = self.changes.keys()

		for change_type in changes_types:
			entry_str += f'### {change_type}\n'
			for change in self.changes[change_type]:
				entry_str += f'- {change}\n'

		return entry_str
