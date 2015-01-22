# Chapter 1 The MU-Puzzle
import re

def r1(s):
  if s[-1] == 'I':
    return [s + 'U']
  else:
    return []

def r2(s):
  if s[0] == 'M':
    return [s + s[1:]]
  else:
    return []

def r3(s):
  return [s[:m.start()] + 'U' + s[m.start() + 3:] for m in
      re.finditer('(?=III)', s)]

def r4(s):
  return [s[:m.start()] + s[m.start() + 2:] for m in
      re.finditer('(?=UU)', s)]

fns = [r1, r2, r3, r4]

# Example:
# search('MI', MIIU')
#
# This way madness lies:
# search('MI', 'MU')
def search(axiom, goal):
  i = 0
  collection = {axiom: []} 
  while not collection.has_key(goal):
    i += 1
    print i, 'collection size:', len(collection)
    cprime = {}
    for s in collection:
      path = list(collection[s])
      path.append(s)
      for fn in fns:
        sprimes = fn(s)
        for sprime in sprimes:
          if sprime == goal:
            return path
          if not collection.has_key(sprime):
            cprime[sprime] = path
    collection = cprime
