RANGE = []
VALUES = []

FRESH = 0
SPOILED = 0

with open('d2input.txt', 'r') as fl:
    for line in fl:
        line = line.strip()
        if '-' in line:
            start, end = map(int, line.split('-'))
            RANGE.append((start, end))
        elif len(line) == 0:
            pass
        else:
            line = int(line)
            VALUES.append(line)

  
#print(RANGE[:5])
#print(VALUES[1:6])

for rng in RANGE:
    for i in VALUES:
        print(type(rng)
        print(range(rng))

#print(FRESH)
#print(SPOILED)





#print(RANGE[:5])
#print('=' * 100)
#print(VALUES[1:6])
    