__author__ = 'WiktorMarchewka'

# height = 17
drawer = []

def evenHeight(height):
    for x in reversed(range(1, height+1)):
        while (len(drawer) <= height):
            drawer.extend(' ')
        try:
            drawer[(-x)] = 'dupa'
            drawer[x] = 'dupa'
        except IndexError:
            break
        print " ".join(str(e) for e in drawer)
        # print drawer
        del drawer[:]

# evenHeight(10)
evenHeight(2)



