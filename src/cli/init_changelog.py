from lib.manage_files import read_config, checkout, changelog_dir

def init():
	'''init initializes a CHANGELOG'''
	read_config()
	checkout()
	print(f'CHANGELOG has been created at {changelog_dir}')
