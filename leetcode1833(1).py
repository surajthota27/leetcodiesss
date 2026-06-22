costs = [1,3,2,4,1]
coins = 7
#[1,1,2,3,8]
costs.sort()
count=0
for x in costs:
    coins=coins-x
    if coins<0:
        break
    count+=1
print(count)