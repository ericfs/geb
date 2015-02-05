# Prime theorem generator from Chapter 3.

import functools
import re

dnd_pattern = re.compile('(-+)DND(-+)')
df_from_dnd_pattern = re.compile('--DND(-+)')
df_pattern = re.compile('(-+)DF(-+)')
p_from_df_pattern = re.compile('(-+)-DF(-+)')
p_pattern = re.compile('P(-+)')

def dnd_axiom(x, y):
  return x + y + 'DND' + x

def dnd_theorem(_, s):
  match = dnd_pattern.match(s)
  if match:
    return s + match.groups()[0]
  return None

def df_from_dnd_theorem(_, s):
  match = df_from_dnd_pattern.match(s)
  if match:
    return match.groups()[0] + 'DF--'
  return None

def df_from_set_theorem(theorems, s):
  match = df_pattern.match(s)
  if match:
    z = match.groups()[0]
    x = match.groups()[1]
    needed_dnd = x + '-DND' + z
    if needed_dnd in theorems:
      return z + 'DF' + x + '-'
  return None

def p_theorem(_, s):
  match = p_from_df_pattern.match(s)
  if match:
    z0 = match.groups()[0]
    z1 = match.groups()[1]
    if len(z0) == len(z1):
      return 'P-' + z0
  return None

theorems_generators = [
    dnd_theorem,
    df_from_dnd_theorem,
    df_from_set_theorem,
    p_theorem
]

def find_all_new_theorems(theorems, fn):
  # Apply fn to each element of theorems then filter out non-theorems.
  mapper = functools.partial(fn, theorems)
  return filter(None, map(mapper, theorems))

def p_theorems(theorems):
  return sorted(filter(lambda s: p_pattern.match(s), theorems))

def print_p_theorems(theorems):
  print p_theorems(theorems)

def p_to_numeric(s):
  match = p_pattern.match(s)
  if match:
    return 'P' + str(len(match.groups()[0]))
  
def print_p_theorems_numeric(theorems):
  print map(p_to_numeric, p_theorems(theorems))

def generate_theorems(n):
  axiom = 'P--'

  # Start with n * n axioms
  theorems = set([axiom])
  theorems.update(
    (dnd_axiom('-' * i, '-' * j)
        for i in xrange(1, n + 1) for j in xrange(1, n + 1)))

  # Go through n iterations of generating theorems.
  for i in xrange(n):
    print i, len(theorems)
    for fn in theorems_generators:
      # Add the new theorems to the set of all theorems.
      theorems.update(find_all_new_theorems(theorems, fn))

  print n, len(theorems)
  return theorems

def identify_p_theorems(n):
  theorems = generate_theorems(n)
  print_p_theorems_numeric(theorems)

if __name__ == '__main__':
  # Slowly find some prime theorems.
  theorems = generate_theorems(10)
  print_p_theorems(theorems)
  identify_p_theorems(20)
