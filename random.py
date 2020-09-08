import random

# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = random.randint(0,n) 
  
    lst.append(ele) # adding the element 

   
print("ARRAY : ",lst) 
print("MAX IN ARRAY : ",max(lst))
print("MINIMUM : ",min(lst))


average = sum(lst) / len(lst)

print("AVERAGE : " + str(round(average, 2)))