import random
statArray = random.choices([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0.1, 0.3, 0.8, 1.6, 2.9, 4.8, 7, 9.4, 11.4, 12.9, 13.3, 12.3, 10.1, 7.3, 4.2, 1.6], k=6)
statName = ["Strength ","Dexterity ","Constitution ","Intelligence ","Wisdom ","Charisma "]
file=open("RandomCharacter.txt",'w')
for i,j in zip(statArray, statName):
    file.write(j + str(i)+"\n")
file.close()
