k=0
j=0
for i in range(101):
    if i%2==0:
        k=k+i
    else:j=j+i
print('The sum of all evens is '+str(k)+'. And the sum of all odds is '+str(j))