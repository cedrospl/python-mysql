import math

f_smaller = 3.141592653589793
f_bigger = 3.87756392764

print(math.ceil(f_smaller), math.ceil(f_bigger))
print("\n")

print(math.floor(f_smaller), math.floor(f_bigger))
print("\n")

print(math.ceil(-f_smaller), math.ceil(-f_bigger))
print("\n")

print(math.floor(-f_smaller), math.floor(-f_bigger))
print("\n")


print(pow(2, 8), pow(9, 0.5))
print("\n")

print(math.sqrt(16))
print("\n")

print(math.pi, math.e)
print("\n")

print(math.sin(math.pi/2), math.cos(math.pi/4))
print("\n")

print('-------------------------------------------------')

# Moduł math - LAB

#1 - import modułu math na górze pliku

#2,3,4,5
degree1 = 360
rad1 = degree1 * math.pi/180
print("%d degree is %s radian" % (degree1, rad1))
print(math.radians(degree1))

degree2 = 45
rad2 = degree2 * math.pi/180
print("%d degree is %s radian" % (degree2, rad2))
print(math.radians(degree2))

print('-------------------------------------------------')

#6
small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

small_area = math.pi * small_pizza_r ** 2 / 10000
print(small_area)
big_area = math.pi * big_pizza_r ** 2 / 10000
print(big_area)
family_area = math.pi * family_pizza_r ** 2 / 10000
print(family_area)

small_area_price = small_pizza_price / small_area
print(small_area_price)

big_area_price = big_pizza_price / big_area
print(big_area_price)

family_area_price = family_pizza_price / family_area
print(family_area_price)

math_ls = dir(math)
print(math_ls)

print('-------------------------------------------------')
