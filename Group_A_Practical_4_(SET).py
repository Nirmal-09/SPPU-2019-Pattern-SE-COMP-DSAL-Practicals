s1=set()
s2=set()
def create(a) :
	s3=a
	n=int(input("Enter the no. of elements in a set : "))
	for i in range(0,n):
		e=int(input(f"Enter the element no. {i+1} for set :- "))
		s3.add(e)
	print(s3)
	
def remove(a):
	s3=a
	e=int(input("Enter the element which has to be removed :-  "))
	s3.remove(e)
	print(s3)
	
def add(a):
	s3=a
	e=int(input("Enter the element which has to be added :- "))
	s3.add(e)
	print(s3)
	
def search(a):
	s3=a
	e=int(input("Enter the element which has to be Searched :- "))
	if e in s3 :
		print(f"Element is present in the set !!")
	else:
		print("Element is not present in the set !!")
	

def size():
	print(f"The size of set is {len(s1)} ")
	
def	intersection():
	i=s1.intersection(s2)
	print(i)
	
def union():
	u=s2.union(s1)
	print(u)

def difference():
	d=s1.difference(s2)
	print(d)

def subset():
	s=s2.issubset(s1)
	if s == 1 :
		print("Given set is subset of First")
	else:
		print("Given set is not subset of First")

a=1
while (a==1) :
		print("\n\n ***********************MENU**************************")
		print("1. Create a set ")
		print("2. Add a Element in the set")
		print("3. Remove a element from the set")
		print("4. Search for an element in the set ")
		print("5. Find the Size of the set")
		print("6. Perform Intersection of the sets ")
		print("7. Perform Union of the sets ")
		print("8. Perform Difference Operation on the set")
		print("9. Find if any set is subset of another ")
		print("10. EXIT!!")
		
		choice=int(input("Enter Your choice :- "))
		
		if choice==1 :
			print("***FOR SET FIRST*** ")
			create(s1)
			print("***FOR SET SECOND***")
			create(s2)
				
		elif choice==2 :
			print("1. Add element in set 1")
			print("2. Add element in set 2")
			choice=int(input("Enter your choice :- "))
			if choice==1:
				add(s1)
			elif choice==2:
				add(s2)
				
		elif choice==3:
			print("1. Remove element from set 1")
			print("2. Remove element from set 2")
			choice=int(input("Enter your choice :- "))
			if choice==1:
				remove(s1)
			elif choice==2:
				remove(s2)
								
		elif choice==4:
			print("1. Search element from set 1")
			print("2. Search element from set 2")
			choice=int(input("Enter your choice :- "))
			if choice==1:
				search(s1)
			elif choice==2:
				search(s2)
