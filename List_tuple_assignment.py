'''
Q1) Create list called "even", store all the even numbers, in the range of 1 to 20.
'''
even = [x for x in range(1,21) if x%2==0]
print(even)
'''
Q2) Create list called "odd", store all the odd numbers, int the range of 1,20.
'''
odd = [x for x in range(1,21) if x%2!=0]
print(odd)

'''
Q3) Take "even" and "odd" list  from previous solution, merge it in new list called "numbers" and sort it.
'''
numbers=even+odd
numbers.sort()
print(numbers)

'''
Q4) Create a nested list for called "Students" for 5 student, each index store the student information. ex.. ["name",roll,marks].
'''
Students =[["Azeem",12,78],["Ravi",10,88],["Harish",5,93],["Robo",17,94],["Rakesh",4,99]]
print(Students)

'''
Q5) Write a Python program to find the second largest number in a list.
'''
numbers = [9,4,-1,16,55,18,13,-2,10,1]
numbers.sort()
print(numbers[-2])

'''
Q6) WAP to print unique element from list.
     ex... nums = [4,3,5,6,3,4,6]      (o/p:- 5 is unique from list)
'''
nums = [4,3,5,6,3,4,6]
print(end='')
for i in nums:
    if nums.count(i) == 1:
        print(i,"is unique from list")

'''
Q7) Given a tuple of numbers, find the max and min elements.
  ex.. tup = (11,26,45,23,15,18)
'''
tup = (11,26,45,23,15,18)
temp_list = list(tup)
temp_list.sort()
tup = tuple(temp_list)
print(f"Min = {tup[0]}, Max={tup[-1]}")

'''
Q8) Retrieve the 'G' from following list using positive indexing
       L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]
'''
L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]

print(L1[3][2][2][1][1])

'''
Q9) WAP to retrieve the 'Sweet' string from the following nested list using Positive indexing
       L2 = [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet', 'Wheat']]], 7065, 5, 2034, [1, 2]]
'''
L2 = [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet', 'Wheat']]], 7065, 5, 2034, [1, 2]]
print(L2[1][2][1][2])

'''
Q10) WAP to extract 'Bengaluru' in reverse order using negative indexing from following string
      s2 = 'Hello I am going to Bengaluru How are you doing?'
'''
s2 = 'Hello I am going to Bengaluru How are you doing?'
print(s2[-28:-19])
print(s2[-20:-29:-1]) #reverse
