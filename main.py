"""
  main.py
    - initialize chromosomes
    - display generations
  ---
  by Wistan Chou (Jan 2016)
"""

from string import printable
from random import choice, randint

def cost(c, a):
  # calculates the distance of chromosome c to goal a
  # using the square of the ascii distance
  cost = 0
  for i in range(len(a)):
    cost += (ord(c[i])-ord(a[i]))**2
  return cost

def generator(length):
  # generates a single chromosome
  bases = printable[:-5]
  chromosome = ""
  for i in range(length):
    chromosome += choice(bases)
  return chromosome

def initialize(n, l, answer):
  # create n random chromosomes of length l
  pop = []
  for i in range(n):
    chrom = generator(l)
    score = cost(chrom, answer)
    C = [chrom, score]
    pop.append(C)
  return pop

def sort(ls):
  for i in range(1, len(ls)):
    cur = ls[i]
    while i > 0 and ls[i-1][1] > cur[1]:
      ls[i] = ls[i-1]
      i -= 1
    ls[i] = cur

def date(ls, answer):
  length = len(ls)
  fit = ls[:length/2]
  if len(fit)%2 == 1:
    fit = fit[:-1]
  children = []
  # round one
  for i in range(0, len(fit), 2):
    children.extend(mate(fit[i], fit[i+1], answer))
  # round two
  for i in range(len(fit)/2):
    children.extend(mate(fit[i], fit[-i], answer))
  return children

def mate(a, b, answer):
  # random crossover point (seems to work better than midpoint)
  point = randint(1,len(a[0])-2)
  # midpoint crossover
  # point = len(a[0])/2
  c1 = a[0][:point]+b[0][point:]
  c2 = b[0][:point]+a[0][point:]
  return [[c1, cost(c1, answer)],[c2, cost(c2, answer)]]

def display(g, ls):
  print "Generation: %d" % g
  for i in ls:
    print i

def mutate(c, answer):
  pos = randint(0, len(c[0])-1)
  char = choice(printable[:-5])
  new = c[0][:pos]+char+c[0][pos+1:]
  return [new, cost(new, answer)]

def environment(Tprob, ls, answer):
  Fprob = 100-Tprob
  poss = []
  for i in range(Tprob):
    poss.append(True)
  for i in range(Fprob):
    poss.append(False)
  for i in range(len(ls)):
    if choice(poss):
      ls[i] = mutate(ls[i], answer)
  return ls

def main():
  # initialize population and store starting chromosomes in list_population
  answer = "Swarthmore College, 500 College Avenue, PA 19081"
  popSize = 20
  chromLength = len(answer)
  mutateProb = 43
  population = initialize(popSize, chromLength, answer)
  sort(population)
  genCount = 0
  done = False
  display(genCount, population)
  raw_input("go?")

  while not done:
    genCount += 1
    population = date(population, answer)
    population = environment(mutateProb, population, answer)
    sort(population)
    display(genCount, population)
    for i in population:
      if i[1] == 0:
        done = True

if __name__=="__main__":
  main()
