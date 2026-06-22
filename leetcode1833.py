costs = [1,6,3,1,2,5]
coins = 20
costs = sorted(costs)
p=[costs[0],]
h=costs[0]
for i in range(0,len(costs)-1):
    h=h+costs[i+1]
    p.append(h)
    i+=1
ans = len(costs)
for i in range(len(p)):
    if p[i] > coins:
        ans = i
        break

print(ans)