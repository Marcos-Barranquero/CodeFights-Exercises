# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
each statue having an non-negative integer size. Since he likes to make things perfect,
he wants to arrange them from smallest to largest so that each statue will be
bigger than the previous one exactly by 1. He may need some additional statues to be
able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.

"""

# Code


def makeArrayConsecutive2(statues):
    l = min(statues)
    r = max(statues)
    rango = []
    for i in range(l + 1, r):
        rango.append(i)
    print(rango)

    cont = 0
    for i in range(0, len(rango)):
        print(i)
        if (not (rango[i]) in statues):
            cont += 1
    return cont
