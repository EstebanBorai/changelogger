def get_version(version, last_version):
  [major, minor, patch] = version.split('.')
  [majorLast, minorLast, patchLast] = last_version.split('.')

  if major > majorLast:
    print('Major Version')
    return

  if major == majorLast:
    if minor > minorLast:
      print('Minor Version')
      return
    
    if patch > patchLast:
      print('Patch Version')
      return

def prompt_config():
  config = {}

  # Prompt Version
  print('Enter version/release (M.m.P)')
  config['version'] = input('Version: ')
  # TODO: Get the last_version from changelog 
  last_version = '0.1.1'
  get_version(config['version'], last_version)

prompt_config()
