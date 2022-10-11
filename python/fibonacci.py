def fibonacci_number(n):
    l=[0,1]
    for i in range(2,n+1):
        l.append(l[i-1]+l[i-2])
    return l[n]
if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))