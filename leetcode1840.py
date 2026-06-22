n=3
restrictions=[[0,1],[2,1],[4,1]]
i,j=0,0
x=restrictions[i][j]
for i in restrictions:
    for x,y in i:
        print(x,y)
