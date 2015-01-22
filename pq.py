# Chapter 2: The pq-system

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

# make a basic axiom
a1 = make_axiom(1)
print a1

# use the rule to find another theorem
t2 = next_theorem(a1)
print t2
