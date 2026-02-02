s= "Apexon"  
print(s[::-1]) #reverse a string

s= "madam"  
print(s == s[::-1]) #rcheck palindrome 

s= "interviw"
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count +=1
        print(count) 

try:
    a=50
    b="Number"
    c=a/b
except TypeError:
    print("TypeError Exception Raised")