A=set(map(str, input('definiti elemente pentru multimea A:').upper()))
B=set(map(str, input('definiti elemente pentru multimea B').upper()))
print('a)', A.intersection(B))
print('b)', A.union(B))
print('c)', A.difference(B))
print('c0)', B.difference(A))