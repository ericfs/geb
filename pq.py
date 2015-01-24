# Chapter 2: The pq-system
import re
import random

axiom_pattern = re.compile('(-*)p-q(-*)-')
theorem_pattern = re.compile('(-*)p(-*)q(-*)')

def make_axiom(n):
  assert type(n) == int
  assert n > 0
  x = '-' * n
  return x + 'p' + '-q' + x + '-'

def next_theorem(theorem):
  assert 'p' in theorem
  assert 'q' in theorem
  iq = theorem.find('q')
  return theorem[:iq] + '-' + theorem[iq:] + '-'

def is_axiom(s):
  match = axiom_pattern.match(s)
  if match:
    return match.groups()[0] == match.groups()[1]
  return False

def is_theorem(s):
  match = theorem_pattern.match(s)
  if match:
    g = match.groups()
    return len(g[0]) + len(g[1]) == len(g[2])
  return False

if __name__ == '__main__':
  # make a basic axiom
  a1 = make_axiom(1)
  print a1, is_axiom(a1), is_theorem(a1)

  # use the rule to find another theorem
  t2 = next_theorem(a1)
  print t2, is_axiom(t2), is_theorem(t2)

  # Test a random axiom
  ra = make_axiom(random.randint(0, 100))
  print is_axiom(ra), is_theorem(ra)
  rt = next_theorem(ra)
  print is_axiom(rt), is_theorem(rt)

  # Test an an arbitrary string
  print is_axiom('-pq-')
