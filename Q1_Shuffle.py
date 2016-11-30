import random


def shuffle(x):
    a = []
    # continue to select and remove items from original list until empty
    while len(x) > 0:
        # randomly select an item from list
        b = random.choice(x)
        # add to new list
        a.append(b)
        # remove from old list
        x.remove(b)
    return a

print(shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
