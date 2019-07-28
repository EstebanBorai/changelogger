import os
import json

current_dir = os.getcwd()
config_dir = f'{current_dir}/.changeloggerrc'

def gather_config():
	"""
		Reads the current working directory to find an
		existent `.changeloggerrc` file and return its contents, 
		otherwise the config will be generated with
		default values.
	"""
	print(f'Attempt to read {config_dir}')
	try:
		with open(config_dir, 'r') as config_file:
			return json.loads(config_file.read())
	except IOError:
		print(f'{config_dir} not found.')
		print(f'Creating a new ".changeloggerrc" at {current_dir}')
		with open(config_dir, 'w') as new_config_file:
			json.dump(__default_config(), new_config_file, indent=2)

def __default_config():
	"""
		Returns a dictionary with default configuration set.
	"""
	config = {}
	config['tokens'] = {}
	tokens = config['tokens']

	def append_keyword(token, keywords):
		tokens[token] = keywords

	append_keyword('Added', ['Add', 'Added'])
	append_keyword('Changed', ['Change', 'Changed'])
	append_keyword('Deprecated',  ['Deprecate', 'Deprecated'])
	append_keyword('Enhanced', ['Enhance', 'Enhanced'])
	append_keyword('Fixed', ['Fix', 'Fixed'])
	append_keyword('Removed', ['Remove', 'Removed'])
	append_keyword('Security', ['Security', 'Secured'])

	return config
