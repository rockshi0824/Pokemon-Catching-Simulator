import math

#Class to determine whether pokemon was hit, close, or miss using distance and health of pokemon
class SunMoon(object):
    def __init__(self, pokemon):
        self.n = pokemon[0]
        self.x = pokemon[1]
        self.y = pokemon[2]
        self.radius = pokemon[3]
        self.health = pokemon[4]
    
    def check(self, ballx, bally):
        if math.sqrt((ballx - self.x)**2 + (bally - self.y)**2) < self.radius:
            return 'hit'
        elif math.sqrt((ballx - self.x)**2 + (bally - self.y)**2) < self.radius + 5:
            return 'close'
        else:
            return 'miss'

#Reads file containing pokemon location
pokefile = input('File name => ')
print(pokefile)
file = open(pokefile, 'r')
pokenum = int(file.readline().strip())

pokemon = []

i = 0
while i < pokenum:
    a = file.readline().strip()
    a = a.split('|')
    a[1] = int(a[1])
    a[2] = int(a[2])
    a[3] = int(a[3])
    a[4] = int(a[4])
    pokemon.append(a)
    i += 1

for a in pokemon:
    print("{}: ".format(a[0]).rjust(14) + "({},{},{}) Health: {}".format(a[1], a[2], a[3], a[4]))
print()    
    
trainermoves = []
for a in file:
    a = a.strip()
    a = a.split('|')
    a[1] = int(a[1])
    a[2] = int(a[2])
    trainermoves.append(a)

num_caught = dict()

i = 0
while len(pokemon) >= 1 or len(trainermoves) > 0:
    if len(pokemon) <= 0:
        break
    if len(trainermoves) <= 0:
        break
    if not trainermoves[0][0] in num_caught.keys():
        num_caught[trainermoves[0][0]] = [0,[]]
    op = len(pokemon)
    for a in pokemon:
        c = SunMoon(a)
        b = c.check(trainermoves[0][1],trainermoves[0][2])
        if b == 'hit':
            a[4] -= 2
            if a[4] <= 0:
                a[4] = 0            
            print("{} throws a pokeball to position ({}, {}) hits {}:".format(trainermoves[0][0], trainermoves[0][1], trainermoves[0][2], a[0]))
            print("{}".format(a[0]).rjust(12)+": ({},{},{}) Health: {}".format(a[1], a[2], a[3], a[4]))
            if a[4] == 0:
                a[4] = 0
                print("{} is caught!".format(a[0]))
                num_caught[trainermoves[0][0]][0] += 1
                num_caught[trainermoves[0][0]][1].append(a[0])
                pokemon.remove(a)
        elif b == 'close':
            a[4] -= 1
            if a[4] <= 0:
                a[4] = 0            
            print("{} throws a pokeball to position ({}, {}) hits {}:".format(trainermoves[0][0], trainermoves[0][1], trainermoves[0][2], a[0]))
            print("{}".format(a[0]).rjust(12)+": ({},{},{}) Health: {}".format(a[1], a[2], a[3], a[4]))            
            if a[4] == 0:
                a[4] = 0
                print("{} is caught!".format(a[0]))
                num_caught[trainermoves[0][0]][0] += 1
                num_caught[trainermoves[0][0]][1].append(a[0])
                pokemon.remove(a)
        else:
            i+=1
    if i == op:
        print("{} misses at ({}, {})".format(trainermoves[0][0], trainermoves[0][1], trainermoves[0][2]))
    i = 0
    trainermoves.pop(0)

if len(pokemon) == 0:
    print()
    print("All pokemon caught, results:")
    for a in sorted(num_caught):
        print("{} caught {} pokemon".format(a,num_caught[a][0]))
        for a in num_caught[a][1]:
            print(a.rjust(12))
elif len(trainermoves) == 0:
    print()
    print("Players run out of pokeballs, results:")
    for a in sorted(num_caught):
        print("{} caught {} pokemon".format(a,num_caught[a][0]))
        for a in num_caught[a][1]:
            print(a.rjust(12))        
