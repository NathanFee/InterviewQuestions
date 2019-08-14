items = [
    ("a", 90),
    ("b", 13),
    ("c", 150),
    ("d", 1),
    ("f", 20),
    ("e", 20),
]


# DEFINE A SORT METHOD
def sort_item(item):
    return item[1], item[0]


items.sort(key=sort_item)
print(items)

# # LAMBDA FUNCTION
# items.sort(key=lambda item: item[1], reverse=True)
# print(items)
