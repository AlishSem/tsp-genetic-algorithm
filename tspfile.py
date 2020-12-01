import random
import math
import numpy as np
import sys
import csv

infile = sys.argv[1]
population = sys.argv[2]
count = sys.argv[3]
with open(infile, 'r') as f:
    name = f.readline().strip().split()[1]
    comment = f.readline().strip().split()[1]
    fileType = f.readline().strip().split()[1]
    dim = f.readline().strip().split()[1]
    EdgeWeightType = f.readline().strip().split()[1]
    f.readline()
    coordinates = []
    for i in range(int(dim)):
        a = f.readline().strip().split()[1:]
        a[0] = float(a[0])
        a[1] = float(a[1])
        coordinates.append(a)
    f.close()



def findfit(p,record):
    global best
    for i in range(len(p)):
        d = finddis(coordinates, p[i])
        if d<record:
            record = d
            best = p[i]
        f[i] = 1/ (math.pow(d,16)+1)

def draw(array, prob):
    ind = 0
    r = random.random()
    while(r>0):
        r = r - prob[ind]
        ind +=1
    return array[ind-1]


def finddis(points, order):
    s = 0
    for i in range(len(order)-1):
        firstcityind = order[i]
        firstcity = points[firstcityind]
        secondcityind = order[i+1]
        secondcity = points[secondcityind]
        d = math.sqrt(sum([(a-b)**2 for a,b in zip(firstcity,secondcity)]))
        s+=d
    return s

def normfit(f):
    s = 0
    for i in range(len(f)):
        s += f[i]
    for i in range(len(f)):
        f[i] = f[i] / s

def mutate(order,rate):
    for i in range(cities):
        if random.random()<rate:
            a = math.floor(len(order)*random.random())
            b = math.floor(len(order)*random.random())
            order[a], order[b] = order[b], order[a]

def crossover(ordA, ordB):
    s = math.floor(random.random()*len(ordA))
    e = math.floor(random.randint(s+1, len(ordA)))
    new = list(ordA[s:e])
    for i in range(len(ordB)):
        c = ordB[i]
        if c not in new:
            new.append(c)
    return new

def nextgen():
    global p,f
    newp = [0]*len(p)
    for i in range(len(p)):
        firstord = draw(p,f)
        secondord = draw(p,f)
        ord = crossover(firstord,secondord)
        mutate(ord,001)
        newp[i] = ord
    p = newp







order = [0]*len(coordinates)
p = [0]*int(population)
f = [0]*int(population)
best = [0]
cities = len(coordinates)
record = math.inf
for i in range(len(coordinates)):
    order[i] = i
for i in range(len(p)):
    p[i] = np.random.permutation(order)
findfit(p,record)
normfit(f)
c = 0
while c != int(count):
    nextgen()
    findfit(p,record)
    normfit(f)
    c+=1
print(finddis(coordinates,best))
with open('solution.csv', 'w', newline = '') as file:
    w = csv.writer(file)
    w.writerows([hit] for hit in best)
































