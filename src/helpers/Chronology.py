import re

def get_date(commit_date):
  date_str = re.findall(r'[^Date:]([A-Za-z]{3})[\s]([0-9]{1,2})[\s](?:[\d]{2}[\:][\d]{2}[\:][\d]{2}[\s])([0-9]{4})', commit_date)
  return date_str

def get_by_date(commits):
  # FIXME: Key Error 

  commits_by_date = {}
  for commit in commits:
    date = get_date(commit['date'])[0]
    date_str = f'{date[0]}_{date[1]}_{date[2]}'

    if commits_by_date[date_str] == None:
      commits_by_date[date_str] = [].append(commit)
    else:
      commits_by_date[date_str].append(commit)
