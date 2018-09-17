
def iterfibo(n):
    answer = 0
    n1 = 0
    n2 = 1
    if n == 1:
        answer = 0
    elif n == 2:
        answer = 1
    for i in range (3,n+1):
        answer = n1 + n2
        n1 = n2
        n2 = answer
    return answer

nbr = int(input("Please Enter the number:"))
print(iterfibo(nbr))