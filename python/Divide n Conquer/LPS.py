def findLPS(s,startindex,endindex):
    if startindex>endindex:
        return 0
    elif startindex==endindex:
        return 1
    elif s[startindex]==s[endindex]:
        return 2 + findLPS(s,startindex+1,endindex-1)
    else:
        op1 = findLPS(s,startindex,endindex-1)
        op2 = findLPS(s,startindex+1,endindex)
        return max(op1,op2)

print(findLPS("ELRMENMET",0,8))