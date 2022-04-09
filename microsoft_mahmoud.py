def solution(compinedlist: list)-> list:
    compinedlist.sort()
    found={}
    result=[]
    for item in compinedlist:
        rem=item//2
        if rem in found and item%2==0:
            result.append(rem)
            found.pop(rem)
        else:
            found[item] = 1
    if found:
        return []
    result.sort()
    return result

print('test1:',solution([1,3,4,2,6,8]))
print('test2:',solution([6,3,0,1]))
print('test3:',solution([0,1,0,2]))
print('test4:',solution([0,1,0,2,0]))
