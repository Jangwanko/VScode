T=int(input())

for i in range(T,T+1):    
    n,m=map(int,input().split())
    if n>=m:
        big=n
        small=m
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
    else:
        big=m
        small=n
        B=list(map(int,input().split()))
        A=list(map(int,input().split()))
    result=-float('inf')
    for time in range(big-small+1):
        max=0
        for j in range(small):
            max+=B[j]*A[j+time]
        if max>result:
            result=max


    print(f"{i} {max}")


    '''n이 m보다 더 적은 경우를 고려하여 리스트의 길이를 이용하여
    A와 B에 입력받은 숫자를 비교한다.
    A의 길이가 더 적으니 A의 대입을 B에 맞춰야함. 
    a[i]b[i+j]로 맞추면 될까 sum을 하여 더 큰값이면 result에 넣기'''
