n=int(input('Enter the limit: '))
a=0
b=1
print(a,b, end=" ")
for _ in range(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=' ')
print("\n ")
print("\nThe Fibonacci series is printed.")
