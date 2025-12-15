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
    print(rng)
    begin = rng[0]
    stop = rng[1]
    range_val = range(begin, stop)
    for int in VALUES[1:6]:
        if int in range_val:
            FRESH += 1
            print(f" FRESH COUNT: {FRESH}")
        else:
            SPOILED += 1
            print(f" SPOILED COUNT: {SPOILED}")

#print(FRESH)
#print(SPOILED)






#print(RANGE[:5])
#print('=' * 100)
#print(VALUES[1:6])
    