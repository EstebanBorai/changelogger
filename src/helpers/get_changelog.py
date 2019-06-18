from helpers.manage_files import read_changelog

def get_changelog():
  data = read_changelog()
  print(data)

get_changelog()
