def solution(l1, l2)-> list:
    x = 0
    y = 0
    result=[]
    while (x < len(l1)) and (y < len(l2)):
        if l1[x]<=l2[y]:
            result.append(l1[x])
            x+=1
        else:
            result.append(l2[y])
            y+=1
    if x < len(l1):
        result+=l1[x:]
    else:
        result+=l2[y:]
    return result

list1=[3,6,8,10]
list2=[1,2,4,7]
print(solution(list1,list2))
