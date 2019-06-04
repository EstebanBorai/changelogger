import subprocess
import sys
import re

leading_4_spaces = re.compile('^    ')

def get_commits():
  git_log = subprocess.check_output(
     ['git', 'log'], stderr=subprocess.STDOUT
  ).decode(sys.stdout.encoding)
    
  lines = str(git_log).split('\n')
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
