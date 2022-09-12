# (1) Python Program to Check if a Number is Ppsitive,Negative  or Zero.


a=int(input("Enter a Number"))
if a>0:
    print(a,"is positive")
elif a==0:
    print(a,"is Zero")
else:
    print(a,"is negative")


(2) #Write a Program to get the Fectorial number of given number
i=int(input("Enter Number"))
fac=1
while i>0:
    fac=fac*i
    i-=1
print("Factorial=",fac)



# (3) Write a Python program to get the Fibonacci series of given range.
'0 1 1 2 3 5 8 13 21 34 55 89'
n=int (input("Enter N:"))
a,b=0,1
print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b=b,a+b

#(4) How Memory is managed in Python.

#(5) What is purpose continue statement in python?

#(6) Write Python Program that swap two number with temp variable and without temp variable.
x=10
y=20
x,y=y,x
print(x,y)
#(7)Write Python Program to find whether a given number is even or odd,print out an appopriate message to the user.
num=int(input("Enter the number"))
if num/2==0:
    print("num,is even number")
else:
    print(num,"is a odd number")    

#(8)write Python Program to test whether a passed letter is a vowel or not.
ch=input("Enter the Alphabet :")
if ch in('a','e','i','o','u'):
    print(ch,"is a vowel")
else:    
     print(ch,"is a consonat")

#(9)Write a python program to sum of three given integers.However, if two values are equal sum will be zero.
a=int(input("enter a number A:"))
b=int(input("enter a number B:"))
c=int(input("enter a number c:"))
if a==b or b==c or c==a:
    print("sum of value is zero")
else:
    print("sum of value is",a+b+c)

#(10) Program that will return true if the two given intteger value 
a=int(input("enter a number A:"))
b=int(input("enter a number B:"))
if a==b or a+b==10 or a-b==10 or b-a==5:
    print("True")
else:
    print('False')

(11) program to count the number of characters (character frequency) in a string 
a=input("enter a string :")
b=input('charecter which want to count:')
c=0
for i in a:
    if i==b:
        c+=1
print(c)
print(a.count(b))


(12) program to count occurrences of a substring in a string. 
a=input("enter a string :")
b=input('substring which want to count:')
print(a.count(b))

(13) program to count the occurrences of each word in a given sentence 
s=input("enter a string :")
l=0
for i in s:
    if i.isalnum():
        l+=1
print("total number of character: ",l)

(14) program to get a single string from two given strings, separated by a space and swap the first two characters of each string.  
s=input("enter a string :")
w=input("enter a string :")
x=w[0:2]+s[2:]
y=s[0:2]+w[2:]
print("The string is ",x,y )

(15) program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. 
s=input("enter a string :")
if len(s)<=3:
    print(s)
elif s.endswith('ing'):
    print(s+"ly")
else:
    print(s+'ing') 
    

(16) program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.  
s="Rudra's condition is not poor."
print(s.replace(s[(s.find('not')):((s.find('poor'))+4)], 'good'))

(17) function that takes a list of words and returns the length of the longest one.
a=['Naresh', 'Suthar', 'Hasmukh', 'Ravi', 'Purushottam']
def fun(a):
    b=[]
    for i in a:
        b.append(len(i))
    print(max(b))
fun(a)

(18) Python function to reverses a string if its length is a multiple of 4. 
s= input("Enter a string: ")
def fun(a):
    if len(a)%4==0:
        for i in a[::-1]:
            print(i, end='')          
    else:
        print(a)
fun(s)


(19) Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
s= input("Enter a string: ")
if len(s)<2:
    print("Empty string")
elif len(s)==2:
    print(s*2)
else:
    print(s[0:2]+s[(len(s)-2):])

(20) Python function to insert a string in the middle of a string.  
s="My name is Ravi"
u=input("enter a substring: ")
n=int(input("enter number at which you want to change: "))
print(s[:n],u+s[n:])




