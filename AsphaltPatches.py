# def Solution(S):
#     patches = 0
#     for char in S:
#         i = S.find('X')
#         if "X" in S:
#             patches += 1
#             S = S[:i] + S[i+3:]
#     print(patches)

def Solution(S):
    patches = 0
    i = 0
    N = len(S)
    
    while i < N:
        if S[i] == 'X':
            patches += 1
            i += 3
        else:
            i += 1
    
    print (patches)

Solution(".X..X")
Solution("X.XXXXX.X.")
Solution("XX.XXX..")
Solution("XXXX")
Solution('.X...XX')


