T = input()
lines = raw_input().split()

for x in range(T):
    n = raw_input()
    shape = raw_input()

    winners = 0
    high = 0
    for l in shape:
        wins = 0
        if l == 'R':
            wins = shape.count('S')
        elif l == 'P':
            wins = shape.count('R')
        elif l == 'S':
            wins = shape.count('P')

        if wins > high:
            high = wins
            winners = 1
        elif wins == high:
            winners += 1
    print 'Case #' + str(x + 1) + ':'
    print winners
    try:
        blank = raw_input()
    except:
        pass
