def reverse_list(x):
    l=[]
    i=len(x)
    while i>0:
        l.append(x[i-1])
        i=i-1
    return l
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))