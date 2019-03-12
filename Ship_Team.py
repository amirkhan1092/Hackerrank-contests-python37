def two_teams(sailors):
    #replace this for solution
    k = []
    l = []
    for name in sailors:
        if sailors[name]<20 or sailors[name]>40:
            l.append(name)
        else:
            k.append(name)
    l.sort()
    k.sort()
    return [
        l,
        k
    ]

if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert two_teams({
    #     'Smith': 34,
    #     'Wesson': 22,
    #     'Coleman': 45,
    #     'Abrahams': 19}) == [
    #         ['Abrahams', 'Coleman'],
    #         ['Smith', 'Wesson']
    #         ]
    #
    # assert two_teams({
    #     'Fernandes': 18,
    #     'Johnson': 22,
    #     'Kale': 41,
    #     'McCortney': 54}) == [
    #         ['Fernandes', 'Kale', 'McCortney'],
    #         ['Johnson']
    #         ]
