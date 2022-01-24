import random
from unicodedata import digit

uppercase_letters ="ABCDEFGHIJKLMNOPQSTUVWXYZ"
lowercase_letters =uppercase_letters.lower()

digit="0123456789"

symbols ="()[]{},:;!:/*#\\?+-_<>"

all =""
upper, lower, nums, syms= True,True,True,True

if upper:
    all +=uppercase_letters
if lower:
    all +=lowercase_letters    
if nums:
    all +=digit
if syms:
    all +=symbols


length = 20
amount = 20 

for caractere in range(amount):
    password= "".join(random.sample(all, length))
    print(password)