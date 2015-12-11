#Question 1
cube= lambda x : x**3
square= lambda y: y**2

def sumlist(alist,num):
    result=0
    if alist==[]:
        return 0
    else:
        for i in alist:
            result+=num(i)
        return result

#Question 2
def mean(blist):
    def sumlist(alist,zero):
        result=0
        for i in alist:
            result+=i
        return float(result/len(alist))

    if blist==[]:
        return 0
    else:
        return sumlist(blist,0)

#Question 3
def std_dev(clist):
    variance= float((sumlist(clist,lambda x: x**2)/len(clist))-(mean(clist))**2)
    stddev=variance**0.5
    return stddev
