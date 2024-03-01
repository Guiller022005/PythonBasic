# Hipotenusa del triangulo
import math
cat_a= float(input("Ingresa el cateto a"))
cat_b= float(input("Ingresa el cateto b"))

hipo_c = (cat_a**2 + cat_b**2)
hipo_2 =  math.sqrt(hipo_c)
print("La hipotenusa del triangulo es ", hipo_2)