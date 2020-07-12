zork=0             #COUNTING THINGS
print("before",zork)
for i in [10,50,30,78,20]:
    zork=zork+1
    print(zork,i)
print("after",zork)


zerk=0               #THIS GIVES ADDITION
print("before",zerk)
for i in [10,50,30,78,20]:
    zerk=zerk+i
    print(zerk,i)
print("after",zerk)


sum=0                #THIS GIVES AVERAGE
count=0
print("Before",count,sum)
for value in [10,50,20,70,60]:
    count=count+1
    sum=sum+value
    print(value,count,sum)
print("After",value,count,sum/count)


found=False  #USING BOOLEAN
print('Before',found)
for value in [10,78,56,90,88,60]:
    if value==90:
        found=True    #AT 90 THE FOUND BECOMES TRUE THEREFORE AFTER 90 ALL THAT BECOMES TRUE
    print(found,value)
print('After',found)

smallest=None
print('Before')
for value in [10,89,56,44,3,2]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest,value)
print('after',smallest)
