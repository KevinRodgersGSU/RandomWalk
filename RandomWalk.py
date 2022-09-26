import random
RepeatTest = 10
total_runs= 25
N = 2500
NumberOfContaminants = 5
totalInfected = 0
totalDistance = 0
InfectX = []
InfectY = []
for i in range(NumberOfContaminants):
  InfectX.append(random.randint(1, 100))
  InfectY.append(random.randint(1, 100))
for repeat in range(1,RepeatTest +1):
  BecameInfected = 0
  Distance = 0
  for Run in range(1, total_runs+ 1):
    Current = BecameInfected
    Px = 50
    Py = 50
    Steps = 0
    while (Steps <= N):
      R = random.random()
      if R < 0.25 and Px>1:
        Px -= 1
      elif R < 0.5:
        if Px==100:
          Px -= 2
        Px += 1
      elif R < 0.75 and Py>1:
        Py -= 1
      else:
        if Py==100:
          Py -= 2
        Py += 1
      for i in range(len(InfectX)):
        if(Px == InfectX[i] and Py == InfectY[i] and Current == BecameInfected):
          BecameInfected += 1
          break 
      if(Current != BecameInfected):
        Distance += ((((50 - Px )**2) + ((50-Py)**2) )**0.5)/Steps
        break
      elif(Steps==N):
        Distance += ((((50 - Px )**2) + ((50-Py)**2) )**0.5)/Steps
      Steps += 1
  totalDistance += Distance/total_runs
  totalInfected += BecameInfected/total_runs
  print("Run:",repeat,"Steps:",N,"totalInfected",BecameInfected/total_runs,"totalDistance",Distance/total_runs)
  #N += 5000
print(totalDistance/RepeatTest)
print(totalInfected/RepeatTest)
