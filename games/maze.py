import pew


level = [
    [3, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 2],
]

pew.init()
screen = pew.Pix.from_iter(level)
pew.show(screen)
