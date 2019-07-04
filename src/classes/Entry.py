import datetime

class Entry:
	'''A Changelog entry structure'''
	version = ''
	date = None
	changes = dict()

	def __init__(self, version, date):
		self.version = version
		self.date = date

	def __entry_changelog_date(self):
		'''__entry_changelog_date formats the entry date into a "YYYY-MM-DD" formatted string'''
		return self.date.strftime("%Y-%m-%d")

	def __entry_changelog_header(self):
		'''__entry_changelog_header creates the header of a CHANGELOG entry'''
		return f'## [{self.version}] - {self.__entry_changelog_date()}'

	def append_change(self, change_t, change_line):
		'''append_change appends a change to the list of changes'''
		if change_t in self.changes:
			self.changes[change_t].append(change_line)
		else:
			self.changes[change_t] = list()
			self.changes[change_t].append(change_line)

	def to_changelog(self):
		'''to_changelog creates the entry string to write in the CHANGELOG file'''
		entry_str = ''
		entry_str += f'{self.__entry_changelog_header()}\n'
		changes_types = self.changes.keys()

		for change_type in changes_types:
			entry_str += f'### {change_type}\n'
			for change in self.changes[change_type]:
				entry_str += f'- {change}\n'
