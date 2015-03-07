T = input()
blank = raw_input()

for x in range(T):
    line = raw_input().split()
    W = int(line[0])
    R = int(line[1])
    M = int(line[2])
    S = int(line[3])
    
    print 'Case #' + str(x + 1) + ':'
    
    if (R < 40 or W < 35) and M < 10:
        print 'EMERGENCY'
    elif M < 10 and R > 60 and M < 10:
        print 'NIGHTMARE'
    elif S > 28800 and M < 10:
        print 'WAKE-UP'
    else:
        print 'NOTHING'

    try:
        blank = raw_input()
    except:
        pass
