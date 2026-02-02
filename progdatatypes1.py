text = "My name is Gauri"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("numbaer of vowels:",count)


#print maximum and minimum numbers

numbers= [12,45,89,43,2,3,9,16,56,4,7]
print("Max:",max(numbers))
print("Min:",min(numbers))


#remove duplicatis numbers

numbers= [1,2,4,22,3,2,6,54,7,6,1]
unique= set(numbers)
print("unique numbers :",unique)



