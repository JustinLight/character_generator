import random
import glob2
import math
d={}
randomfile=glob2.glob('class_'+random.choice(["fighter", "wizard"])+'.txt').pop()
with open(randomfile) as f:
    for line in f:
        (key, val) = line.split()
        d[key] = val

statArray = random.choices([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0.1, 0.3, 0.8, 1.6, 2.9, 4.8, 7, 9.4, 11.4, 12.9, 13.3, 12.3, 10.1, 7.3, 4.2, 1.6], k=6)
statName = ["Strength ","Dexterity ","Constitution ","Intelligence ","Wisdom ","Charisma "]
statBonus =[]
for i in statArray:
    statBonus.append(math.floor((i-10)/2))

file=open("RandomCharacter.txt",'w')
file.write('Class '+d['class']+"\n")
hp=int(d['hit-points']) + int(statBonus[2])
file.write('Hit points '+ str(hp)+'\n')
for i,j,k in zip(statArray, statName, statBonus):
    file.write(j + str(i)+" "+str(k)+"\n")
file.close()
