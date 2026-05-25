n = int(input())
num = 0
while(n>0):
    s = n%10
    num = num*10
    n = n//10
print(num)