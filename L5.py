RANGE = []
VALUES = []

def process_ing():
    FRESH = 0
    SPOILED = 0

    for val in VALUES:
        is_fresh = False
        for rng in RANGE:
            begin = rng[0]
            stop = rng[1]
            if begin <= val <= stop:
                is_fresh = True
                break

        if is_fresh:
            FRESH += 1
            print(f"Total FRESH ingedients: {FRESH}")
        else:
            SPOILED += 1
            print(f"Total SPOILED ingredients: {SPOILED}")
    print(f"\nFinal Counts: FRESH: {FRESH}, SPOILED: {SPOILED}")

def main():
    with open('d2input.txt', 'r') as fl:
        for line in fl:
            line = line.strip()
            if '-' in line:
                start, end = map(int, line.split('-'))
                RANGE.append((start, end))
            elif len(line) > 0:
                VALUES.append(int(line))
    process_ing()

if __name__ == '__main__':
    main()