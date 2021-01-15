# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
import random

def password_gen(ma, mi, num, s_ch):
  
  mayus = ['A', 'B','C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  minus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  numbers = [0,1,2,3,4,5,6,7,8,9]
  special = ['!','¡','?','¿']
  password =[] 

  for i in range(0,ma):
    password.append(random.choice(mayus))
  for x in range(0,mi):
    password.append(random.choice(minus))
  for y in range(0,num):
    password.append(random.choice(numbers))
  for i in range(0,s_ch):
    password.append(random.choice(special))

  password = ''.join(str(x) for x in password)
  print(password)

  





ma = int(input('Write how many mayus you want for your password '))
mi = int(input('Write how many minus you want for your password '))
num = int(input('Write how many numbers you want for your password '))
s_ch = int(input('Write how many special characters you want for your password '))

password_gen(ma, mi, num, s_ch)