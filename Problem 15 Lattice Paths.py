"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

						---Cant get image here---

How many such routes are there through a 20×20 grid?
"""
N=21
sol =[]
for i in range(N):
	sol.append([0]*N)


for i in range(N):
	for j in range(N):
		if (i==0 or j==0):
			sol[i][j]=1
		else:
			sol[i][j]=sol[i-1][j] + sol[i][j-1]
		#print(i,j)
		#for k in sol:
		#	print(k)
print(sol[20][20])


## Genereates Pascals traingle
## FeelsGoodMan to revisit Dynamic Programming