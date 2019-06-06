from manage_files import read_config

class Tokenize:
  tokens = []
  undefined_lines = []
  

  def __init__(self):
    self.tokens = read_config()['tokens']
    self.tokens_keys = list(self.tokens.keys())

  def tokenize_line(self, line):
    try:
      for token in self.tokens_keys:
        if token in line:

        

    except ValueError:
      self.undefined_lines.append(line)

    print(self.tokens_keys)

t = Tokenize()
t.tokenize_line('Added')
