'''
1)Iterate 0 to 10 using for loop, do the same using while loop.
'''
for i in range(11):
    print(i,end=" ")
print()
#While Loop
i =0 
while i < 11:
    print(i,end=" ")
    i+=1
print("\n")

'''
2)Iterate 10 to 0 using for loop, do the same using while loop.

'''
i =11
for x in range(i):
    print(i-x-1,end=" ")
print()

# (or)
#for x in range(10,-1,-1):
#    print(x,end=' ')

i =10 
while i >= 0:
    print(i,end=" ")
    i-=1
    
print("\n")

'''
3)Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''
for x in range(7):
    print("# # # # # # # #")
print("\n")

'''
4)Use nested loops to create the following:
      #
     ###
    #####
   #######
  #########
 ###########
#############
'''

#n = int(input("Enter your vale:"))
n=7
star  = 1
space = n

for x in range(n):
    for y in range(space):
        print(" ",end="")
    for z in range(star):
        print("#",end="")
    print()
    space -=1
    star = star +2
print("\n")
'''
5)Print the following pattern using loops
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
'''
for i in range(11):
    print(f"{i} x {i} = {i*i}")
   
print("\n")
'''
6)Iterate through the list, ['Python', 'Numpy','Pandas','Scikit', 'Pytorch'] using a for loop and print out the items.
'''
items = ['Python', 'Numpy','Pandas','Scikit', 'Pytorch']

for it in items:
    print(it)
print()

'''
7)Use for loop to iterate from 0 to 100 and print only even numbers
'''
for i  in range(0,100):
    if i%2 == 0:
        print(i,end=" ")
print("\n")
        
'''
8)Use for loop to iterate from 0 to 100 and print only odd numbers
'''
for i  in range(0,100):
    if i%2 != 0:
        print(i,end=" ")
print("\n")
'''
9)Use for loop to iterate from 0 to 100 and print the sum of all numbers.
'''
sumnum=0
for i  in range(0,100):
    sumnum+=i
print("Sum of all number[0-100] =",sumnum)
print("\n")
    
'''
10)Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
'''
evensum= 0
oddsum = 0
for i  in range(0,100):
    if i%2 != 0:
        oddsum+=i
    else:
        evensum+=i
print("Even sum=",evensum,"Odd sum=",oddsum)
