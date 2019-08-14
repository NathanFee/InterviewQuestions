def sock_merchant(sock_pile):
    colors = []
    pairs = 0
    for sock in sock_pile:
        if sock not in colors:
            colors.append(sock)
            pairs += int(sock_pile.count(sock)/2)
    return pairs


print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))

