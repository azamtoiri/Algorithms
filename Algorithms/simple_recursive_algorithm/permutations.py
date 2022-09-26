# Permutations
"""
Permutations of 'ABC' = 3! = 3 x 2 x 1 = // 6
"""


def permute(sting, pocket=""):
    if len(sting) == 0:
        print(pocket)
    for i in range(len(sting)):
        letter = sting[i]
        front = sting[0:i]
        back = sting[i + 1:]
        together = front + back
        permute(together, letter + pocket)


permute("AFFSDFSDF")
