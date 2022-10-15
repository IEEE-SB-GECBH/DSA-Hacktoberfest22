def numberfactor(n):
    if n in (0,1,2):
        return 1
    elif n==3:
        return 2
    else:
        subP1=numberfactor(n-1)
        subP2=numberfactor(n-3)
        subP3=numberfactor(n-4)
    return subP1+subP2+subP3

print(numberfactor(5))