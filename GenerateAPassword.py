#Excercise 2.
#Generate a Random Password

import secrets

chars = 'abcdefghijklmnopqrstuvwxyz1234567890|!"#$%&/()=?¡´+}[]*?¡'
password = ''

for i in range(10):
    password += secrets.choice(chars)

print("Your random password is:", password)
print("\n")

