from generators.changelog_config import default_config
import json
import os

current_directory = os.getcwd()
changelog_dir = f'{current_directory}/CHANGELOG'
changelog_config_dir = f'{current_directory}/changelogger.config.json'

def read_config():
  print(f'Reading configuration from {changelog_config_dir}')
  try:
    with open(changelog_config_dir, 'r') as config_file:
      return json.loads(config_file.read())
  except IOError:
    print(f'Configuration file not found in {changelog_config_dir}')
    print(f'Creating a new configuration file')
    with open(changelog_config_dir, 'w') as new_config_file:
      json.dump(default_config(), new_config_file, indent=2)

def read_changelog():
  print(f'Reading CHANGELOG from {changelog_dir}')
  try:
    with open(changelog_dir, 'r') as changelog:
      return changelog.read()
  except IOError:
    print(f'CHANGELOG not found at {changelog_dir}')

def checkout():
  try:
    with open(changelog_dir, 'r') as existent_changelog:
      print('Not implemented yet')
      # load_current_changelog(existent_changelog)
  except IOError:
    print('Creating new CHANGELOG')
    with open(changelog_dir, 'w') as new_changelog:
      new_changelog.write('# Changelog\n')
      new_changelog.write('All notable changes to this project will be documented in this file.\n\n')
      new_changelog.write('The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),\n')
      new_changelog.write('and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).\n\n')
