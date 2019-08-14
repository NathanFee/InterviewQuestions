from functools import cmp_to_key


class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f'{self.name} {self.score}'

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            return -1 if a.name < b.name else 1


names = ['charlie', 'abby', 'bob', 'derek']
players = []

for x in names:
    players.append(Player(x, names.index(x)))

players.append(Player('amy', 3))

for player in players:
    print(player)
print()

players.sort(key=cmp_to_key(Player.comparator))

for player in players:
    print(player)

    # # DEFINE A SORT METHOD
    # def sort_item(item):
    #     return item[1]
    #
    # items.sort(key=sort_item)
    # print(items)
    #
    # # LAMBDA FUNCTION
    # items.sort(key=lambda item: item[1], reverse=True)
    # print(items)
