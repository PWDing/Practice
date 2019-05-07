def hanoi(n, from_rod, aux_rod, to_rod):
    if n == 1:
        print("Move disk 1 from rod {} to rod {}.".format(from_rod, to_rod))
        return
    if n > 1:
        print("Move {} disk from rod {} to rod {}.".format(n-1, from_rod, aux_rod))
        hanoi(n-1, from_rod, to_rod, aux_rod)

        print("Move disk {} from rod {} to rod {}.".format(n, from_rod, to_rod))

        print("Move {} disk from rod {} to rod {}.".format(n-1, aux_rod, to_rod))
        hanoi(n-1, aux_rod, from_rod, to_rod)


print(hanoi(5, 'a', 'b', 'c'))
