def squaresum(n):
    return (n * (n + 1) / 2) * (2 * n + 1) / 3
  
# main()
n = 4
print(squaresum(n));

X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
  
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
result = [[X[i][j] + Y[i][j]  for j in range
(len(X[0]))] for i in range(len(X))]
  
for r in result:
    print(r)