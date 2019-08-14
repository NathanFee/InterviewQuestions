def counting_valleys(s):
    elevation = 0
    valleys_count = 0
    for x in s:
        if x == 'U':
            elevation += 1
            if elevation == 0:
                valleys_count += 1
        else:
            elevation -= 1
    print(valleys_count)


trip = 'UDDDUDUU'

counting_valleys(trip)
