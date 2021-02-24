def sum_of_odds(x):
    i=0
    for j in range(x+1):
        if j%2!=0:
            i=i+j
    return i
print(sum_of_odds(5))