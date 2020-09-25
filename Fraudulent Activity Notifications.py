import bisect
n,d = map(int,input().split())
exp = list(map(int,input().split()))
arr = sorted(exp[:d])
mid = d//2
median = 0
for i in range(d,n):
    if d % 2 == 0:
        med_arr = sum(arr[mid - 1:mid + 1]) / 2
    else :
        med_arr = arr[int(mid)]
    if exp[i] >= 2*med_arr:
        median+=1
    del arr[bisect.bisect_left(arr,exp[i-d])]
    bisect.insort(arr,exp[i])
print(median)