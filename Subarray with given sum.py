#cod
t=int(input())
for i in range(t):
    n,k=list(int(x) for x in input().split())
    arr=list(int(x) for x in input().split())
    def m(arr,k):
        n=len(arr)
        i=0
        res=0
        j=0
        while i<len(arr):
            res+=arr[i]
            while res>=k:
                if res==k:
                    print(j+1,i+1)
                    return
                else:
                    res-=arr[j]
                    j+=1
            i+=1
        print(-1)
    m(arr,k)


'''
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5
'''
