"""
  optimize.py
    - finds the best mutation probability for main.py
  by Wistan Chou (Jan 2016)
"""

from main import *

def run(prob, maxGen):
  answer = "Swarthmore College, 500 College Avenue, PA 19081"
  popSize = 40
  chromLength = len(answer)
  mutateProb = prob
  population = initialize(popSize, chromLength, answer)
  sort(population)
  genCount = 0
  done = False

  while not done and genCount < maxGen:
    genCount += 1
    print ("%d\r" % genCount), 
    population = date(population, answer)
    population = environment(mutateProb, population, answer)
    sort(population)
    for i in population:
      if i[1] == 0:
        done = True

  return genCount


def test():
  maxGen = 5000
  trials = 10
  probs = []
  result = []
  for i in range(31, 47, 2):
    probs.append(i) 
  print probs
  print ""


  for prob in probs:
    pDis = "P:%d%%" % prob
    print pDis
    total = 0
    for i in range(trials):
      r = run(prob, maxGen)
      print ("run %d: %d\r" % (i+1, r))
      total += r
    avg = total/trials
    print "average: %d\n" % avg
    result.append([pDis, avg])

  for item in result:
    print item



test()
