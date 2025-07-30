
'''
1. Explain the difference between immutable and mutable types in Python. How does this apply to strings?
'''
#  mutable means content can be modified in runtime 
#    Example:- Arrays,lists,sets, Dictionary values
#  immutable means content can not be modified  
#    Example:- srings,tuples, Dictionary keys

#  we can not change the strings if once we assign. insted concatenate and update object.
#  in background in string classes it will create a new object

''''
2. Describe the role of escape characters in Python strings. Give examples.
'''
#  Escape characters are special characters. combination few characters of will give output that 
#  we can not give as an input
#  Example '\n' => newline
#          '\t' => tab space
#          '\b' => back space

'''
3. Write a Python program that takes a string and removes all vowels.
'''
string = "Write a Python program that takes a string and removes all vowels"
vowel = ['a','e','i','o','u','A','E','I','O','U']
newstr= str()
for c in string:
    if c not in vowel:
        newstr+=c
print(newstr)


'''
3. Given a string, write a program to count the frequency of each character.
'''
string = 'Helloworld'
str_set = set(string)
for c in str_set:
    print(c,"=",string.count(c),end=" ,")
print()

'''    
4. Write a Python program to check if two given strings are anagrams of each other
'''

string1 = "Listen"
string2 = "Silent"
#Listen → Silent
string1= string1.lower()
string2 = string2.lower()
stringlist1 = list(string1)
stringlist2 = list(string2)
stringlist1.sort()
stringlist2.sort()

if stringlist1 == stringlist2:
    print("two given strings are anagrams")
else:
    print("two given strings are not anagrams")

'''   
5. Write code to reverse the order of words in a sentence, without using built-in reverse functions
'''

string = "reverse the order of words in a sentence"
stringtemp =  string.split(" ")
stringtemp=stringtemp[::-1]
string = str(stringtemp)
string = ""
for word in stringtemp:
    string+=word+" "
print(string)

'''
6. Write a Python program to find the longest substring without repeating characters.
'''
def StrToSubstring(string)->list:
    settemp = set() 
    strtemp = ""
    strlist = []
    i=0
    while(i<len(string)):
        if string[i] not in settemp:
            settemp.add(string[i])
            strtemp +=string[i]
        else:
            i=i-1
            strlist.append(strtemp)
            strtemp = ""
            settemp.clear()
            
        if len(strtemp) == len(string):
            strlist.append(strtemp)
            break
        i=i+1
        
    return strlist


string  = "Testing strinstr"
strlist = StrToSubstring(string)

maxlen=0
subset=""
for li in strlist:
    if maxlen < len(li):
        maxlen = len(li)
        subset = li
print(subset,maxlen)

'''
7. Write a program to check if a string is a palindrome, ignoring spaces and punctuation,
'''
string = "321Reviver123"
temp = ""
for c  in string:
    if (c>= 'A'  and c <= 'Z') or (c >='a' and c<='z') or(c >='0' and c<='9' ):
       temp+=c
string = temp.lower()


if string == string[::-1]:
    print("palindrome")
else:
    print("Not palindrome")


'''
8. Write code to convert a string so that the first letter of each word is capitalized (like title case), without using .
with out using Title()
'''

string = "Write code to convert a string so that the first letter is capitalized"
temp = ""
setspace = False
temp += string[0].upper()
for i in range(1,len(string)):
    if string[i] ==' ' and string[i] !='\n':
        temp += string[i]
        temp += string[i+1].upper()
        setspace =True
    elif setspace == True:
        pass
        setspace = False
    else:
        temp += string[i]
        
print(temp)    
        
