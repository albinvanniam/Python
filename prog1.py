stock={}
n=input("Enter the number of items:")
for i in range(n):
	a=raw_input("Enter the item name:")
	stock[a]=input("Enter the number of items:")
print stock
h=raw_input("Enter the item to be removed:")
del stock[h]
print stock
k=raw_input("Enter the item name to change the stock:")
for j in stock:
	if j==k:
		u=input("Enter the new stock:")
		stock[j]=u
print stock
