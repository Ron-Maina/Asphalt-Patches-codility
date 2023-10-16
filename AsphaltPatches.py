def Solution(S):
    patches = 0
    for char in S:
        i = S.find('X')
        if "X" in S:
            patches += 1
            S = S[:i] + S[i+3:]
    print(patches)

Solution(".X..X")
Solution("X.XXXXX.X.")
Solution("XX.XXX..")
Solution("XXXX")
Solution('.X...XX')

# print(len(S))
    # for i in range(0, len(S), 3):
    #     print([S[i:i+3]])
    #     if "X" in S[i:i+3]:
    #         patches += 1
    # print(patches)
