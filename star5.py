N=5
for i in range(1,N+1):
  for j in range(N+1-i):
    print(" ",end="")
  for j in range(2*i-1):
    print("*",end="")
  print()
