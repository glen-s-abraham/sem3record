"""String operations"""

str1=input("Enter a string?")
print("Length of string is:",len(str1))
print("Lowercase of string is:",str1.lower())
print("Uppercase of string is:",str1.upper())
print("Swapcase of string is:",str1.swapcase())
print("capitalized string is:",str1.capitalize())
print("Title  string is:",str1.title())
print("Left Stripped off _:",str1.lstrip('_'))
print("Right Stripped off _:",str1.rstrip('_'))
print("Stripped Both sides off _:",str1.strip('_'))
print("Maximum valued character:",max(str1))
r_str1=input("Enter a string to be replaced")
r_str2=input("Enter a string to replace with")
str1=str1.replace(r_str1,r_str2)
print("replaced String",str1)
r_str1=input("Enter a Character to Count")
print("Count fo character:",str1.count(r_str1))
print("Is String of alphabets:",str1.isalpha())
print("Is String of Digits:",str1.isdigit())
print("Is String of mixture of Digits and Alphabets:",str1.isalnum())
r_str1=input("Enter a Character to find index")
print("Index of character:",str1.index(r_str1))




