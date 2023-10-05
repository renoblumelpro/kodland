import random
 

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("por favor ingrese la longitud de la contraseña"))
password = ""
for i in range(longitud):
    a = random.choice(seq= caracteres)
    password = password + a
print(password)