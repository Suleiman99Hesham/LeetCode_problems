result = []
A = [1,2,1,4,3]
B = [3,5]
for i in B:
    counter = 0
    for j in A :
        if j <= i:
            counter+=1
    result.append(counter)
    counter = 0
print(result)