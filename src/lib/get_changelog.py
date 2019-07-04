import re
import datetime
from lib.manage_files import read_changelog
from classes.Entry import Entry

def __entry_version(line):
	version = re.search(r'(\d.*)\.(\d.*)\.(\d[^\]]*)', line).group()
	date_str = re.search(r'(\d{4})\-(\d{1,2})\-(\d{1,2})', line).group()
	[year, month, day] = date_str.split('-')
	date = datetime.date(int(year), int(month), int(day))
	return [version, date]

def __entry_change_section(line):
	title = re.search(r'[^#][\S]{1}.*', line).group
	return title

def get_changelog():
	data = read_changelog()
	lines = str(data).split('\n')
	total_lines = len(lines)
	entries = {}
	current_entry = None
	current_change_section = None

	for line_number in range(total_lines):
		current_line = lines[line_number]

		if line_number <= 6:
			continue

		if current_line == '':
			continue

		if current_line.startswith('## ['):
			# start of CHANGELOG entry
			if current_entry == None:
				# the first time an Entry is registered
				[version, date] = __entry_version(current_line)
				current_entry = Entry(version, date)
				continue

			if current_entry != None:
				# steps into another Entry
				entries[current_entry.version] = current_entry
				[version, date] = __entry_version(current_line)
				current_entry = Entry(version, date)
				current_change_section = None
				continue

		if current_line.startswith('### '):
			# entry log (Entry.changes)
			current_change_section = __entry_change_section(current_line)
			continue

		if current_line.startswith('- '):
			# entry anotation
			current_entry.append_change(current_change_section, current_line)
			continue

	return entries
