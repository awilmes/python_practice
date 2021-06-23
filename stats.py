def calculateMedian(x):
    n = len(x)
    index = n // 2
    # if index is even...
    if n % 2 == 0:
        x1 = index - 1
        m = (x[index] + x[x1]) / 2
    else:
        m = index
        m = x[m]
    return m

def calculateMode(x):
    modeDict = {}
    for i in set(x):
        modeDict[i]=x.count(i)
    v = list(modeDict.values())
    k = list(modeDict.keys())
    return k[v.index(max(v))]

def calculateMean(x):
    m = sum(x) / len(x)
    return round(m, 2)

def main():
    #x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    x = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7]
    return calculateMean(x), calculateMedian(x), calculateMode(x)