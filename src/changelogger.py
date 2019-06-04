import re
import os
import subprocess

current_directory = os.getcwd()

leading_4_spaces = re.compile('^    ')

def get_commits():
    lines = subprocess.check_output(
        ['git', 'log'], stderr=subprocess.STDOUT
    ).split('\n')
    commits = []
    current_commit = {}

    def save_current_commit():
        title = current_commit['message'][0]
        message = current_commit['message'][1:]
        if message and message[0] == '':
            del message[0]
        current_commit['title'] = title
        current_commit['message'] = '\n'.join(message)
        commits.append(current_commit)

    for line in lines:
        if not line.startswith(' '):
            if line.startswith('commit '):
                if current_commit:
                    save_current_commit()
                    current_commit = {}
                current_commit['hash'] = line.split('commit ')[1]
            else:
                try:
                    key, value = line.split(':', 1)
                    current_commit[key.lower()] = value.strip()
                except ValueError:
                    pass
        else:
            current_commit.setdefault(
                'message', []
            ).append(leading_4_spaces.sub('', line))
    if current_commit:
        save_current_commit()
    return commits

def create_changelog():
  changelog_dir = current_directory + '/CHANGELOG'
  try:
    with open(changelog_dir, 'r') as current_changelog:
      print(current_changelog)
  except IOError:
    print('There\'s no CHANGELOG in this project.')
    print('Creating a new CHANGELOG')
    with open(changelog_dir, 'w') as new_changelog:
      new_changelog.write('# Changelog\n')
      new_changelog.write('All notable changes to this project will be documented in this file.\n\n')
      new_changelog.write('The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),\n')
      new_changelog.write('and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).\n\n')

create_changelog()