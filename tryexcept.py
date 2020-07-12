#str='hello boo'   #this gives an error thus use try block becoz there was no num in str
#istr=int(str)
#print(istr)

str='hello boo'   #when the first conversion fails it will jump into except block
try:
    istr=int(str)
except:
    istr=-1
print('first',istr)
str='123'      #here it is crct so it will execute try block
try:
    istr=int(str)
except:
    istr=-1
print('second',istr)

#output
#first -1
#second 123
