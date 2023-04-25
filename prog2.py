a=[]
n=input("Enter the number of numbers:")
for i in range(1,n+1):
	l=input("Enter the number:")
	l=l**3
	a.append(l)
print a
pos=[]
neg=[]
zero=[]
for i in a:
	if i>0:
		pos.append(i)
	
	elif i<0:
		neg.append(i)
	else:
		zero.append(i)
	
print pos
print len(pos)
print neg
print len(neg)
print zero
print len(zero)

