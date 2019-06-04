import os

current_directory = os.getcwd()
changelog_dir = current_directory + '/CHANGELOG'

def checkout():
  try:
    with open(changelog_dir, 'r') as existent_changelog:
      print(existent_changelog)
  except IOError:
    print('Creating new CHANGELOG')
    with open(changelog_dir, 'w') as new_changelog:
      new_changelog.write('# Changelog\n')
      new_changelog.write('All notable changes to this project will be documented in this file.\n\n')
      new_changelog.write('The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),\n')
      new_changelog.write('and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).\n\n')
