dig=input('Enter a digit:')
try:
    idig=int(dig)
except:
    idig=-1

if idig>0:
    print('Nice work')
else:
    print('not a number')
exit()

#output
#Enter a digit:24
#Nice work
#Enter a digit:twenty
#not a number
