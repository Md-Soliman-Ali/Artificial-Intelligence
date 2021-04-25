import collections
print("Nested list")
list = ["1", "2", "3", "4", "5", "6",['nested1','nested2','nested3']]
print(list)
print("\nLength : ")
print("Length of main list: ",len(list))
print("Length of nested list: ",len(list[6]))

print("\nConcatenation : ")
list1 = ["X", "Y" , "Z"]
list2 = [7, 8, 9]

list3 = list1 + list2

print("First list: ",list1)
print("Second list: ",list2)
print("Concatenation",list3)

print("\nMembership : ")
a = 100
b = 200
list = [200, 300];

print("Membership List: ",list)
if ( a in list ):
   print("Line 1 - a(",a,") is available in the given list")
else:
   print("Line 1 - a(",a,") is not available in the given list")

a = 200
if ( a in list ):
   print("Line 3 - a(",a,") is available in the given list")
else:
   print("Line 3 - a(",a,") is not available in the given list")
   
print("\nIteration")
list = ["A", "B", "C", "D", "E", "F"]
for i in list:
        print("List's element: ",i)
        
print("\nIndexing")
list = ["A", "B", "C", "D", "E", "F"]
      
for i in list:
        print("Index of ",i, "is ",list.index(i))
            
print("\nSlicing")
list = ["A", "B", "C", "D", "E", "F"]
print("Initial list: ",list)
sliced_list = list[1:4]
print("Spliced list position 1 to 4: ",sliced_list)
            
            