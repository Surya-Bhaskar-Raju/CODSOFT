import random
import string

lowercase=string.ascii_lowercase
uppercase=string.ascii_uppercase
numbers=string.digits
symbols=string.punctuation
all_characters=uppercase+lowercase+numbers+symbols


password=''

password+=random.choice(uppercase)+random.choice(lowercase)+random.choice(numbers)+random.choice(symbols)

n=int(input('Enter the length of the password required:'))

for i in range(n-4):
    password+=random.choice(all_characters)
    
print(password)

