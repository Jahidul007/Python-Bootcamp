A = sorted(A, key = lambda x: abs(x))
       d = {}
       eliminate = 0
       for i, num in enumerate(A):
           if not num & 1 and num//2 in d and d[num//2] > 0:
               d[num//2] -= 1
               eliminate += 2
           else:
               d[num] = 1 if num not in d else d[num] + 1
       return (eliminate == len(A))