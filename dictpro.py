students={}
n=input("Enter the number of names:")
for i in range(n):
	roll=input("Enter the roll:")
	students[roll]=raw_input("Enter the name:")
print students
k=input("Enter the roll number to be updated:")
y=raw_input("Enter the new name:")
for j in students:
	if j==k:
		students[j]=y
print students
searname=raw_input("Enter the name to be searched:")
for k,v in students.items():
	if v==searname:
		print k,v
print "Alphabetical order:"
print sorted(students.values())
l=input("Enter the roll no. to be deleted:")
for k,v in students.items():
	if k==l:
		del students[k]
print students 	


